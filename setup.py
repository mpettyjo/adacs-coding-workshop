#! /usr/bin/env python
"""
Set up for mymodule
"""
from setuptools import setup

requirements = ['numpy>=1.0',
                # others
                ]

setup(
    name='mymodule',
    version=0.1,
    install_requires=requirements,
    python_requires='>=3.6',
    entry_points={'console_scripts':['sky_sim=mymodule.sky_sim:main']}
)

