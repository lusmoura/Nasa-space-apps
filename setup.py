import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covidata",
    version="0.0.5",
    author="Control-space",
    author_email="author@example.com",
    description="Easily access NASA, ESA and JAXA data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lusmoura/Nasa-space-apps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pandas', 
                    'requests',
                    'beautifulsoup4',
                    ' lxml']
)