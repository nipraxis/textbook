""" Script to run SPM processing in nipype
"""
import shutil

import nibabel as nib

# Import our own configuration for nipype
import nipype_settings

import nipype.interfaces.spm as spm

# Start at the original image
base_fname = 'ds114_sub009_t2r1.nii'
structural_orig = 'ds114_sub009_highres.nii'
structural_fname = 'cds114_sub009_highres.nii'

# Copy the structural, because SPM will modify it
shutil.copyfile(structural_orig, structural_fname)

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
img = nib.load(base_fname);
dropped_img = nib.Nifti1Image(img.get_data()[..., n_dummies:],
                              img.affine,
                              img.header)
nib.save(dropped_img, 'f' + base_fname)

# Slice time correction
num_slices = img.shape[2]
time_for_one_slice = TR / num_slices
TA = TR - time_for_one_slice
st = spm.SliceTiming()
st.inputs.in_files = 'f' + base_fname
st.inputs.num_slices = num_slices
st.inputs.time_repetition = TR
st.inputs.time_acquisition = TA
st.inputs.slice_order = order_func(num_slices)
st.inputs.ref_slice = slice_time_ref_slice
st.run()

# Realign
realign = spm.Realign()
realign.inputs.in_files = 'af' + base_fname
# Do not write resliced files, do write mean image
realign.inputs.write_which = write_which
realign.run()

# Coregistration
coreg = spm.Coregister()
# Coregister structural to mean image from realignment
coreg.inputs.target = 'meanaf' + base_fname
coreg.inputs.source = structural_fname
coreg.run()

# Normalization / resampling with combined realign and normalization params
seg_norm = spm.Normalize12()
seg_norm.inputs.image_to_align = structural_fname
seg_norm.inputs.apply_to_files = 'af' + base_fname
seg_norm.inputs.write_bounding_box = bounding_box
seg_norm.run()

# Smoothing by 8mm FWHM in x, y and z
smooth = spm.Smooth()
smooth.inputs.in_files = 'waf' + base_fname
smooth.inputs.fwhm = [8, 8, 8]
smooth.run()
