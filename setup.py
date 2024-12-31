from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements

    """
    requirement_lst:List[str] = []

    try:
        with open('requirements.txt', 'r') as f:
            # read lines from the file
            lines = f.readlines()
            ## process each line
            for line in lines:
                requirement = line.strip()
                # ignore the empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='John Farrell',
    author_email='johndfarrell@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
