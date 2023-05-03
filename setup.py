from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in eda/__init__.py
from eda import __version__ as version

setup(
	name="eda",
	version=version,
	description="Event Driven Architecture",
	author="sidhu",
	author_email="sidhu@karkhana.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
