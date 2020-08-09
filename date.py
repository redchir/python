#!/usr/bin/env python
# -*- coding: utf-8  -*-

from datetime import date

today = date.today()
d = today.strftime("%A, %d %B %Y")

print(d)
