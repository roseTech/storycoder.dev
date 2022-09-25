#!/usr/bin/env python3

import re
import collections

POEM = '''
Money and Soul

Earn earn earn
    Our money their money your
Money

Sell sell sell
    Your soul their soul your
Soul

Spend spend spend
    Your money their money your
Money

Lie lie lie
    To you to them to
You


Have you earned your money yet?

Have you sold your soul yet?

Have you spent your money yet?

Have you lied to yourself yet?


It is never too late to not.

Is is it surrealism? Or is it realism?
'''

words = re.findall(r'\w+', POEM)
counter = collections.Counter(words)
for (word, n) in counter.most_common():
    print(word, n)
