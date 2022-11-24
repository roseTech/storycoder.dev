#!/bin/bash

number_lilies=1
days_between_full_moon=29

for x in `seq 2 $days_between_full_moon`; do
  number_lilies=$((number_lilies*2))
done

echo $number_lilies
