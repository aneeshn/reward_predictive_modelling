import os
from setuptools import find_packages, setup


def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="reward_predictive_modelling",
    packages=find_packages(exclude=["tests"]),
    install_requires=required,
    version="0.0.1",
    author="Aneesh Chandran",
    python_requires=">=3.8",
    extras_require={
        "dev": [
            "pre-commit==2.12.0",
        ]
    },
)