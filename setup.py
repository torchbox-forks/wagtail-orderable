import os
import sys
import subprocess

from wagtailorderable import __version__
from setuptools import setup, find_packages
from setuptools.command.install import install

INSTALL_REQUIRES = [
    "wagtail>=6.3",
    "wagtail-modeladmin>=2.2.0",
]

DEVELOPMENT_REQUIRES = [
    "black",
    "isort",
    "flake8",
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    "Framework :: Django",
    "Framework :: Django :: 4.2",
    "Framework :: Django :: 5.1",
    "Framework :: Django :: 5.2",
    'License :: OSI Approved :: zlib/libpng License',
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Framework :: Wagtail",
    "Framework :: Wagtail :: 6",
    "Framework :: Wagtail :: 7",

]

class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != __version__:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, __version__
            )
            sys.exit(info)

setup(
    name='wagtail-orderable',
    version=__version__,
    description='Orderable support for Wagtail',
    long_description="Provides drag-and-drop support ordering support to the ModelAdmin listing view.",
    author='Elton Lee & Andy Babic',
    author_email='elton2048@gmail.com',
    url='https://github.com/elton2048/wagtail-orderable',
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'dev': DEVELOPMENT_REQUIRES,
    },
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=CLASSIFIERS,
    cmdclass={
        'verify': VerifyVersionCommand,
    },
)
