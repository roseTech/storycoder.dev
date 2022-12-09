#!/bin/bash

POEM="Money and Soul

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

Is is it surrealism? Or is it realism?"

echo $POEM | sed -e 's/ /\n/g' | sort | uniq -c | sort -r | awk '$1 > 1'
