#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import re
import string
import random

with io.open('words.txt','r',encoding='utf8') as f:
    text = f.read()

words = re.split('\W+', text, flags=re.UNICODE)

for i in range(0, 10):
  print i+1, random.choice(words)
