#!/bin/bash

# Get the current year
YEAR=$(date +%Y)

# Get the current month
MONTH=$(date +%m)

# Calculate the semester
if [ "$MONTH" -ge 2 ] && [ "$MONTH" -le 7 ]; then
    SEMESTER="s"
else
    SEMESTER="f"
fi

cp output.json result.json
cp output.json result-"$YEAR"$SEMESTER.json

git add result.json
git add result-"$YEAR"$SEMESTER.json
