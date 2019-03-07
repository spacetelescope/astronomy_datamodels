#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# Note: This file needs to be Python 2 / <3.6 compatible, so that the nice
# "This package only supports Python 3.x+" error prints without syntax errors etc.

import glob
import os
import sys
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

# Get some values from the setup.cfg
conf = ConfigParser()
conf.read(['setup.cfg'])
metadata = dict(conf.items('metadata'))

PACKAGENAME = metadata.get('package_name', 'asdf_astronomy_schemas')
DESCRIPTION = metadata.get('description', 'asdf astronomy schemas')
AUTHOR = metadata.get('author', 'STScI')
AUTHOR_EMAIL = metadata.get('author_email', '')
LICENSE = metadata.get('license', 'unknown')
URL = metadata.get('url', ' http://stsci.edu/schemas')
__minimum_python_version__ = metadata.get("minimum_python_version", "3.6")

# Enforce Python version check - this is the same check as in __init__.py but
# this one has to happen before importing ah_bootstrap.
if sys.version_info < tuple((int(val) for val in __minimum_python_version__.split('.'))):
    sys.stderr.write("ERROR: asdf_astronomy_schemas requires Python {} or later\n".format(__minimum_python_version__))
    sys.exit(1)

# Import ah_bootstrap after the python version validation

import ah_bootstrap
from setuptools import setup

import builtins
builtins._ASTROPY_SETUP_ = True

from astropy_helpers.setup_helpers import (register_commands, get_debug_option,
                                           get_package_info)
from astropy_helpers.git_helpers import get_git_devstr
from astropy_helpers.version_helpers import generate_version_py


# order of priority for long_description:
#   (1) set in setup.cfg,
#   (2) load LONG_DESCRIPTION.rst,
#   (3) load README.rst,
#   (4) package docstring
readme_glob = 'README*'
_cfg_long_description = metadata.get('long_description', '')
if _cfg_long_description:
    LONG_DESCRIPTION = _cfg_long_description

elif os.path.exists('LONG_DESCRIPTION.rst'):
    with open('LONG_DESCRIPTION.rst') as f:
        LONG_DESCRIPTION = f.read()

elif len(glob.glob(readme_glob)) > 0:
    with open(glob.glob(readme_glob)[0]) as f:
        LONG_DESCRIPTION = f.read()

else:
    # Get the long description from the package's docstring
    __import__(PACKAGENAME)
    package = sys.modules[PACKAGENAME]
    LONG_DESCRIPTION = package.__doc__

# Store the package name in a built-in variable so it's easy
# to get from other parts of the setup infrastructure
builtins._ASTROPY_PACKAGE_NAME_ = PACKAGENAME

# VERSION should be PEP440 compatible (http://www.python.org/dev/peps/pep-0440)
VERSION = metadata.get('version', '0.0.dev')

# Indicates if this version is a release version
RELEASE = 'dev' not in VERSION

if not RELEASE:
    VERSION += get_git_devstr(False)

# Populate the dict of setup command overrides; this should be done before
# invoking any other functionality from distutils since it can potentially
# modify distutils' behavior.
cmdclassd = register_commands(PACKAGENAME, VERSION, RELEASE)

# Freeze build information in version.py
###generate_version_py(PACKAGENAME, VERSION, RELEASE,
###                    get_debug_option(PACKAGENAME))

# Treat everything in scripts except README* as a script to be installed
### scripts = [fname for fname in glob.glob(os.path.join('scripts', '*'))
###           if not os.path.basename(fname).startswith('README')]


# Get configuration information from all of the various subpackages.
# See the docstring for setup_helpers.update_package_files for more
# details.
package_info = get_package_info()

# Add the project-global data
package_info['package_data'].setdefault(PACKAGENAME, [])
package_info['package_data'][PACKAGENAME].append('data/*')

# Define entry points for command-line scripts
entry_points = {}
entry_points['asdf_extensions'] = [
    'astronomy_datamodels = asdf_astronomy_schemas_python.datamodels.extension:AstronomyDataModelExtension',
    'astronomy_datamodels_asdf = asdf_astronomy_schemas_python.datamodels.extension:AstronomyDataModelAsdfExtension'
    ]


# Note that requires and provides should not be included in the call to
# ``setup``, since these are now deprecated. See this link for more details:
# https://groups.google.com/forum/#!topic/astropy-dev/urYO8ckB2uM

setup(name=PACKAGENAME,
      version=VERSION,
      description=DESCRIPTION,
      #scripts=scripts,
      install_requires=[s.strip() for s in metadata.get('install_requires', 'astropy').split(',')],
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      long_description=LONG_DESCRIPTION,
      cmdclass=cmdclassd,
      zip_safe=False,
      use_2to3=False,
      entry_points=entry_points,
      python_requires='>={}'.format(__minimum_python_version__),
      **package_info
)
