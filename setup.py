from setuptools import setup, find_packages


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# handle sequana git link
with open("requirements.txt") as fh:
    requirements = [req.rstrip() if not req.startswith("git+") else req.rstrip().split('egg=')[-1] for req in fh]

setup(
    name="sequanix",
    version="0.2.0",
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
    packages=find_packages(exclude=['tests*']),
    #python_requires="==3.7.*",
    install_requires=requirements,
    extras_require={
        "testing": [
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "pytest-qt",
            #"pytest-xvfb", # issue on CI action and locally with X11 connection broke and core dump
            "coveralls",
        ],
        "pipelines": [
            "sequana_fastqc"
        ],
        "doc": [
            "sphinx>=3",
            "sphinx_rtd_theme",
            "sequana_sphinxext",
        ],
    },







    entry_points={
        'console_scripts': [
            'sequanix=sequanix:main',
        ],
    },
)
