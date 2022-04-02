""" Create Boolean indexing graphic

Copyright Matthew Brett

BSD 2-clause license
"""

import os
import os.path as op
from subprocess import check_call

import numpy as np
import pandas as pd

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                Paragraph)

HERE = op.dirname(__file__)

course_fname = op.join(HERE, '..', 'data', 'rate_my_course.csv')
big_courses = pd.read_csv(course_fname).head(6)
# Put the columns into arrays
disciplines = np.array(big_courses['Discipline'])
easiness = np.array(big_courses['Easiness'])
quality = np.array(big_courses['Overall Quality'])

pdf_fname = op.join(HERE, "easiness_values.pdf")
doc = SimpleDocTemplate(pdf_fname, pagesize=letter)

col_widths = 34
easy_list = [round(e, 2) for e in easiness]
t1 = Table([easy_list],
           colWidths=col_widths)
grid_stuff = [
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ]
t1.setStyle(TableStyle(grid_stuff))

greater_than_3 = easiness > 3

# Grey out the False values
false_cols = np.where(~greater_than_3)[0]
backgrounds = [('BACKGROUND', (i, 0), (i, 0), colors.gray)
               for i in false_cols]

t2 = Table([list(greater_than_3)],
           colWidths=col_widths)
t2.setStyle(TableStyle(grid_stuff))

t3 = Table([[''] * len(greater_than_3)],
           colWidths=col_widths)
t3.setStyle(TableStyle(grid_stuff + backgrounds))

t4 = Table([easy_list],
           colWidths=col_widths)
t4.setStyle(TableStyle(grid_stuff + backgrounds))

t5 = Table([[round(e, 2) for e in easiness[greater_than_3]]],
           colWidths=col_widths)
t5.setStyle(TableStyle(grid_stuff))

style = getSampleStyleSheet()['Normal']
style.leading = 24
style.spaceBefore = 24

def dp(text, table):
    return [Paragraph(text, style), table]

# write the document to disk
doc.build(sum([
    dp('<b>easiness</b>:', t1),
    dp('<b>greater_than_3</b>:', t2),
    dp('<b>greater_than_3</b> displayed as white for True, gray for False',
       t3),
    dp('<b>easiness</b> overlaid with <b>greater_than_3</b>:', t4),
    dp('<b>easiness[greater_than_3]</b>:', t5),
], []))


def write_png(pdf_fname):
    # From some TeX distribution.
    check_call(['pdfcrop', pdf_fname,
                '--margins', '10 10 10 10',
                pdf_fname])

    # ImageMagick
    png_fname = op.splitext(pdf_fname)[0] + '.png'
    check_call(['convert', '-strip',
                '-density', '300',
                pdf_fname,
                png_fname])
    os.unlink(pdf_fname)

write_png(pdf_fname)

other_array = op.join(HERE, "easiness_reused.pdf")
o_doc = SimpleDocTemplate(other_array, pagesize=letter)

col_widths = 70
o_t1 = Table([list(disciplines)],
           colWidths=col_widths)
o_t1.setStyle(TableStyle(grid_stuff))

o_t1a = Table([easy_list],
              colWidths=col_widths)
o_t1a.setStyle(TableStyle(grid_stuff))

o_t2 = Table([list(greater_than_3)],
             colWidths=col_widths)
o_t2.setStyle(TableStyle(grid_stuff))

o_t3 = Table([[''] * len(greater_than_3)],
             colWidths=col_widths)
o_t3.setStyle(TableStyle(grid_stuff + backgrounds))

o_t4 = Table([list(disciplines)],
             colWidths=col_widths)
o_t4.setStyle(TableStyle(grid_stuff + backgrounds))

o_t5 = Table([list(disciplines[greater_than_3])],
             colWidths=col_widths)
o_t5.setStyle(TableStyle(grid_stuff))

# write the document to disk
o_doc.build(sum([
    dp('<b>disciplines</b>:', o_t1),
    dp('<b>easiness</b>:', o_t1a),
    dp('<b>greater_than_3</b>:', o_t2),
    dp('<b>greater_than_3</b> displayed as white for True, gray for False',
       o_t3),
    dp('<b>disciplines</b> overlaid with <b>greater_than_3</b>:', o_t4),
    dp('<b>disciplines[greater_than_3]</b>:', o_t5),
], []))

write_png(other_array)
