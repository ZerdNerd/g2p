#from distutils.core import setup
from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'g2p_pl',
  packages = ['g2p_pl'], # this must be the same as the name above
  version = '2.0.0',
  description = 'A Simple Python Module for English Grapheme To Phoneme Conversion - or Polish, dunno.',
  long_description=long_description,
  author = 'ZerdNerd & Kyubyong Park & Jongseok Kim',
  author_email = 'kbpark.linguist@gmail.com',
  url = 'https://github.com/ZerdNerd/g2p_pl', # use the URL to the github repo
  download_url = 'https://github.com/Kyubyong/g2p/archive/1.0.0.tar.gz', # I'll explain this in a second
  keywords = ['g2p','g2p_pl'], # arbitrary keywords
  classifiers = [],
  install_requires = [
    'numpy>=1.13.1',
    'nltk>=3.2.4',
    'inflect>=0.3.1',
    'distance>=0.1.3',
  ],
  license='Apache Software License',
  include_package_data=True
)

