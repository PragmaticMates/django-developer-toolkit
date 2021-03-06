#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-developer-toolkit',
    version='0.4.2',
    description='Django utility app for Django developers.',
    long_description=open('README.rst').read(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-developer-toolkit',
    packages=[
        'developer_toolkit',
    ],
    include_package_data=True,
    install_requires=('django', 'ordereddict'),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha'
    ],
    license='GPL License',
    keywords = "django toolkit developer utility",
)
