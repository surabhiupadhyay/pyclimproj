from setuptools import setup, find_packages

setup(
    name="pyclimproj",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "tk",
    ],
    author="Your Name",
    description="GUI-based downloader for hydroclimatic NetCDF data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "pyclimproj-gui = pyclimproj.gui:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
