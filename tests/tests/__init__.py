#!/usr/bin/env python3

from os.path import basename
from os.path import join
from os.path import splitext
from types import SimpleNamespace as SN
import subprocess

##  session-wide test context;
test_ctx = SN()

def get_test_name(test_file):

    '''
    get test name from test file name;

    $1:test_file:str
    :   test file name;
    $?::str
    :   test name;
    '''

    return splitext(basename(test_file))[0]

def get_input_dir(test_name):

    '''
    get input dir of a test;

    $1:test_name:str
    :   test name;
    $?::str
    :   input dir;
    '''

    return join(test_ctx.test_dir, 'ins', test_name)

def get_output_dir(test_name):

    '''
    get output dir of a test;

    $1:test_name:str
    :   test name;
    $?::str
    :   output dir;
    '''

    return join(test_ctx.test_dir, 'outs', test_name)

def read_bytes(fname):

    '''
    read bytes from a file;

    $1:fname:str
    :   file name;
    $2:mode:str
    :   read mode;
    $?::bytes
    :   file content;
    '''

    with open(fname, 'rb') as fin:
        return fin.read()

def run_proc(args):

    '''
    run a process and capture its output;

    $1:args:list
    :   args;
    $?::CompletedProcess
    :   completed process;
    '''

    return subprocess.run(args, capture_output=True, check=True)

