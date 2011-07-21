import os
from setuptools import setup, find_packages

from clippy import VERSION

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
requirements = []

setup(
    name = "django-clippy",
    version = ".".join(map(str, VERSION)),
    description = "A template tag for a 'copy to clipboard' button, based on GitHub's Clippy.",
    long_description = read('README.rst'),
    url = '',
    license = 'MIT',
    author = 'Flavio Curella',
    author_email = 'flavio.curella@curella.org',
    packages = find_packages(exclude=['tests']),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires = requirements,
    tests_require = ["nose",],
    test_suite = "nose.collector",
)
