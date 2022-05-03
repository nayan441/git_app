from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in naffhis01/__init__.py
from naffhis01 import __version__ as version

setup(
	name="naffhis01",
	version=version,
	description="none",
	author="nayan",
	author_email="nayan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
