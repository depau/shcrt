#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import errno
import re

from typing import List

item_regex = re.compile(r'.*(?P<type>\w):"(?P<key>.+?)"=(?P<value>.*)$', re.DOTALL)

def parse_ini(path: str) -> dict:
    values = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("\ufeff"):
                line = line[1:]
            if len(line) > 2 and (line[1] == ":" or line[2] == ":"):
                values.append(line)
            elif line == "":
                continue
            else:
                values[-1] += "\n" + line

    matches = []
    for i in values:
        try:
            match = item_regex.match(i)
            matches.append(match.groupdict())
        except Exception:
            pass

    result = {}
    for match in matches:
        t = match["type"]
        k = match["key"]
        v = match["value"]

        if t == "S":
            result[k] = v
        if t == "D":
            result[k] = int(v, 16)
        # We don't care about the other types

    return result


def gen_cmdlines_ssh(ini: dict, cfgdir: str) -> List[str]:
    hostname = ini["Hostname"]
    port = ini.get("[SSH2] Port", 22)
    username = ini["Username"]
    keyfile = ini.get("Identity Filename V2", None)
    if keyfile:
        keyfile = os.path.normpath(
                keyfile \
                    .replace('\\', '/') \
                    .replace('${VDS_CONFIG_PATH}', cfgdir)
            ) \
            .replace('"', '\\"')

    cmdline = []
    if keyfile:
        cmdline += ["-i", f'"{keyfile}"']
    if port != 22:
        cmdline += ["-p", str(port)]

    cmdline.append(f"{username}@{hostname}")

    ssh = ["ssh"] + cmdline
    scp = ["scp"] + cmdline

    return [' '.join(ssh), ' '.join(scp)]


def gen_cmdlines(ini: dict, cfgdir: str) -> List[str]:
    if ini["Protocol Name"].startswith("SSH"):
        return gen_cmdlines_ssh(ini, cfgdir)
    return []


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} path/to/Config path/to/session.ini", file=sys.stderr)
        sys.exit(1)

    cfg = sys.argv[1]
    ini = sys.argv[2]

    if not os.path.exists(ini):
        raise OSError(f"Session file does not exist: '{ini}'", errno=errno.ENOENT)

    if not os.path.isfile(ini):
        raise OSError(f"Not a file: '{ini}'", errno=errno.ENFILE)

    inidict = parse_ini(ini)
    cmdlines = gen_cmdlines(inidict, cfg)
    print('\n'.join(cmdlines))
