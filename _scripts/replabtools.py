""" Functions for working with Reportlab.
"""

from pathlib import Path

import numpy as np


def theta_diag(x1, y1, x2, y2):
    """ Angle, diagonal length for rect defined by points `x1`,`y1`,`x2`,`y2`

    Returns
    -------
    theta : float
        Angle in radians of diagonal *from second point to first*, where angle
        is angle to ray from the origin through (0, 1).
    """
    dx = x1 - x2
    dy = y1 - y2
    r = np.sqrt(dx ** 2 + dy ** 2)
    theta = np.arctan2(dy, dx)
    return theta, r


def draw_wedge_pts(canvas, x1, y1, x2, y2, extent):
    theta, r = theta_diag(x1, y1, x2, y2)
    draw_wedge_theta(canvas, theta, r, x2, y2, extent)
    return theta, r


def draw_wedge_theta(canvas, theta, r, x, y, extent_deg):
    angle = theta * 180 / np.pi
    canvas.wedge(x - r, y - r, x + r, y + r,
                 angle - extent_deg / 2, extent_deg, fill=1)


def prop_points(pcts, x, y, theta, L):
    pt_L = np.array(pcts) * L
    dx = np.cos(theta) * pt_L
    dy = np.sin(theta) * pt_L
    return x + dx, y + dy


def draw_line_arrow(canvas,
                    x1, y1, x2, y2,
                    arrow_prop=0.15,
                    extent_deg=15):
    theta, L = theta_diag(x1, y1, x2, y2)
    draw_line_arrow_theta(canvas, x2, y2, theta, L, arrow_prop, extent_deg)


def draw_line_arrow_theta(canvas, x, y, theta, L,
                          arrow_prop=0.15,
                          extent_deg=15):
    (x_a, x1), (y_a, y1) = prop_points([arrow_prop, 1], x, y, theta, L)
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
