from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in demo/__init__.py
from demo import __version__ as version

setup(
	name="demo",
	version=version,
	description="this is a demo app",
	author="nahala",
	author_email="nehalanajeeb11@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
