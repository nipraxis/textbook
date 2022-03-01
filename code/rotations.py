""" Rotation matrices for rotations around x, y, z axes

See: https://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations
"""

import numpy as np


def x_rotmat(theta):
    """ Rotation matrix for rotation of `theta` radians around x axis

    Parameters
    ----------
    theta : scalar
        Rotation angle in radians

    Returns
    -------
    M : shape (3, 3) array
        Rotation matrix
    """
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    return np.array([[1, 0, 0],
                     [0, cos_t, -sin_t],
                     [0, sin_t, cos_t]])


def y_rotmat(theta):
    """ Rotation matrix for rotation of `theta` radians around y axis

    Parameters
    ----------
    theta : scalar
        Rotation angle in radians

    Returns
    -------
    M : shape (3, 3) array
        Rotation matrix
    """
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    return np.array([[cos_t, 0, sin_t],
                     [0, 1, 0],
                     [-sin_t, 0, cos_t]])


def z_rotmat(theta):
    """ Rotation matrix for rotation of `theta` radians around z axis

    Parameters
    ----------
    theta : scalar
        Rotation angle in radians

    Returns
    -------
    M : shape (3, 3) array
        Rotation matrix
    """
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    return np.array([[cos_t, -sin_t, 0],
                     [sin_t, cos_t, 0],
                     [0, 0, 1]])
