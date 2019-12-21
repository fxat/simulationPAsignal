
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='simPAsig',
    version='0.1.0',
    description='Simulation of a photo acoustic signal excitation',
    long_description=readme,
    author='Franz Taffner',
    author_email='franz.taffner@yahoo.de',
    url='https://github.com/fxat/simulationPAsignal',
    license=license,
    packages=find_packages()
)
