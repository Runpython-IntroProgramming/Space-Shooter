#!/bin/bash
set -e # exit with nonzero exit code if anything fails

# create the tests folder
mkdir tests
cd tests
git init
git pull https://${GH_REPO}
cd ..

# hope we hit three distinct cases in random testing!
python tests/test.py ${TESTMODULE}
