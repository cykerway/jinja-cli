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
    test load data precedence is env, file, args;
    '''

    data_file = join(get_input_dir(test_name), 'a.json')
    tmpl_file = join(get_input_dir(test_name), 'a.j2')

    import os
    os.environ['FOOD'] = 'env'

    text_file = join(get_input_dir(test_name), 'env.txt')
    text_data = read_bytes(text_file)
    args = [
        'jinja', '-E', 'FOOD', tmpl_file,
    ]
    cp = run_proc(args)
    assert cp.stdout == text_data

    text_file = join(get_input_dir(test_name), 'file.txt')
    text_data = read_bytes(text_file)
    args = [
        'jinja', '-E', 'FOOD', '-d', data_file, tmpl_file,
    ]
    cp = run_proc(args)
    assert cp.stdout == text_data

    text_file = join(get_input_dir(test_name), 'args.txt')
    text_data = read_bytes(text_file)
    args = [
        'jinja', '-E', 'FOOD', '-d', data_file, '-D', 'FOOD', 'args', tmpl_file,
    ]
    cp = run_proc(args)
    assert cp.stdout == text_data

