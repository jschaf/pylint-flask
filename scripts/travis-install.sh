#!/bin/bash
pip install coverage coveralls
pip install -r dev-requirements.txt
pip install git+https://github.com/landscapeio/pylint-plugin-utils.git@develop
pip install --editable .
