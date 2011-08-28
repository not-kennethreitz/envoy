Envoy: Simplified Subprocesses for Python
==========================================

**Note:** Work in progress.

This is a convenience wrapper around the `subprocess` module.

You don't need this.

.. image:: https://github.com/kennethreitz/envoy/raw/master/ext/in_action.png

But you want it.


Usage
-----

::

    >>> r = envoy.run('git config', data='data to pipe in', timeout=2)

    >>> r.status_code
    129
    >>> r.std_out
    'usage: git config [options]'
    >>> r.std_err
    ''

Soon, you'll be able to pass in pipe strings too ::

    >>> r = envoy.run('uptime | pbcopy')

    >>> r.command
    'pbcopy'
    >>> r.status_code
    0

    >>> r.history
    [<Response 'uptime'>]