__doc__ = """
    ...Global
"""

from .TF_IDF import *
from .MorfAnaliz import *
from .Bigram import *
from .summa import *

try:
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    with open(version_file, 'r') as infile:
        __version__ = infile.read().strip()
except NameError:
    __version__ = 'unknown (running code interactively?)'
except IOError as ex:
    __version__ = "unknown (%s)" % ex
if __doc__ is not None:
    __doc__ += '\n    @version: ' + __version__

__copyright__ = """\
    KazNU (c) FIT 2019 Project
"""

__license__ = "KazNU License, Version 1.0"
# Description of the toolkit, keywords, and the project's primary URL.
__longdescr__ = """\
    Using Python version 2.3-3.7.2
"""
__keywords__ = [
    'tf_idf',
    '...'
]
__url__ = "http://kaznu.kz/"

# Maintainer, contributors, etc.
__maintainer__ = "Tukesev Ualsher Anuarbekovich"
__maintainer_email__ = "info@kaznu.kz"
__author__ = __maintainer__
__author_email__ = __maintainer_email__

# "Trove" classifiers for Python Package Index.
__classifiers__ = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: General',
    'Topic :: Text Processing :: Indexing',
    'Topic :: Text Processing :: Linguistic',
]