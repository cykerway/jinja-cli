# jinja-cli

a command line interface to [jinja][jinja];

this program renders a jinja template with given data; data may be read from a
file, or defined as command line arguments; either template or data file may be
stdin; output file may be stdout;

supported data formats: ini, json, xml, yaml;

## install

    pip install jinja-cli

## usage

    usage: jinja [options] [template]

    a command line interface to jinja;

    positional arguments:
        [template]                 template file;

    optional arguments:
        -h|--help                  display help message;
        -D|--define {key} {value}  define data;
        -d|--data {file}           data file;
        -f|--format {format}       data format;
        -o|--output {file}         output file;

### usage example

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

[jinja]: http://jinja.pocoo.org/

