# jinja-cli

a command line interface to [jinja][jinja];

this program renders a jinja template with given data; data may be read from a
file, or defined as command line arguments; either template or data file may be
stdin; output file may be stdout;

supported data formats: ini, json, xml, yaml;

## install

    pip install jinja-cli

## usage

to render a jinja template with data in json format:

    # jinja -d {data} {template}

to use a different data format:

    # jinja -d {data} -f {data_format} {template}

to read template from stdin:

    # jinja -d {data} < {template}

to read data from stdin:

    # jinja -d - {template} < {data}

to output to a file:

    # jinja -d {data} -o {output} {template}

## example

template file `example.j2`:

    sheep eat {{ sheep.eat }};

data file `example.json`:

    {
        "sheep": {
            "eat": "grass"
        }
    }

any of these commands:

    # jinja -d example.json example.j2
    # jinja -d example.json < example.j2
    # jinja -d - -f json example.j2 < example.json

output:

    sheep eat grass;

## license

Copyright (C) 2018 Cyker Way

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

[jinja]: http://jinja.pocoo.org/

