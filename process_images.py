#!/usr/bin/python3
import os
from subprocess import check_call

dir = 'original_images'

for file in os.listdir('original_images'):
    if file.startswith('.'):
        continue
    path = os.path.join(dir, file)
    dest = 'static/img/proj/{}-' + file
    for width in [150, 300, 600, 900, 1200, 1800, 2400]:
        print('making ', dest.format(width))
        check_call(['convert', path, '-resize', str(width), '-strip', '-quality', '90', dest.format(width)])

