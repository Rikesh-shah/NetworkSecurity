"""
The setup.py file is an essential part of packaging and distributing Python
projects. It is used by setuptools(or distutils in older Python versions) to define the configuration
of pour project, such as its metadata, dependencies, and more.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    try:
        requirement_lst : List[str] = []
        with open("requirements.txt", "r") as file:
            # read lines from the file
            lines = file.readlines()

            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name = 'NetworkSecurity',
    version="0.0.1",
    author = "Rikesh Kumar Shah",
    author_email = "rikeshshah2075@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)


"""
-e . --> It mainly refers to the setup.py file and forces to install the requirements.
"""