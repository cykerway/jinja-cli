# jinja-cli

a command line interface to [jinja][jinja];

this program renders a jinja template using input data; data may be read from a
file, environment variables, or command line arguments; either template or data
file may be read from stdin; output file may be written to stdout;

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

to read data from command line arguments:

    # jinja -D {key} {value} [ -D {key} {value} ... ] {template}

to read data from environment variables:

    # jinja -E {key} [ -E {key} ... ] {template}

to read data from environment variables using regex:

    # jinja -X {regex} {template}

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

## data priority

data priority from low to high:

-   environment variables: `-E, --env`, `-X, --env-regex`;

-   data file: `-d, --data`;

-   command line arguments: `-D, --define`;

## license

Copyright (C) 2018-2021 Cyker Way

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

