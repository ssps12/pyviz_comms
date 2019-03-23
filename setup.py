#!/usr/bin/env python

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_setup_version(reponame):
    """
    Helper to get the current version from either git describe or the
    .version file (if available).
    """
    import json
    basepath = os.path.split(__file__)[0]
    version_file_path = os.path.join(basepath, reponame, '.version')
    try:
        from param import version
    except:
        version = None
    if version is not None:
        return version.Version.setup_version(basepath, reponame, archive_commit="$Format:%h$")
    else:
        print("WARNING: param>=1.6.0 unavailable. If you are installing a package, this warning can safely be ignored. If you are creating a package or otherwise operating in a git repository, you should install param>=1.6.0.")
        return json.load(open(version_file_path, 'r'))['version_string']


extras_require = {
    'tests': ['flake8'],
    'build': ['param >=1.7.0', 'setuptools']
}

extras_require['all'] = sorted(set(sum(extras_require.values(), [])))

install_requires = ['param']
setup_args = dict(
    name='pyviz_comms',
    version=get_setup_version("pyviz_comms"),
    install_requires = install_requires,
    extras_require=extras_require,
    tests_require=extras_require['tests'],
    description='Bidirectional communication for the PyViz ecosystem.',
    long_description=open('README.md').read() if os.path.isfile('README.md') else 'Consult README.md',
    long_description_content_type="text/markdown",
    author= "PyViz developers",
    author_email= "",
    maintainer= "PyViz",
    maintainer_email= "developers@pyviz.org",
    platforms=['Windows', 'Mac OS X', 'Linux'],
    license='BSD',
    url='http://pyviz.org',
    packages = ["pyviz_comms"],
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries"]
)


if __name__=="__main__":
    setup(**setup_args)
