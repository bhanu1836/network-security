from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    try:
        with open('requirements.txt','r') as f:
            lines = f.readlines() 
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')
    return requirement_list


setup(
    name='Network Security',
    version='0.0.1',
    author='K.Bhanu Prakash',
    author_email='itzbhanu00@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)