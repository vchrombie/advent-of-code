#!/bin/bash

# Usage ./script.sh <day>
# Example:
# ./script.sh 01
# ./script.sh 31

mkdir day-$1
cd day-$1
touch sample.txt
touch input.txt
cp ../day.py .
sed -i '' '1,2d' day.py
mv day.py day-$1.py
touch README.md
cat <<EOL > README.md
# Day-$1

> https://adventofcode.com/2024/day/$1

---

## Answers

- Part 1: 
- Part 2: 

## Notes
EOL
echo "ready for day-$1"
