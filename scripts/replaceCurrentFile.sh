#!/bin/bash

# Get the current year
YEAR=$(date +%Y)

# Get the current month
MONTH=$(date +%m)

# Check the semester
if [ "$MONTH" -ge 2 ] && [ "$MONTH" -le 7 ]; then
    SEMESTER="s"
else
    SEMESTER="f"
fi

# get the previous semester
if [ "$SEMESTER" == "s" ]; then
    PREV_SEMESTER="f"
else
    PREV_SEMESTER="s"
fi

# get the previous year
if [ "$SEMESTER" == "s" ]; then
    PREV_YEAR=$((YEAR - 1))
else
    PREV_YEAR=$YEAR
fi

# ignore if there is already a previous file
if [ -f result-"$PREV_YEAR$PREV_SEMESTER".json ]; then
    echo "File already exists"
else
    mv result.json result-"$PREV_YEAR$PREV_SEMESTER".json
fi

sleep 1
mv output.json result.json
