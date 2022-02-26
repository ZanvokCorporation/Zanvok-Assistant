import setuptools

with open("README.md" , "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Zanvok-Assistant",
    version="12.4.0",
    author="Zanvok Corporation",
    description="A virtual assistant made in python for PCs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)