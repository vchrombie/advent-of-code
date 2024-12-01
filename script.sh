#!/bin/bash

mkdir day-0$1
cd day-0$1
touch sample.txt
touch input.txt
cp ../day.py .
sed -i '' '1,2d' day.py
mv day.py day-0$1.py
echo "ready for day-0$1"
