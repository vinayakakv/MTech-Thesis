#!/usr/bin/env python

"""
Pandoc filter to convert divs with class="small" to LaTeX
blocks prepended with \small, then reverting to \normalize
"""

from panflute import Div, RawBlock, toJSONFilter

def size(e, doc):
    if type(e) == Div and 'small' in e.classes:
        if doc.format == 'latex':
            left = RawBlock('\\small', format='latex')
            right = RawBlock('\\normalsize', format='latex')
        else:
            return
        e.content = [left] + list(e.content) + [right]
        return e


if __name__ == "__main__":
    toJSONFilter(size)

