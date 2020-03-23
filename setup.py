from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='simPAsig',
    version='0.1.0',
    description='Simulation of a photo acoustic signal excitation',
    long_description=readme(),
    author='Franz Taffner',
    author_email='franz.taffner@yahoo.de',
    url='https://github.com/fxat/simulationPAsignal',
    license=license,    
    packages=['simPAsig', 'simPAsig.sim', 'simPAsig.constants', 'simPAsig.plots'],
    #scripts=['simPAsig/runSim.py']
    entry_points={'console_scripts': ['run_Sim = simPAsig.runSim:main']}
)
