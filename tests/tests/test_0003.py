#!/usr/bin/env python3

from os.path import join
from pytest import raises

from tests import get_input_dir
from tests import get_test_name
from tests import read_bytes
from tests import run_proc

test_name = get_test_name(__file__)

def test(session):

    '''
    test load data from env;
    '''

    data_file = join(get_input_dir(test_name), 'a.json')
    tmpl_file = join(get_input_dir(test_name), 'a.j2')

    import os
    os.environ['FOOD'] = 'grass'

    text_file = join(get_input_dir(test_name), 'a.txt')
    text_data = read_bytes(text_file)

    args = [ 'jinja', '-E', 'FOOD', tmpl_file ]
    cp = run_proc(args, env=os.environ)
    assert cp.stdout == text_data

    args = [ 'jinja', '-X', '.*', tmpl_file ]
    cp = run_proc(args, env=os.environ)
    assert cp.stdout == text_data

