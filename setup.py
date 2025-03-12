from setuptools import setup, find_packages

setup(
    name="cursormind",
    version="0.2.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0.0",
        "rich>=10.0.0",
        "python-dateutil>=2.8.2",
        "pytz>=2021.3",
    ],
    entry_points={
        "console_scripts": [
            "cursormind=cursormind.cli:main",
        ],
    },
) 