""" Script to run SPM processing in nipype
"""
from pathlib import Path

import nibabel as nib

from nipraxis import fetch_file

# Import our own configuration for nipype
import nipype_settings

import nipype.interfaces.spm as spm


def add_pref_suf(pth, prefix='', suffix=''):
    """ Add prefix `prefix` and suffix `suffix` to filename `pth`
    """
    pth = Path(pth)
    return pth.with_name(prefix + pth.stem + suffix + pth.suffix)


def copyfile(in_path, out_dir):
    """ Copy file `in_path` to directory `out_dir`
    """
    in_path = Path(in_path)
    out_path = Path(out_dir) / in_path.name
    out_path.write_bytes(in_path.read_bytes())
    return out_path


out_dir = Path('spm_processing')
if not out_dir.is_dir():
    out_dir.mkdir()

func_path = copyfile(fetch_file('ds114_sub009_t2r1.nii'), out_dir)
anat_path = copyfile(fetch_file('ds114_sub009_highres.nii'), out_dir)

# Analysis parameters
TR = 2.5
slice_time_ref_slice = 1  # 1-based indexing
n_dummies = 4
# Realign "write_which" input. The 0 means 'do not write resampled versions of
# any of the individual volumes`.  The 1 means 'write mean across volumes after
# motion correction'.  See config/spm_cfg_realign.m in the SPM12 distribution.
write_which = [0, 1]
# Normalize write parameters.  Bounding box gives extreme [[left, posterior,
# inferior], [right, anterior, superior]] millimeter coordinates of the voxel
# grid that SPM will use to write out the new images in template space.  See
# spm_preproc_write8.m for use of the bounding box values.
bounding_box = [[-78., -112., -46.], [78., 76., 86.]]


def ascending_interleaved(num_slices):
    """ Return acquisition ordering given number of slices

    Note 1-based indexing for MATLAB.

    Return type must be a list for nipype to use it in the SPM interface
    without error.
    """
    odd = range(1, num_slices + 1, 2)
    even = range(2, num_slices + 1, 2)
    return list(odd) + list(even)


order_func = ascending_interleaved

# Drop dummy volumes
dummied = add_pref_suf(func_path, 'f')
img = nib.load(func_path);
dropped_img = nib.Nifti1Image(img.get_fdata()[..., n_dummies:],
                              img.affine,
                              img.header)
nib.save(dropped_img, dummied)

# Slice time correction
num_slices = img.shape[2]
time_for_one_slice = TR / num_slices
TA = TR - time_for_one_slice
st_dummied = add_pref_suf(dummied, 'a')
st = spm.SliceTiming()
st.inputs.in_files = dummied
st.inputs.num_slices = num_slices
st.inputs.time_repetition = TR
st.inputs.time_acquisition = TA
st.inputs.slice_order = order_func(num_slices)
st.inputs.ref_slice = slice_time_ref_slice
st.run()

# Realign
mc_st_dummied = add_pref_suf(st_dummied, 'r')
realign = spm.Realign()
realign.inputs.in_files = st_dummied
# Do not write resliced files, do write mean image
realign.inputs.write_which = write_which
realign.run()

# Coregistration
mc_mean_path = add_pref_suf(st_dummied, 'mean')
coreg = spm.Coregister()
# Coregister structural to mean image from realignment
coreg.inputs.target = mc_mean_path
coreg.inputs.source = anat_path
coreg.run()

# Normalization / resampling with combined realign and normalization params
seg_norm = spm.Normalize12()
seg_norm.inputs.image_to_align = anat_path
seg_norm.inputs.apply_to_files = st_dummied
seg_norm.inputs.write_bounding_box = bounding_box
seg_norm.run()

# Smoothing by 8mm FWHM in x, y and z
w_st_dummied = add_pref_suf(st_dummied, 'w')
smooth = spm.Smooth()
smooth.inputs.in_files = w_st_dummied
smooth.inputs.fwhm = [8, 8, 8]
smooth.run()
