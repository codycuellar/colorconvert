import os
from setuptools import setup, find_packages


install_path = os.path.abspath(os.path.dirname(__file__))


setup(
	name='colorconvert',
	version='0.0.1',
	packages=find_packages(),
	author='Cody Cuellar',
	author_email='cody.cuellar@gmail.com',
	description='Simple color math and conversion library.',
	install_requires=['numpy'],
	python_requires='>=3.8'
)
