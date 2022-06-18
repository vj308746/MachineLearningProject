from setuptools import setup
from typing import list

#DECLARING variable for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.1"
AUTHOR="Vishal Joshi"
DESCRIPTION="First machine learning project"
PACKAGES=['HOUSING']
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup()
name ="PROJECT_NAME",
version="0.0.1"
author="Vishal"
packages="PACKAGES"
install_requires=get_requirements_list()    


if __name__=="__main__":
    print(get_requirements_list())
