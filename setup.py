from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

with open('requirements.txt', 'r') as fp:
    requirements = list()
    for line in fp:
        requirements.append(line.strip('\n'))


setup(
    name='example',
    version='0.1.0',
    packages=find_package()
    install_requires = requirements
)
