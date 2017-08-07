from distutils.core import setup
import setuptools

setup(
  name = 'proximitypyhash',
  py_modules = ['proximitypyhash'],
  version = '0.1',
  description = 'Pygeohash for proximity queries',
  long_description = open('README.rst').read(),
  author = 'Ashwin Nair/Alexander Mueller',
  author_email = 'alexander.mueller@gmail.com',
  license = "MIT",
  url = 'https://github.com/ashwin711/proximityhash',
  download_url = 'https://github.com/dice89/proximityhash/tarball/0.1',
  keywords = ['geohash', 'optimizer', 'compression', 'geo', 'latitude', 'longitude', 'coordinates', 'proximity', 'circle'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  setup_requires=['pytest-runner'],
  tests_require=[
            'pytest',
        ],
  install_requires = [
	'clint',
	'argparse',
    'georaptor>=2.0.3',
    'pygeohash==1.2.0'
  ],
  entry_points='''
	[console_scripts]
	proximityhash=proximityhash:main
  '''
)
