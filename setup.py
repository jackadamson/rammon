import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rammon",
    version="0.1.0",
    author="Jack Adamson",
    author_email="jack@mrfluffybunny.com",
    description="A low-memory alert daemon",
    install_requires=["cryptography", "setproctitle"],
    entry_points={"console_scripts": ["librepass = librepass:main"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://localhost/librepass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.5",
)
