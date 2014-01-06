#!/usr/bin/env python
from distutils.core import setup, Extension

module1 = Extension('rPi_spi', sources = ['rPi_spi.c'])

setup (
	name = 'rPi_spi',
	author='Louis Thiery',
	url='https://github.com/hybotics/rPi-SPI-Py',
	download_url='https://github.com/hybotics/rPi-SPI-Py/archive/master.zip',
	version = '1.01',
	description = 'rPi_spi: Hardware SPI as a C Extension for Python',
	license='GPL-v2',
	platforms=['Linux'],
	ext_modules = [module1]
)
