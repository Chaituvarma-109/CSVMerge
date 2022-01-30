import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="CSV-pydev",
    version="0.0.3",
    author="Chaitanya Varma",
    author_email="justme.python@gmail.com",
    description="Package for Merging Multiple CSV files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chaituvarma-109/CSVMerge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=['CSV'],
    python_requires=">=3.9",
)
