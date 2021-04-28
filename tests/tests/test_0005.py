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
    test load data in various formats;
    '''

    tmpl_file = join(get_input_dir(test_name), 'a.j2')
    text_file = join(get_input_dir(test_name), 'a.txt')
    text_data = read_bytes(text_file)

    data_file = join(get_input_dir(test_name), 'a.json')
    args = [ 'jinja', '-d', data_file, tmpl_file ]
    cp = run_proc(args)
    assert cp.stdout == text_data

    data_file = join(get_input_dir(test_name), 'a.json')
    args = [ 'jinja', '-d', data_file, '-f', 'json', tmpl_file ]
    cp = run_proc(args)
    assert cp.stdout == text_data

    data_file = join(get_input_dir(test_name), 'a.ini')
    args = [ 'jinja', '-d', data_file, '-f', 'ini', tmpl_file ]
    cp = run_proc(args)
    assert cp.stdout == text_data

    data_file = join(get_input_dir(test_name), 'a.xml')
    args = [ 'jinja', '-d', data_file, '-f', 'xml', tmpl_file ]
    cp = run_proc(args)
    assert cp.stdout == text_data

    data_file = join(get_input_dir(test_name), 'a.yaml')
    args = [ 'jinja', '-d', data_file, '-f', 'yaml', tmpl_file ]
    cp = run_proc(args)
    assert cp.stdout == text_data

