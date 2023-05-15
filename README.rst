Sequanix
########
Sequanix is a graphical user interface (GUI) that can be used to run Snakemake workflows.


.. image:: https://github.com/sequana/sequanix/actions/workflows/main.yml/badge.svg?branch=main
    :target: https://github.com/sequana/sequanix/actions/workflows/main.yml

.. image:: https://coveralls.io/repos/github/sequana/sequanix/badge.svg?branch=main
    :target: https://coveralls.io/github/sequana/sequanix?branch=main

.. image:: http://readthedocs.org/projects/sequana/badge/?version=main
    :target: https://sequana.readthedocs.io/en/main/sequanix.html
    :alt: Documentation Status

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
   :target: http://joss.theoj.org/papers/10.21105/joss.00352
   :alt: JOSS (journal of open source software) DOI


:Python version: 3.8, 3.9, 3.10
:Documentation: `On readthedocs <http://sequana.readthedocs.org/>`_
:Issues: `On github <https://github.com/sequana/sequana/issues>`_
:How to cite: Citations are important for us to carry on developments.

    For **Sequanix**: Dimitri Desvillechabrol, Rachel Legendre, Claire Rioualen,
    Christiane Bouchier, Jacques van Helden, Sean Kennedy, Thomas Cokelaer.
    Sequanix: A Dynamic Graphical Interface for Snakemake Workflows 
    Bioinformatics, bty034, https://doi.org/10.1093/bioinformatics/bty034
    Also available on bioRxiv (DOI: https://doi.org/10.1101/162701)

**Sequanix** is a derivative of the **Sequana** project that is dedicated to the analyse of NGS data (sequencing data). We provide a set of NGS pipelines  including quality control, variant calling, coverage, taxonomy, transcriptomics. Please see the Sequana `documentation <http://sequana.readthedocs.org>`_ for an up-to-date status and further information.



Notes
######

Fix OpenGL for mac Big Sur: https://stackoverflow.com/a/64021312/11988671


Installation
############

Please see the installation notes and installation steps on the https://sequana.readthedocs.io link.


In brief::

    pip install sequanix

For developers, use::


    git clone git@github.com:sequana/sequanix.git
    pip install -e .[testing]


Design choice
#############

Uses PySide6 from v0.2.0. See e.g., https://www.pythonguis.com/faq/pyqt6-vs-pyside6/ from information
on the switch to PySide6. In brief, the Qt project has recently adopted PySide as the official Qt for Python release which should ensure its viability going forward. When we migrate PyQt5 to PyQt6, we therefore decided to use PySide instead of PyQt.

Changelog
~~~~~~~~~

========= ==========================================================================
Version   Description
========= ==========================================================================
0.2.0     * add logo
          * remove pin on python3.7
          * switch from PyQt5 to PySide6
          * remove automatic creation of readtag in config. we let the pipelines
            handle it
0.1.0     * revamp Sequanix independently of Sequana
========= ==========================================================================





