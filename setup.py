"""
Setup script for PlotNeuralNet.

This script configures the PlotNeuralNet package and its dependencies.
"""

from setuptools import find_packages, setup

setup(
    name="PlotNeuralNet",  # Package name
    version="0.1.0",  # Version number
    author="Your Name",  # Your name
    author_email="your.email@example.com",  # Your email
    description="Visualize neural networks.",  # A short description
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically find packages
    include_package_data=True,  # Include non-code files
    install_requires=[
        # Add dependencies here, e.g., 'numpy', 'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
