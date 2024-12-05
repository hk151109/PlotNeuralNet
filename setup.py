"""
Setup script for PlotNeuralNet.

This script configures the PlotNeuralNet package and its dependencies.
"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:

    long_description = fh.read()

setup(
    name="PlotNeuralNet",
    version="0.1.0",
    author="Kaden Gruizenga",
    author_email="kgruiz@umich.edu",
    description="Visualize neural networks with a focus on easy-to-use diagrams.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
    url="https://github.com/kgruiz/PlotNeuralNet",
    project_urls={
        "Source": "https://github.com/kgruiz/PlotNeuralNet",
        "Original Work": "https://github.com/HarisIqbal88/PlotNeuralNet",
    },
)
