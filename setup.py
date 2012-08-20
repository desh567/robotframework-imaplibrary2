#!/usr/bin/env python

from os.path import join, dirname

execfile(join(dirname(__file__), 'src', 'ImapLibrary', 'version.py'))

from distutils.core import setup

CLASSIFIERS = """
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

long_description=open(join(dirname(__file__), 'README.rst',)).read()

setup(
  name             = 'robotframework-imaplibrary',
  version          = VERSION,
  description      = 'Robot Framework IMAP Mail Check Library',
  long_description = long_description,
  author           = 'Lovely Systems GmbH',
  author_email     = 'office@lovelysystems.com',
  url              = 'https://github.com/lovelysystems/robotframework-imaplibrary',
  license          = 'EPL',
  keywords         = 'robotframework testing testautomation imap mail calabash',
  platforms        = 'any',
  zip_safe         = False,
  classifiers      = CLASSIFIERS.splitlines(),
  package_dir      = {'' : 'src'},
  install_requires = ['robotframework', 'requests'],
  packages         = ['ImapLibrary'],
)