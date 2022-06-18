from setuptools import find_packages, setup, find_packages
from typing import List

#DECLARING variable for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Vishal Joshi"
DESCRIPTION="First machine learning project"
PACKAGES=find_packages(),
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup()
name ="PROJECT-NAME",
version="VERSION"
author="AUTHOR"
packages="PACKAGES"
install_requires=get_requirements_list()    


if __name__=="__main__":
    print(get_requirements_list())
