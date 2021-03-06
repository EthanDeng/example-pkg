import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example",
    version="0.0.1",
    author="XXX",
    author_email="XXX@yyyy.com",
    description="example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="example site url",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)