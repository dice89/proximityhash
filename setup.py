from distutils.core import setup
import setuptools

setup(
  name = 'proximitypyhash',
  py_modules = ['proximitypyhash'],
  version = '0.2',
  description = 'Pygeohash for proximity queries',
  long_description=open('README.rst').read(),
  author = 'Ashwin Nair/Alexander Mueller',
  author_email = 'alexander.mueller@gmail.com',
  license = "MIT",
  url = 'https://github.com/dice89/proximityhash',
  download_url = 'https://github.com/dice89/proximityhash/archive/0.2.tar.gz',
  keywords = ['geohash', 'optimizer', 'compression', 'geo', 'latitude', 'longitude', 'coordinates', 'proximity', 'circle'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
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
  entry_points={
    'console_scripts': [
      'proximitypyhash=proximitypyhash:main'
    ]
  },
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4'
)
