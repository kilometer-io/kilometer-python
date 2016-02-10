from setuptools import setup, find_packages

LONG_DESCRIPTION = "The official Kilometer.io library for python"

setup(
    name='kilometer',
    version='0.8.2',
    description='The official Kilometer.io library for Python',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/kilometer-io/kilometer-python',
    author='Kilometer.io Ltd.',
    author_email='info@kilometer.io',
    license='Apache',
    install_requires=['requests >= 2.9.1'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    keywords='kilometer analytics',
    packages=find_packages(),
)
