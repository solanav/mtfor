import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mtfor",
    version="0.0.1",
    author="Antonio Solana",
    author_email="solanav@qq.com",
    description="Plug 'n' play multithreaded for",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/solanav/mtfor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)