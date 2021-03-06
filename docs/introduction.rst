############
Introduction
############


Compatibility
*************

Python
======

3.4 and 3.5 are supported. 2.7 and 3.3 should work too but not all features are
supported and those versions might not be as stable.

Django
======

1.7, 1.8, 1.9 and 1.10 are supported.


Installation
************

After installing better-test into your virtualenv, add ``better_test`` to your
``INSTALLED_APPS``.


Usage
*****

You can invoke better-test like you would your standard Django test command
using ``python manage.py test``. You may pass a list of tests, test modules or
test classes to run, just like with your normal Django test command.


.. _parallel:

``--parallel``
==============

The ``--parallel`` flag will run your tests distributed across your CPU cores.
For large test suites on a computer with several CPU cores, this can
significantly speed up your test run.

This flag cannot be used together with ``--isolate``.


.. _isolate:

``--isolate``
=============

This flag will run each test in it's own process (distributed across your CPU
cores). This will result in a very long test run, but is useful to find tests
that leak state or depend on leaked state. Almost always when tests fail with
``--parallel`` but pass without it, leaking tests are the reason.

This flag cannot be used together with ``--parallel``.


.. _failed:

``--failed``
============

Re-runs all the tests that failed or errored in the last test run.


.. _retest:

``--retest``
============

Re-runs the tests using the same configuration used in the last run.


.. _migrate:

``--migrate``
=============

Run migrations before your tests.


.. _list-slow:

``--list-slow=<number>``
========================

After the test run, list the ``<number>`` slowest tests.


.. _vanilla:

``--vanilla``
=============

Bypass better-test and use the standard Django test command. You cannot use any
of the arguments mentioned above if you use ``--vanilla``.

.. _start_method:

``--start-method``
==================

.. versionadded:: 0.10

Start method to use for multiprocessing. Defaults to ``spawn``. Available
choices: ``spawn``, ``fork``, ``forkserver``. Refer to the Python documentation
for the differences.
