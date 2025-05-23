from setuptools import find_packages, setup

setup(
    name="UniMiB-Lab",
    version="0.1.0",
    packages=find_packages(),  # Automatically find all packages
    author="Lorenzo Minuz",
    author_email="minuzlorenzo@gmail.com",
    description="Una libreria contenente le funzioni principali da utilizzare durante il corso di Laboratorio 2 e Laboratorio 1 dell'Università degli studi Milano Bicocca",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LM0516/UniMiB-Lab",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
