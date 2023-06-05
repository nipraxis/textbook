""" Run non-linear registration using Dipy
"""

import os
import pickle
from pathlib import Path

import numpy as np
import numpy.linalg as npl

import nibabel as nib
from nibabel.affines import to_matvec

from scipy.ndimage import affine_transform

from dipy.align.imaffine import (MutualInformationMetric, AffineRegistration)
from dipy.align.transforms import (TranslationTransform3D,
                                   RigidTransform3D,
                                   AffineTransform3D)
from dipy.align.imwarp import SymmetricDiffeomorphicRegistration
from dipy.align.metrics import CCMetric


TEMPLATE_IMG = 'mni_icbm152_t1_tal_nlin_asym_09a.nii'
TEMPLATE_MASK = 'mni_icbm152_t1_tal_nlin_asym_09a_mask.nii'


def as_image(image):
    """ If `image` is string, assume filename and load image, else pass through
    """
    if isinstance(image, str):
        image = nib.load(image)
    return image


def apply_mask(brain_img, mask_img):
    """ Load brain image, matching mask; apply and return masked image

    Parameters
    ----------
    brain_img : str or image
        string giving image filename or image object
    mask_img : str or image
        string giving mask image filename or image object.  Mask must match
        `brain_img` after mapping with image and mask affine.

    Returns
    -------
    mask_img : image object
        image object where data is data from `brain_img` multiplied elementwise
        by the data of `mask_img`, where the mask data has[ been resampled into
        the voxel space of `brain_img` if necessary.
    """
    brain_img = as_image(brain_img)
    b_aff = brain_img.affine
    b_hdr = brain_img.header
    mask_img = as_image(mask_img)
    brain_data = brain_img.get_fdata()
    mask_data = mask_img.get_fdata()
    if not np.allclose(b_aff, mask_img.affine):
        # Mask and brain have different affines - we need to resample
        brain2mask = npl.inv(mask_img.affine) @ brain_img.affine
        mat, vec = to_matvec(brain2mask)
        mask_data = affine_transform(mask_data, mat, vec,
                                     output_shape=brain_data.shape,
                                     order=0)  # nearest neighbor
    return nib.Nifti1Image(brain_data * mask_data, b_aff, b_hdr)


def register_affine(t_masked, m_masked, affreg=None,
                    final_iters=(10000, 1000, 100)):
    """ Run affine registration between images `t_masked`, `m_masked`

    Parameters
    ----------
    t_masked : image
        Template image object, with image data masked to set out-of-brain
        voxels to zero.
    m_masked : image
        Moving (individual) image object, with image data masked to set
        out-of-brain voxels to zero.
    affreg : None or AffineRegistration instance, optional
        AffineRegistration with which to register `m_masked` to `t_masked`.  If
        None, we make an instance with default parameters.
    final_iters : tuple, optional
        Length 3 tuple of level iterations to use on final affine pass of the
        registration.

    Returns
    -------
    affine : shape (4, 4) ndarray
        Final affine mapping from voxels in `t_masked` to voxels in `m_masked`.
    """
    if affreg is None:
        metric = MutualInformationMetric(nbins=32,
                                         sampling_proportion=None)
        affreg = AffineRegistration(metric=metric)
    t_data = t_masked.get_fdata()
    m_data = m_masked.get_fdata()
    t_aff = t_masked.affine
    m_aff = m_masked.affine
    translation = affreg.optimize(t_data, m_data, TranslationTransform3D(),
                                  None, t_aff, m_aff)
    rigid = affreg.optimize(t_data, m_data, RigidTransform3D(), None, t_aff,
                            m_aff, starting_affine=translation.affine)
    # Maybe bump up iterations for last step
    if final_iters is not None:
        affreg.level_iters = list(final_iters)
    affine = affreg.optimize(t_data, m_data, AffineTransform3D(), None, t_aff,
                             m_aff, starting_affine=rigid.affine)
    return affine.affine


def register_diffeo(t_masked, m_masked, start_affine, registration=None):
    """ Run non-linear registration between `t_masked` and `m_masked`

    Parameters
    ----------
    t_masked : image
        Template image object, with image data masked to set out-of-brain
        voxels to zero.
    m_masked : image
        Moving (individual) image object, with image data masked to set
        out-of-brain voxels to zero.
    start_affine : shape (4, 4) ndarray
        Affine mapping from voxels in `t_masked` to voxels in `m_masked`.
    registration : None or SymmetricDiffeoMorphicRegistration instance
        Registration instance we will use to register `t_masked` and
        `m_masked`.  If None, make a default registration object.

    Returns
    -------
    mapping : mapping instance
        Instance giving affine + non-linear mapping between voxels in
        `t_masked` and voxels in `m_masked`.
    """
    if registration is None:
        registration = SymmetricDiffeomorphicRegistration(
            metric=CCMetric(3),
            level_iters=[10, 10, 5])
    return registration.optimize(t_masked.get_fdata(),
                                 m_masked.get_fdata(),
                                 t_masked.affine,
                                 m_masked.affine,
                                 start_affine)


def register_save(template_fname, template_mask_fname,
                  moving_fname, moving_mask_fname):
    """ Resister individual image `moving_fname` to template `template_fname`

    Save warped image and mapping object to directory of `moving_fname`.

    Parameters
    ----------
    template_fname : str
        string giving image filename of template image to register to
    template_mask_fname : str
        string giving image filename of brain mask corresponding to
        `template_fname`
    moving_fname : str
        string giving image filename of individual image to register
    moving_mask_fname : str
        string giving image filename of brain mask corresponding to
        `moving_fname`

    Returns
    -------
    mapping : mapping instance
        Instance giving affine + non-linear mapping between voxels in
        `template_fname` and voxels in `moving_fname`.
    """
    mv_pth = Path(moving_fname)
    root = mv_pth.stem
    if root.endswith('.gz'):
        root = root[:-3]
    t_masked = apply_mask(template_fname, template_mask_fname)
    m_masked = apply_mask(moving_fname, moving_mask_fname)
    affine = register_affine(t_masked, m_masked)
    mapping = register_diffeo(t_masked, m_masked, affine)
    masked_data = m_masked.get_fdata()
    warped_moving = nib.Nifti1Image(mapping.transform(masked_data),
                                    t_masked.affine,
                                    t_masked.header)
    nib.save(warped_moving, mv_pth.with_name('w_' + mv_pth.name))
    mv_pth.with_name(f'map_{root}.pkl').write_bytes(pickle.dumps(mapping))
    return mapping


def as_mapping(mapping):
    """ If `mapping` is string, assume filename, load pickle, else pass through
    """
    if isinstance(mapping, ):
        with open(mapping, 'rb') as fobj:
            mapping = pickle.load(fobj)
    return mapping


def write_warped(fname, mapping, interpolation='nearest', template_header=None):
    """ Warp an image in individual space to template space

    Parameters
    ----------
    fmame : str
        Filename of image to warp in template space
    mapping : mapping instance
        object containing mapping from individual space to template space
    interpolation : str, optional
        interpolation to use when resampling data from `fname`
    template_header : None or header instance
        template header with which to save image.  If None, use default header.
    """
    img = nib.load(fname)
    mapping = as_mapping(mapping)
    template_affine = mapping.codomain_grid2world
    data = img.get_fdata()
    warped = mapping.transform(data, interpolation=interpolation)
    warped_img = nib.Nifti1Image(warped, template_affine, template_header)
    path = Path(fname)
    nib.save(warped_img, path.with_name('w_' + path.name))


def find_anatomicals(root):
    """ Find anatomical image, mask pairs from OpenFMRI directory root `root`

    Parameters
    ----------
    root : str
        root directory of OpenFMRI dataset - e.g. "ds114"

    Returns
    -------
    anatomicals : list
        List of anatomical, mask image pairs for each subject in `root`
    """
    anatomicals = []
    for dirpath, dirnames, filenames in os.walk(root):
        if not 'highres001.nii.gz' in filenames:
            continue
        pth = Path(dirpath)
        full_image = pth / 'highres001.nii.gz'
        mask_image = pth / 'highres001_brain_mask.nii.gz'
        assert full_image.is_file()
        assert mask_image.is_file()
        anatomicals.append((str(mask_image), str(full_image)))
    return anatomicals


def sub2img_mask(root, sub_no):
    """ Return anatomical image, mask pair from OpenFMRI root, subject no

    Parameters
    ----------
    root : str
        root directory of OpenFMRI dataset - e.g. "ds114"
    sub_no : int
        subject no, where 1 is the first subject

    Returns
    -------
    anatomical_fname : str
        filename of anatomical image, beginning with path `root`
    mask_fname : str
        filename of anatomical image brain mask, beginning with path `root`
    """
    anatomical_path = Path(root) / 'sub{:03d}'.format(sub_no) / 'anatomy'
    imgs = (anatomical_path / 'highres001.nii.gz',
            anatomical_path / 'highres001_brain_mask.nii.gz')
    if all(p.is_file() for p in imgs):
        return tuple(str(p) for p in imgs)
    return ()


def write_highres(root):
    """ Calculate parameters, write anatomicals from OpenFMRI directory `root`

    Parameters
    ----------
    root : str
        root directory of OpenFMRI dataset - e.g. "ds114"
    """
    for moving_img, moving_mask in find_anatomicals(root):
        register_save(TEMPLATE_IMG, TEMPLATE_MASK,
                      moving_img, moving_mask)


def write_highres_parallel(root):
    """ Calculate parameters, write anatomicals from OpenFMRI directory `root`

    Use parallel execution.  Careful, this can crash your machine with too many
    images found at `root`.

    Parameters
    ----------
    root : str
        root directory of OpenFMRI dataset - e.g. "ds114"
    """
    import multiprocessing
    jobs = []
    for moving_img, moving_mask in find_anatomicals(root):
        p = multiprocessing.Process(target=register_save, args=(
            TEMPLATE_IMG, TEMPLATE_MASK, moving_img, moving_mask))
        jobs.append(p)
        p.start()


def register_subject(root, sub_no):
    """ Calculate parameters, write anatomical for subject at OpenFMRI `root`

    Parameters
    ----------
    root : str
        root directory of OpenFMRI dataset - e.g. "ds114"
    sub_no : int
        subject no, where 1 is the first subject

    Returns
    -------
    mapping : mapping instance
        Instance giving affine + non-linear mapping between voxels in
        `t_masked` and voxels in `m_masked`.
    """
    moving_img, moving_mask = sub2img_mask(root, sub_no)
    return register_save(TEMPLATE_IMG, TEMPLATE_MASK,
                         moving_img, moving_mask)
