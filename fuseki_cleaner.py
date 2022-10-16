#!/usr/bin/env python3
# script developed with help from https://stackoverflow.com/questions/79968/split-a-string-by-spaces-preserving-quoted-substrings-in-python

import argparse
import sys
import shlex

parser = argparse.ArgumentParser(description="Convert quadruples to triples.")
parser.add_argument(
    "-i", "--input", type=str, nargs=1, help="Filename of TTL to be cleaned"
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    nargs="?",
    default="new_data.ttl",
    help="Filename of output TTL",
)

parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true"
)

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

if args.verbose:
    print(args)

with open(args.input[0], "r") as file:
    data = file.read()

new_data = ""
for line in data.split("\n"):
    split_line = shlex.split(line, posix=False)
    if len(split_line) > 0:
        new_line = "".join(
            [split_line.pop(0), " ", split_line.pop(0), " ", split_line.pop(0), " ."]
        )
        new_data = new_data + new_line + "\n"

with open(args.output, "w") as new_file:
    new_file.write(new_data)
