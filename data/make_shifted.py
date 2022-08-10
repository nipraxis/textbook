""" Make shifted data for exercise.
"""

import nibabel as nib
import nipraxis

# Fetch image file.
bold_fname = nipraxis.fetch_file('ds114_sub009_t2r1.nii')
img = nib.load(bold_fname)
data = img.get_fdata()

unshifted = data[..., 100]
shifted = data[..., 101]

# Resample by a few voxels.


# Write both
nib.save(nib.Nifti1Image(unshifted, None, unshifted.header), 'unshifted.nii')
nib.save(nib.Nifti1Image(shifted, None, unshifted.header), 'shifted.nii')
