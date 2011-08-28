# -*- coding: utf-8 -*-

"""
envoy.core
~~~~~~~~~~

This module provides
"""

import os
import shlex
import subprocess


__version__ = '0.0.0'
__license__ = 'MIT'
__author__ = 'Kenneth Reitz'



class Response(object):
    """A command's response"""

    def __init__(self, process=None):
        super(Response, self).__init__()

        self._process = process
        self.command = None
        self.std_err = None
        self.std_out = None
        self.status_code = None
        self.history = []


    def __repr__(self):
        if len(self.command):
            return '<Response [{0}]>'.format(self.command[0])
        else:
            return '<Response>'


def run(command, data=None, timeout=None, capture=True):
    """Executes a given commmand and returns Response.

    Blocks until process is complete, or timeout is reached.
    """

    # Prepare arguments.
    if isinstance(command, basestring):
        command = command.split('|')
        command = map(shlex.split, command)

    history = []

    for c in enumerate(command):

        if capture:
            do_capture=subprocess.PIPE

        if len(history):
            data = history[-1].std_out

        p = subprocess.Popen(c,
            universal_newlines=True,
            shell=False,
            env=os.environ,
            stdin=do_capture or None,
            stdout=do_capture or None,
            stderr=do_capture or None,
        )

        out, err = p.communicate(input=data)

        r = Response(process=p)

        r.command = c
        r.std_out = out
        r.std_err = err
        r.status_code = p.returncode

        history.append(r)


    r = history.pop()
    r.history = history

    return r