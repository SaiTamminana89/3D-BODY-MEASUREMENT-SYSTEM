# he main aim of a setup file is to simplify the installation and configuration process for a software application
from setuptools import setup,find_packages
from typing import List

# this function returns the list of requirements
def get_requirements(file_Path:str)->List[str]:
  with open(files_Path,'r') as file:
    file_r = file.readlines()
    file_r = [r.replace('/n','') for r in file_r]
    requirements = file_r
  return requirements

    
    

setup(
name='3D_BODY_MEASUREMENT_SYSTEM'
version='0.0.1',
author = 'SaiKumar',
email = 'saitamminana@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)

