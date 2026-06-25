#!/bin/bash
set -e

pytest /tests/test_outputs.py \
    --json-ctrf /tests/ctrf.json \
    -rA