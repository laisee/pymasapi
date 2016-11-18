#! /bin/bash 

# erase previous coverage data
coverage erase

# run coverage generation for nose tests
coverage run --source=/Users/laisee/src/pymasapi /usr/local/bin/nosetests -c ../test/nose.cfg -vv test/

# run coverage html file generation
coverage html -d `pwd`\..\test
