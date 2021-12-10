from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quebec_app/__init__.py
from quebec_app import __version__ as version

setup(
	name="quebec_app",
	version=version,
	description="App custom",
	author="Romeo",
	author_email="romeorealist@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
