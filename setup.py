import codecs
import os

from setuptools import setup, find_packages, Command
from django_stuff import __version__

version = __version__

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get changelog
with codecs.open(os.path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    changelog = f.read()

with codecs.open(os.path.join(here, 'requirements.txt')) as f:
    install_requires = [line for line in f.readlines() if not line.startswith('#')]


class VersionCommand(Command):
    description = 'print library version'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


setup(
    author='Rafael Henter',
    author_email='rafael@henter.com.br',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],
    cmdclass={'version': VersionCommand},
    description='Library with common code for Django',
    install_requires=install_requires,
    keywords='utils tools django',
    license='MIT',
    long_description=long_description,
    name='django-stuff',
    packages=find_packages(exclude=['docs', 'tests*']),
    url='https://github.com/rhenter/django-stuff',
    version=version,
)
