import setuptools
from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'squeezectl',
  py_modules=['squeezectl'],
  version = '0.0.1',
  license='Apache',
  description = 'Control Logitech Media Server and Squeezebox from command line',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Bastian Bowe',
  author_email = 'bastian.dev@gmail.com',
  url = 'https://github.com/baztian/squeezectl',
  keywords = ['lms', 'squeeze'],
  install_requires = [
          # necessary unless a version newer than 1.1.0 of lms is available on pypi
          'lms @ https://github.com/baztian/lms/archive/develop.zip'
      ],
  entry_points = {
      'console_scripts': [
        'squeezectl = squeezectl:main',
      ],
  },
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Multimedia :: Sound/Audio',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)