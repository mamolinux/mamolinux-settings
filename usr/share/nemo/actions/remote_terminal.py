#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

terminal="x-terminal-emulator"

_path = sys.argv[1]
# print(_path)
_user = os.environ['USER']
# print(_user)

if '/sftp:' in _path:
    # print("remote")
    sftp = _path.split('/sftp:', 1)[1]
    settings = {}
    settings['user'] = _user
    options, sep, settings['path'] = sftp.partition('/')
    for opt in options.split(','):
        name, sep, value = opt.partition('=')
        settings[name] = value
    
    cmd = [terminal, '-e',
        'ssh %(user)s@%(host)s -t "cd /%(path)s; $SHELL"' % settings]
    subprocess.call(cmd)
    # print(cmd)
else:
    sys.exit(1)
    