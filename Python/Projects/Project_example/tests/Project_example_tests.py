from nose.tools import *
import Project_example

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')
