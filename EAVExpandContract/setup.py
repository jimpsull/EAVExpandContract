# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:00:55 2018

@author: SulliJP
"""

from distutils.core import setup

setup(
      name='EAVExpandContract',
      version='0.1',
      description='Change table to EAV format or expand from EAV format',
      packages=['EAVExpandContract'],
      license='JPS',
      long_description=open('README.txt').read(),
      author='Jim Sullivan',
      author_email='MediatorJim@Yahoo.com',
      keywords=['eav','sparse','compress','expand'],
      download_url='https://github.com/jimpsull/PythonEAVExpandContract'
)