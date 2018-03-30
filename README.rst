Funda quick search component test with python selenium
==========================================

Installation
------------
Installation run shell script. The script will then take care of installing `virtualenv <https://virtualenv.pypa.io/en/latest/>`_, creating the virtualenv and installing all necessary dependencies.
For preparation of the system follow next steps::

In case of linux 32 bit system::
    ~$ sudo /bin/cp geckodriver_linux_32bit /usr/local/bin

In case of linux 64 bit system::
    ~$ sudo /bin/cp geckodriver_linux_64bit /usr/local/bin

In any other case see: https://github.com/mozilla/geckodriver/releases for the geckodriver for you system and copy that one to /usr/local/bin

Install if you want to use chromium: the chromium-chromedriver::

    ~$ sudo apt-get install chromium-chromedriver

To bootstrap the test environment execute::
    ~$ ./setup_virtualenv.sh

Running tests
-------------
To run the tests execute the following::

    ~$ source test_venv/bin/activate

This will switch to the virtualenv just created by ``setup_virtualenv.sh``.

To run all the tests simply execute::

    ~$ py.test -svl tests/

To run tests in a particular directory or module, provide the path to this directory or file::

    ~$ py.test -svl tests/fundaSearch.py

Commandline options
-------------------
py.test and py.test plugins come with several useful command line options.
Here is a short list of some most helpful options:

* ``-s``
    disallows py.test to capture standard streams (without this options you will not see any prints in your tests)

* ``-v``
    makes output more verbose

* ``-l``
    print locals in traceback, could be useful for debugging

* ``-k``
    allows to select tests by ``keyword`` argument
