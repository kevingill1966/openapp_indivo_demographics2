from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='openapp_indivo_demographics2',
      version=version,
      description="Version of openapp_indivo_demographics using indivo models directly",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='indivo',
      author='Kevin Gill (openapp)',
      author_email='kevin.gil@openapp.ie',
      url='',
      license='AGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openapp_indivo'],
      include_package_data=True,
      package_data = {'':['README.rst']},
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
