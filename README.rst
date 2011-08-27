Envoy:
=======

You probally don't need this. I do.


Usage
-----

::

    >>> r = envoy.command('git config', data='data to pipe in')
    >>> r.status_code
    129
    >>> r.std_out
    'usage: git config [options]'
    >>> r.std_err
    ''
