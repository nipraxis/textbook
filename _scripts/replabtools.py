""" Functions for working with Reportlab.
"""

from pathlib import Path

import numpy as np


def theta_diag(x1, y1, x2, y2):
    """ Angle, diagonal length for rect defined by points `x1`,`y1`,`x2`,`y2`

    Parameters
    ----------
    x1 : float
        x coordinate of first corner.
    y1 : float
        y coordinate of first corner.
    x2 : float
        x coordinate of second corner, diagonally opposite to first.  Can be
        greater or less than `x1`.
    y2 : float
        y coordinate of second corner, diagonally opposite to first.  Can be
        greater or less than `y1`.

    Returns
    -------
    theta : float
        Angle in radians of diagonal *from second point to first*, where angle
        is angle to ray from the origin through (0, 1).
    L : float
        Length of diagnonal joining ``(x1, y1)`` and ``(x2, y2)``.
    """
    dx = x1 - x2
    dy = y1 - y2
    L = np.sqrt(dx ** 2 + dy ** 2)
    theta = np.arctan2(dy, dx)
    return theta, L


def draw_wedge_pts(canvas, x1, y1, x2, y2, extent_deg):
    """ Draw wedge from (`x1`, `y1`) with point at (`x2`, `y2`).

    Parameters
    ----------
    canvas : canvas object
        Canvas object implementing methods ``line`` and ``wedge``.
    x1 : float
        x coordinate of center of thick end of wedge.
    y1 : float
        y coordinate of center of thick end of wedge.
    x2 : float
        x coordinate of thin end of wedge.
    y2 : float
        y coordinate of thin end of wedge.
    extent_deg : float
        Arc of wedge in degrees.

    Returns
    -------
    theta : float
        Angle in radians of diagonal *from second point to first*, where angle
        is angle to ray from the origin through (0, 1).
    L : float
        Length of diagnonal joining ``(x1, y1)`` and ``(x2, y2)``.
    """
    theta, L = theta_diag(x1, y1, x2, y2)
    draw_wedge_theta(canvas, theta, L, x2, y2, extent_deg)
    return theta, L


def draw_wedge_theta(canvas, theta, L, x, y, extent_deg):
    """ Draw wedge length `r` with point at (`x`, `y`) and angle `theta`.

    Parameters
    ----------
    canvas : canvas object
        Canvas object implementing methods ``line`` and ``wedge``.
    theta : float
        Angle in radians of wedge center line where angle is angle to
        horizontal ray from (`x`, `y`) through (`x` + 1, `y').
    L : float
        Length of wedge.
    x : float
        x coordinate of thin end of wedge.
    y : float
        y coordinate of thin end of wedge.
    extent_deg : float
        Arc of wedge in degrees.

    Returns
    -------
    None
    """
    angle = theta * 180 / np.pi
    canvas.wedge(x - L, y - L, x + L, y + L,
                 angle - extent_deg / 2, extent_deg, fill=1)


def pts_along_line(lengths, x, y, theta):
    """ Points at `lengths` along line given by start (`x`, `y`), angle `theta`

    Parameters
    ----------
    lengths : array-like of float
        Lengths along which to travel on line.
    x : float
        x coordinate of line origin.
    y : float
        y coordinate of line origin.
    theta : float
        Angle in radians of line where angle is angle of line to horizontal ray
        from (`x`, `y`) through (`x` + 1, `y').

    Returns
    -------
    x_coords : array
        x coordinates of corresponding points.
    y_coords : array
        y coordinates of corresponding points.
    """
    lengths = np.array(lengths)
    dx = np.cos(theta) * lengths
    dy = np.sin(theta) * lengths
    return x + dx, y + dy


def draw_line_arrow(canvas,
                    x1, y1, x2, y2,
                    arrow_prop=0.15,
                    extent_deg=15):
    """ Draw line from `x1`,`y1` to `x2`,`y2`, with arrow to `x2`, `y2`.

    Parameters
    ----------
    canvas : canvas object
        Canvas object implementing methods ``line`` and ``wedge``.
    x1 : float
        x coordinate of line start.
    y1 : float
        y coordinate of line start.
    x2 : float
        x coordinate of line end (end pointed to by arrow).
    y2 : float
        y coordinate of line end (end pointed to by arrow).
    arrow_prop : float, optional
        Proportion of line length to be taken up by arrow.
    extent_deg : float, optional
        Arc of wedge for arrow in degrees.

    Returns
    -------
    theta : float
        Angle in radians of line *from end to start*, where angle
        is angle to ray from (`x2`, `y2`) through (`x2` + 1, `y2`).
    L : float
        Length of line joining ``(x1, y1)`` and ``(x2, y2)``.
    """
    theta, L = theta_diag(x1, y1, x2, y2)
    draw_line_arrow_theta(canvas, x2, y2, theta, L, arrow_prop, extent_deg)
    return theta, L


def draw_line_arrow_theta(canvas, x, y, theta, L,
                          arrow_prop=0.15,
                          extent_deg=15):
    """ Arrow-headed line back from `x`, `y` at angle `theta` and length `L`

    The arrow points to (`x`, `y`).

    Parameters
    ----------
    canvas : canvas object
        Canvas object implementing methods ``line`` and ``wedge``.
    x : float
        x coordinate of line end (end at which arrow points).
    y : float
        y coordinate of line end (end at which arrow points).
    theta : float
        Angle in radians of line where angle is angle of line to horizontal ray
        from (`x`, `y`) through (`x` + 1, `y').
    L : float
        Length of line.
    arrow_prop : float, optional
        Proportion of line length to be taken up by arrow.
    extent_deg : float, optional
        Arc of wedge for arrow in degrees.
    """
    (x_a, x1), (y_a, y1) = pts_along_line([arrow_prop * L, L], x, y, theta)
    canvas.line(x1, y1, x_a, y_a)
    draw_wedge_theta(canvas, theta, arrow_prop * L, x, y, extent_deg)


def test_page():
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    width, height = A4
    x, y = width / 2, height / 2

    HERE = Path(__file__).parent.absolute()
    out_path = str(HERE / 'test_wedge.pdf')
    canvas = canvas.Canvas(out_path)

    x2, y2 = x - 50, y + 100
    canvas.circle(x, y, 5)
    canvas.circle(x2, y2, 5)
    draw_line_arrow(canvas, x, y, x2, y2)
    canvas.save()
