#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:59:47 2024

@author: alexblanco
"""
from rembg import remove
from PIL import Image

input_path = 'avatar.jpg'
output_path = 'avatar_sin_fondo.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)