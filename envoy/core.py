# -*- coding: utf-8 -*-

"""
envoy.core
~~~~~~~~~~

This module provides
"""

import subprocess
import shlex


__version__ = '0.0.0'


class Response(object):
    """A command's response"""

    def __init__(self):
        super(Response, self).__init__()
        self.command = None

    def __repr__(self):
        return '<Respones [{0}]>'.format(self.command)

    @property
    def status_code(self):
        return 0

    @property
    def std_out(self):
        return ''

    @property
    def std_err(self):
        return ''


def run(command, data=None, timeout=None):
    """Executes a given commmand and returns Response.

    Blocks until process is complete, or timeout is reached.
    """

    return Response()