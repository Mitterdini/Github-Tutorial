from sys import path
path.insert(0, '/root/Coding/Python/Github/Learning-The-Hard-Way/Projects/ex47/')
from scripts import test_lex
from nose.tools import *

def test_directions():
    assert_equal(test_lex.scan('north'), [('direction', 'north')])
    result = test_lex.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(test_lex.scan('go'), [('verb', 'go')])
    result = test_lex.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(test_lex.scan('the'), [('stop', 'the')])
    result = test_lex.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(test_lex.scan('bear'), [('noun', 'bear')])
    result = test_lex.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(test_lex.scan('1234'), [('number', 1234)])
    result = test_lex.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(test_lex.scan('ASDFASDFASDF'), [('error', 'ASDFASDFASDF')])
    result = test_lex.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
