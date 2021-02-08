from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import SD4_Lab2
import os
from glob import glob
import site


setup(
	name = "SD4_Lab2",
	version = SD4_Lab2.__version__,
	url = 'pynq',
	license = 'Software License',
	author = "SD4_Lab2",
	author_email = "t3s@ecam.be",
	include_package_data = True,
	packages=find_packages(),
	package_data = {
	'' : ['*.bit','*.tcl','*.py'],
	},
	data_files = [(os.path.join('/home/xilinx/jupyter_notebooks/SD4_Lab2',root.replace('notebooks/','')), [os.path.join(root, f) for f in files]) for root, dirs, files in os.walk('notebooks/')],
	description = "PYNQ-Z2 labs using a hardware accelerated "
)

if os.path.isdir(os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/SD4_Lab2/"):
	shutil.rmtree(os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/SD4_Lab2/")
shutil.copytree("notebooks/",os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/SD4_Lab2/")
