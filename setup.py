from setuptools import setup, find_packages

setup(
    name="grokcli",
    version="0.1.0",
    packages=find_packages(include=["grokcli", "grokcli.*"], exclude=["tests", "docs"]),
    install_requires=[
        "requests",
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'grok = grokcli.main:main',
        ],
    },
    author="Avik Partners, LLC",
    description="Grok CLI for interacting with the Grok platform.",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='>=3.6',
)
