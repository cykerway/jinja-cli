#!/usr/bin/env python3

from os.path import dirname
from pkg_resources import resource_filename
from pytest import fixture

from tests import test_ctx

@fixture(scope='session')
def prog_dir():

    '''
    top-level package dir;
    '''

    yield resource_filename('jinja_cli', '')

@fixture(scope='session')
def test_dir():

    '''
    top-level test dir;
    '''

    yield dirname(dirname(__file__))

@fixture(scope='session')
def session(prog_dir, test_dir):

    '''
    fixture:session: session;
    '''

    test_ctx.prog_dir = prog_dir
    test_ctx.test_dir = test_dir

