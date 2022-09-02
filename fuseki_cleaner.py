#!/usr/bin/env python3
# script developed with help from https://stackoverflow.com/questions/79968/split-a-string-by-spaces-preserving-quoted-substrings-in-python

import shlex

with open("data.ttl", "r") as file:
    data = file.read()

new_data = ""
for line in data.split("\n"):
    split_line = shlex.split(line, posix=False)
    if len(split_line) > 0:
        new_line = "".join(
            [split_line.pop(0), " ", split_line.pop(0), " ", split_line.pop(0), " ."]
        )
        new_data = new_data + new_line + "\n"

with open("new_data.ttl", "w") as new_file:
    new_file.write(new_data)
