import sys
import os

from ez_setup import use_setuptools
use_setuptools('0.6c3')

from setuptools import setup, find_packages, Extension
from distutils.sysconfig import get_python_inc
from glob import glob
import commands


dist = setup( name='shr-installer',
    version='0.0.1',
    author='dos',
    author_email='seba.dos1@gmail.com',
    description='python-elementary and PackageKit based installer for SHR distribution',
    url='http://shr-project.org/',
    download_url='git://git.shr-project.org/repo/shr-installer.git',
    license='GNU GPL',
    scripts=['shr-installer'],
    data_files=[('pixmaps/shr-installer' , glob("data/icons/*.png")),
                ('applications', ['data/shr-installer.desktop'])]
)

installCmd = dist.get_command_obj(command="install_data")
installdir = installCmd.install_dir
installroot = installCmd.root

if not installroot:
    installroot = ""

if installdir:
    installdir = os.path.join(os.path.sep,
        installdir.replace(installroot, ""))

