#!/usr/bin/env python3

'''
main module;
'''

from jinja2 import ChainableUndefined
from jinja2 import DebugUndefined
from jinja2 import DictLoader
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import StrictUndefined
from jinja2 import Template
from jinja2 import Undefined
from os.path import basename
from os.path import dirname

import argparse
import argparse_ext
import configparser
import json
import os
import re
import sys
import xmltodict
import yaml

##  program name;
prog = 'jinja'

def _load_file_data_ini(fin):

    '''
    load data in ini format;

    $1:fin:file object
    :   data file object;
    $?::dict
    :   data;
    '''

    cp = configparser.ConfigParser()
    cp.read_file(fin)
    return { s: dict(cp.defaults(), **cp[s]) for s in cp.sections() }

def _load_file_data_json(fin):

    '''
    load data in json format;

    $1:fin:file object
    :   data file object;
    $?::dict
    :   data;
    '''

    return json.load(fin)

def _load_file_data_xml(fin):

    '''
    load data in xml format;

    $1:fin:file object
    :   data file object;
    $?::dict
    :   data;
    '''

    return xmltodict.parse(fin.read())

def _load_file_data_yaml(fin):

    '''
    load data in yaml format;

    $1:fin:file object
    :   data file object;
    $?::dict
    :   data;
    '''

    return yaml.safe_load(fin)

def _load_env_data(envs, env_regex):

    '''
    load data from env;

    $1:envs:list
    :   names of envars that define data;
    $2:env_regex:str
    :   regex matching envars that define data;
    $?::dict
    :   data;
    '''

    data = {}

    for k in os.environ:
        if ( envs and k in envs) or ( env_regex and re.match(env_regex, k) ):
            data[k] = os.environ[k]

    return data

def _load_file_data(fname, fmt):

    '''
    load data from file;

    $1:fname:str
    :   data file name;
    $2:fmt:str
    :   data file format;
    $?::dict
    :   data;
    '''

    data = {}

    if fname is not None:
        ##  get input file object;
        if fname == '-':
            fin = sys.stdin
        else:
            fin = open(fname, 'rt')

        try:
            ##  detect data file format;
            if fmt is None:
                if fname.endswith('.ini'):
                    fmt = 'ini'
                elif fname.endswith('.json'):
                    fmt = 'json'
                elif fname.endswith('.xml'):
                    fmt = 'xml'
                elif fname.endswith('.yaml'):
                    fmt = 'yaml'
                else:
                    raise Exception('no data file format;')

            ##  load data;
            if fmt == 'ini':
                data = _load_file_data_ini(fin)
            elif fmt == 'json':
                data = _load_file_data_json(fin)
            elif fmt == 'xml':
                data = _load_file_data_xml(fin)
            elif fmt == 'yaml':
                data = _load_file_data_yaml(fin)
            else:
                raise Exception('invalid data file format: {};'.format(fmt))

        finally:
            fin.close()

    return data

def _load_data(fname, fmt, defines, envs, env_regex):

    '''
    load data; precedence (low to high): envars, files, args;

    $1:fname:str
    :   data file name;
    $2:fmt:str
    :   data file format;
    $3:defines:list
    :   data defined as command line arguments;
    $4:envs:list
    :   names of envars that define data;
    $5:env_regex:str
    :   regex matching envars that define data;
    $?::dict
    :   data;
    '''

    data = {}

    ##  merge data defined as envars;
    data.update(_load_env_data(envs, env_regex))

    ##  merge data defined in file;
    data.update(_load_file_data(fname, fmt))

    ##  merge data defined as cmd args;
    if defines:
        data.update(defines)

    return data

def _undefined_type(name):

    '''
    get undefined type from its name;

    $1:name:str
    :   undefined type name: '', 'chainable', 'debug', 'strict';
    $?::type
    :   undefined type;
    '''

    try:
        return {
            '':             Undefined,
            'chainable':    ChainableUndefined,
            'debug':        DebugUndefined,
            'strict':       StrictUndefined,
        }[name]
    except KeyError:
        raise Exception('unknown undefined type: {}'.format(name))

def _parse_args():

    '''
    parse command line arguments;
    '''

    ##  init arg parser;
    parser = argparse.ArgumentParser(
        prog=prog,
        description='a command line interface to jinja;',
        formatter_class=argparse_ext.HelpFormatter,
        add_help=False,
    )

    ##  add arg;
    parser.add_argument(
        '-h', '--help',
        action='help',
        help='display help message;',
    )

    ##  add arg;
    parser.add_argument(
        '-D', '--define',
        action='append',
        nargs=2,
        type=str,
        metavar=('key', 'value'),
        help='define data with key-value pairs;',
    )

    ##  add arg;
    parser.add_argument(
        '-E', '--env',
        action='append',
        type=str,
        metavar='key',
        help='define data with envars;',
    )

    ##  add arg;
    parser.add_argument(
        '-X', '--env-regex',
        type=str,
        metavar='regex',
        help='define data with envars matching regex;',
    )

    ##  add arg;
    parser.add_argument(
        '-d', '--data',
        type=str,
        metavar='file',
        help='data file;',
    )

    ##  add arg;
    parser.add_argument(
        '-f', '--format',
        type=str,
        metavar='format',
        help='data file format;',
    )

    ##  add arg;
    parser.add_argument(
        '-o', '--output',
        type=str,
        metavar='file',
        help='output file;',
    )

    ##  add arg;
    parser.add_argument(
        '-u', '--undefined',
        type=str,
        metavar='type',
        help='undefined type;',
        choices=['', 'chainable', 'debug', 'strict'],
        default='',
    )

    ##  add arg;
    parser.add_argument(
        'template',
        nargs='?',
        type=str,
        metavar='template',
        help='template file;',
    )

    ##  parse args;
    args = parser.parse_args()

    return args

def main():

    '''
    main function;
    '''

    ##  parse args;
    args = _parse_args()

    ##  load template;
    if args.template is None or args.template == '-':
        env = Environment(
            loader=DictLoader({ '-': sys.stdin.read() }),
            keep_trailing_newline=True,
            undefined=_undefined_type(args.undefined),
        )
        template = env.get_template('-')
    else:
        env = Environment(
            loader=FileSystemLoader(dirname(args.template)),
            keep_trailing_newline=True,
            undefined=_undefined_type(args.undefined),
        )
        template = env.get_template(basename(args.template))

    ##  load data;
    data = _load_data(
        args.data, args.format, args.define, args.env, args.env_regex,
    )

    ##  render template with data;
    rendered = template.render(data)

    ##  write to output;
    if args.output is None or args.output == '-':
        fout = sys.stdout
    else:
        fout = open(args.output, 'wt')
    try:
        fout.write(rendered)
    finally:
        fout.close()

if __name__ == '__main__':
    main()

