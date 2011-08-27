# -*- coding: utf-8 -*-

"""
envoy.core
~~~~~~~~~~

This module provides
"""

import os
import shlex
import subprocess
import sys

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


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
        command = shlex.split(command)

    if capture:
        do_capture=subprocess.PIPE


    p = subprocess.Popen(command,
        universal_newlines=True,
        shell=False,
        env=os.environ,
        stdin=do_capture or None,
        stdout=do_capture or None,
        stderr=do_capture or None,
    )

    out, err = p.communicate(input=data)

    r = Response(process=p)

    r.command = command
    r.std_out = out
    r.std_err = err
    r.status_code = p.returncode

    return r