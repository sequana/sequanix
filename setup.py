import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sequanix",
    version="0.0.1",
    author="Sequana Team",
    description="Sequanix is a graphical user interface (GUI) that can be used to run Snakemake workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sequana/sequanix",
    project_urls={
        "Bug Tracker": "https://github.com/sequana/sequanix/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix"
    ],
    packages=[],
    python_requires="==3.7.*",
    install_requires=open("requirements.txt").read(),
    tests_requires=['pytest'],
    entry_points={
        'console_scripts': [
            'sequanix=sequanix:main',
        ],
    },
)
