""" File to calculate volume means, detect outliers

When run as a script, print out values for given Nipraxis file.
"""

# New import of sys.
import sys

import numpy as np

import nibabel as nib

import nipraxis

def vol_means(image_fname):
    """ Calculate volume means from 4D image `image_fname`
    """
    img = nib.load(image_fname)
    data = img.get_fdata()
    means = []
    for i in range(data.shape[-1]):
        vol = data[..., i]
        means.append(np.mean(vol))
    return np.array(means)


def detect_outliers_fixed(some_values, n_stds=2):
    overall_mean = np.mean(some_values)
    overall_std = np.std(some_values)
    thresh = overall_std * n_stds
    is_outlier = np.abs(some_values - overall_mean) > thresh
    return np.where(is_outlier)[0]


if __name__ == '__main__':
    # New: using sys to get first argument.
    nipraxis_fname = sys.argv[1]
    data_fname = nipraxis.fetch_file(nipraxis_fname)
    means = vol_means(data_fname)
    print(detect_outliers_fixed(means))
