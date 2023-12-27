"""Setups the package for installation."""

from setuptools import setup, find_packages


def load_requirements():
    """Load requirements from file."""
    with open("requirements.txt") as f:
        return f.readlines()


setup(
    install_requires=load_requirements(),
    setup_requires=["setuptools_scm"],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
)
