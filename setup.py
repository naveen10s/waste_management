from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in waste_management/__init__.py
from waste_management import __version__ as version

setup(
	name="waste_management",
	version=version,
	description="waste management",
	author="Neveka",
	author_email="nevekaberyl@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
