# -*- coding: utf-8 -*-
#
#  This file is part of Sequana software
#
#  Copyright (c) 2016 - Sequana Development Team
#
#  File author(s):
#      Thomas Cokelaer <thomas.cokelaer@pasteur.fr>
#      Dimitri Desvillechabrol <dimitri.desvillechabrol@pasteur.fr>,
#          <d.desvillechabrol@gmail.com>
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/sequana/sequana
#  documentation: http://sequana.readthedocs.io
#
##############################################################################
""".. rubric:: misc utilities"""
import os
import glob
import platform
import pathlib
import re
import subprocess

import ruamel.yaml

import colorlog

logger = colorlog.getLogger(__name__)

from docutils import core
from docutils.writers.html4css1 import Writer, HTMLTranslator


__all__ = ["rest2html", "on_cluster", "YamlDocParser"]


def on_cluster(cmds=["sbatch"]):
    """Used to check if we are on a cluster

    :return: True is a clsuter commands is found

    Currently, checks for slurm commands only

    """

    def cmd_exists(cmd):
        result = subprocess.call(
            "type " + cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result == 0

    for cmd in cmds:
        if cmd_exists("sbatch"):
            return True
    return False


class HTMLFragmentTranslator(HTMLTranslator):
    def __init__(self, document):
        HTMLTranslator.__init__(self, document)

    def astext(self):
        return "".join(self.body)

    def visit_document(self, node):
        self.body.append(self.starttag(node, "div", CLASS="comment"))


html_fragment_writer = Writer()
html_fragment_writer.translator_class = HTMLFragmentTranslator


def rest2html(s):
    """Converts a restructuredText document into HTML

    Note that the returned object is a bytes so need to be
    decoded with decode()"""
    return core.publish_string(s, writer=html_fragment_writer)


class YamlDocParser(object):
    """A simple parser to extract block content to be found in YAML files

    So as to create tooltips automatically in :ref:`sequanix`, one can comment
    YAML configuration file with block comments (see developers guide in
    :ref:`developers` )

    Once read and parsed, all block comments before top-level sections are to
    be found in the dictionary :attr:`sections`.

    .. doctest::

        from sequana_pipetools import snaketools
        from sequanix.misc import YamlDocParser
        module = snaketools.Module('quality_control')
        r = YamlDocParser(module.config)
        r.sections['fastqc']

    Those lines are removed from the docstring but available as a dictionary

    """

    def __init__(self, filename):
        """.. rubric:: constructor

        :param str filename: the YAML file to parse

        ::

            # main documentation

            # block comment
            section1:
                - item

            # block comment
            section2:

            # a comment

            section3:

        Here, section1 and section2 have block comments but not section3

        """
        self.filename = filename
        self.regex_section = re.compile("^[a-z,A-Z,_,0-9]+:")
        self._specials = ["choice__"]

        self.sections = {}
        self._read_data()
        self._parse_data()

    def _get_expected_sections(self):
        """Get the top level keys in the YAML file

        :return: list of top level sections' names"""

        with open(self.filename, "r") as fh:
            yaml = ruamel.yaml.YAML(typ="unsafe", pure=True)
            data = yaml.load(fh.read())
        keys = list(data.keys())
        return keys

    def _read_data(self):
        with open(self.filename, "r") as fh:
            self.data = fh.readlines()

    def _parse_data(self):
        """Parse the YAML file to get the block content (comments)
        before each top-level sections. See doc in the constructor

        Removes all # so that the block of comments can be interpreted as
        a standard docstring in Sequanix
        """
        current_block = []
        current_section = "docstring"

        # if we get a line that starts with #, this is a new comment or
        # part of a block comment. Otherwise, it means the current block
        # comment has ended.

        for this in self.data:
            # Beginning of a new section at top level
            if self.regex_section.findall(this):
                name = self.regex_section.findall(this)[0]
                current_section = name.strip(":")
                self.sections[current_section] = "".join(current_block)
                current_block = []
                current_section = None
            elif this.startswith("#"):  # a comment at top level
                current_block.append(this)
            elif this.strip() == "":  # an empty line
                # this was the main comment, or an isolated comment
                current_block = []
            else:  # a non-empty line to skip
                current_block = []

        for key in self._get_expected_sections():
            if key not in self.sections.keys():
                logger.warning("section %s not dealt by the parsing function" % key)

    def _block2docstring(self, section):
        if section not in self.sections.keys():
            logger.warning("%s not found in the yaml " % section)
            return
        comments = self.sections[section]
        docstring = []
        for line in comments.split("\n"):
            if "#############" in line:
                pass
            elif sum([this in line for this in self._specials]):
                pass
            else:
                if len(line) < 2:  # an empty line (to keep)
                    docstring.append("")
                else:
                    docstring.append(line[2:])  # strip the "# "characters
        docstring = "\n".join(docstring).strip()
        return docstring

    def _get_specials(self, section):
        """This method extracts data from the docstring

        Lines such as ::

            field_choice__ = ["a", "b"]

        are extracted. Where _choice is a special keyword to be
        found.

        """
        if section not in self.sections.keys():
            logger.warning("%s not found in the yaml " % section)
            return
        comments = self.sections[section]
        specials = {}
        for line in comments.split("\n"):
            if "#############" in line:
                pass
            elif sum([this in line for this in self._specials]):
                for special in self._specials:
                    line = line[2:]
                    key, value = line.split("=", 1)
                    key = key.strip().rstrip("__")
                    value = value.strip()
                    specials[key] = list(eval(value))
        return specials
