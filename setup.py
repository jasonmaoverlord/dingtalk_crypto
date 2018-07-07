#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='dingtalk_crypto_upgrade',
    version='1.0.0',
    description='钉钉加密解密工具',
    long_description='',
    author='jasonmaoverlord',
    author_email='2420582240@qq.com',
    url='https://github.com/jasonmaoverlord/dingtalk_crypto',
    packages=['dingtalk_crypto', 'tests'],
    install_requires=['pycrypto'],
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ),
    license='MIT'
)
