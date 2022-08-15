""" Script to draw illustration of reshaping
"""

from pathlib import Path
import sys
from subprocess import check_call

import numpy as np
import pandas as pd

from reportlab.lib.pagesizes import inch
from reportlab.lib import colors
from reportlab.lib.colors import PCMYKColor
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas

import nipraxis

HERE = (Path(__file__).parent / '..').absolute()
sys.path.append(str(HERE))

import replabtools as rlt

# Fetch the file.
stim_fname = nipraxis.fetch_file('24719.f3_beh_CHYM.csv')
data = pd.read_csv(stim_fname).iloc[:15]
trial_isis = np.array(data['trial_ISI'])
response_times = np.array(data['response_time'])

exp_onsets = np.cumsum(trial_isis)
scanner_onsets = exp_onsets + 4000

out_path = str(HERE / 'images' / '2d_reshape.pdf')
canvas = canvas.Canvas(out_path)

# container for the 'Flowable' objects
elements = []

arr = np.stack([scanner_onsets, response_times], axis=1)
m, n = arr.shape
in_data = arr.astype('U10').tolist()
t=Table(in_data, n * [0.6 * inch], m * [0.4 * inch])
t.setStyle(TableStyle([
    ('TEXTFONT', (0, 0), (-1, -1), 'Courier'),
    ('ALIGN',(0, 0), (-1, -1),'CENTER'),
    ('VALIGN',(0, 0), (-1, -1),'MIDDLE'),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
]))

t.wrapOn(canvas, 400, 100)
t.drawOn(canvas, 0, 0)
cps = np.array(t._colpositions)
col_width = np.mean(np.diff(cps))
cps = cps[:-1] + col_width / 2
rps = np.array(t._rowpositions)
row_height = np.mean(-np.diff(rps))
rps = rps[:-1] - row_height / 2
red = PCMYKColor(0,100,100,0)
red50transparent = red.clone(alpha=50)
canvas.setStrokeColor(red50transparent)
canvas.setFillColor(red50transparent)
canvas.setLineWidth(2)

arr_prop = 0.1
extent_deg = 40

# Straight line.
left, right = cps
y1, y2 = rps[:2]
(hx1, hx2), _ = rlt.prop_points([0.20, 0.80], left, y1, 0, right-left)
line_len = hx2 - hx1
# Get parameters from first diagonal line
dtheta, vL = rlt.theta_diag(left, y2, right, y1)
(vx1, vx2), v_ys = rlt.prop_points([0.20, 0.80], right, y1, dtheta, vL)
dvy1, dvy2 = v_ys - y1

last_rn = len(rps) - 1
arr_prop = 0.1
extent_deg = 60
for i, rp in enumerate(rps):
    rlt.draw_line_arrow_theta(canvas, hx2, rp, np.pi, line_len,
                              arrow_prop=arr_prop, extent_deg=extent_deg)
    if i == last_rn:
        break
    rlt.draw_line_arrow(canvas,
                        vx1, rp + dvy1, vx2, rp + dvy2,
                        arrow_prop=arr_prop,
                        extent_deg=extent_deg)
canvas.save()

check_call(['inkscape',  '--export-area-drawing',
            '--export-type=svg', out_path])
