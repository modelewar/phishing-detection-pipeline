

from setuptools import setup,find_packages

from typing import List

def get_requirements()->List[str]:
    
    """
        This function will return list of requirements
    """
    req_lst:List[str]=[]
    try :
        with open('requirements.txt','r') as file:
            lines=file.readlines()

            for line in lines:
                req=line.strip()

                if req and req!='-e .':
                    req_lst.append(req)


    except FileNotFoundError:
        print('File not Found...!')

    return req_lst

# print(get_requirements())

setup(
    name="Network Security",
    version="0.0.1",
    author="modelewar",
    author_email='delewarmohamed@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()


)