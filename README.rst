Envoy: Simplified Subprocesses for Python
==========================================

**Note:** Work in progress.

This is a convenience wrapper around the `subprocess` module.

You likely don't need this.

.. image:: http://cl.ly/2n1F3z0d3U2T0Z2E051E/Screen_Shot_2011-08-27_at_3.34.16_PM.png


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