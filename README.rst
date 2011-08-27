Envoy: Simplified Subprocesses
===============================

You probally don't need this. I do.

**Note:** Work in progress.

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
