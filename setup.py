from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-formats',
	version=version,
	description="File Format Extension",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Alan Steremberg',
	author_email='alan.steremberg@gsa.gov',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.formats'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
        formats=ckanext.formats.plugin:FormatsPlugin
	""",
)
