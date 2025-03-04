#!/usr/bin/env python
import math
import sys

from xml.dom.minidom import parse, Element
import xml.etree.ElementTree as ElementTree


TOLERANCES = (
    .1,
    .2,
    .3,
    .4,
    .5,
    .6,
    .7,
    .8,
    .9,
)
HALF_SIZE_TAGS = (
    'MajorDia',
    'MinorDia',
    'TapDrill',
)
SIZE_TAGS = (
    'PitchDia',
)


def attr(node, attr_name):
    return node.find('./%s' % attr_name).text


input_file = sys.stdin
if len(sys.argv) > 1:
    input_file = open(sys.argv[1])

tree = ElementTree.parse(input_file)
root = tree.getroot()

angle = math.radians(90 - float(attr(root, 'Angle')))

for thread_size in root.iterfind('ThreadSize'):
    designation = thread_size.find('./Designation')
    for thread in designation.findall('./Thread'):
        sign = 1 if attr(thread, 'Gender') == 'internal' else -1

        width = (float(attr(thread, 'MajorDia')) -
                 float(attr(thread, 'MinorDia')))

        for tol in TOLERANCES:
            dx = tol / math.sin(angle)

            if dx >= width:
                continue

            new_thread = ElementTree.SubElement(designation, 'Thread')
            for el in thread.iterfind('./*'):
                new_el = ElementTree.SubElement(new_thread, el.tag)
                if el.tag == 'Class':
                    new_el.text = '%s ±%.1fmm' % (el.text, tol)
                elif el.tag in SIZE_TAGS:
                    new_el.text = '%.4f' % (float(el.text) + (dx * sign))
                elif el.tag in HALF_SIZE_TAGS:
                    new_el.text = '%.4f' % (float(el.text) + (tol * sign))
                else:
                    new_el.text = el.text

ElementTree.indent(root)

# Encoding fails if we try to write to a file opened in text mode, so we need
# to allow the serializer to reopen stdout in binary mode by passing
# `sys.stdout.fileno()`, rather than passing the descriptor directly.
tree.write(sys.stdout.fileno(), encoding='utf-8', xml_declaration=True)
