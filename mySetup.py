"""
Setup script for DIRAC
"""

import os
import re

from setuptools import setup


PACKAGES= [
  "AccountingSystem",
  "ConfigurationSystem",
  "Core",
  "DataManagementSystem",
  "FrameworkSystem",
  "Interfaces",
  "RequestManagementSystem",
  "Resources",
  "ResourceStatusSystem",
  "StorageManagementSystem",
  "TransformationSystem",
  "Workflow",
  "WorkloadManagementSystem",
]

def find_packages(path='.'):
  """ find all packages, need to re-implement from setuptools because we need to follow the links """
  ret = []
  for root, _dirs, files in os.walk(path, followlinks=True):
    if '__init__.py' in files:
      ret.append(re.sub('^[^A-z0-9_]+', '', root.replace('/', '.')))

  return ret

def read(fname):
  """ read fname and return the string """
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

def makeDIRAC( bf="DIRAC" ):
  """ crete a DIRAC module with the existing PACKAGES """
  if not os.path.exists( bf ):
    os.mkdir( bf )
  for folder in PACKAGES+['__init__.py']:
    newFolder=os.path.join( bf, folder )
    if not os.path.exists( newFolder ):
      os.symlink( "../%s" % folder, newFolder )
 
 
makeDIRAC()

setup(
  name = "DIRAC",
  version = "19",
  keywords = "",
  packages=find_packages( "DIRAC" ),
  license = "GPL3",
  long_description='README.md',
  classifiers=[
    "Development Status :: 3 - Production",
    "Topic :: Grid",
  ],
)
