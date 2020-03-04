#!/bin/bash

AFL_SKIP_CPUFREQ=1 AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1 \
    py-afl-fuzz -o results -i examples -- $(which python) sut.py

tree examples
cat examples/*
tree results
python -c "import sys; result = open(sys.argv[1], 'rb').read(); print([result, len(result)])" results/crashes/id*
