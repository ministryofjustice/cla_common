#!/usr/bin/env bash
virtualenv venv
venv/bin/pip install -r requirements-test.txt
venv/bin/coverage run --source cla_common runtests.py