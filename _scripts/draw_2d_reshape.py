""" Script to draw illustration of reshaping
"""

from pathlib import Path

import numpy as np
import pandas as pd

from reportlab.lib.pagesizes import inch
from reportlab.lib import colors
from reportlab.lib.colors import PCMYKColor
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas

import nipraxis

HERE = (Path(__file__).parent / '..').absolute()

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
    ('ALIGN',(0, 0),(-1, -1),'CENTER'),
    ('VALIGN',(0, 0),(-1, -1),'MIDDLE'),
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
n = len(rps)
red = PCMYKColor(0,100,100,0)
red50transparent = red.clone(alpha=50)
canvas.setStrokeColor(red50transparent)
canvas.setLineWidth(2)
w_y = 15
w_x = 8
angle = np.arctan(row_height / col_width)
arr_start_deg = angle * 180 / np.pi - 5
w_y_d = w_x * np.sin(angle)
w_x_d = w_x * np.cos(angle)
L, R = cps
for i, rp in enumerate(rps):
    canvas.line(L + w_x, rp, R - w_x - 1, rp)
    canvas.wedge(R - w_x, rp - w_y, R, rp + w_y, 175, 10)
    if i < n - 1:
        rp_p1 = rps[i + 1]
        canvas.line(
            R - w_x_d, rp - w_y_d, L + w_x_d, rp_p1 + w_y_d)
        canvas.wedge(
            L + w_x_d, rp_p1 - w_y_d, L + w_x_d, rp_p1 + w_y_d, arr_start_deg, 10)
canvas.save()
