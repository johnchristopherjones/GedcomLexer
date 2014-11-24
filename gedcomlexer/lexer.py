#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ['GedcomLexer']

class GedcomLexer(RegexLexer):
    name = 'Gedcom'
    aliases = ['gedcom']
    filenames = ['*.ged', '*.gedcom']
    flags = re.DOTALL | re.UNICODE | re.MULTILINE

    tokens = {
        'root': [
            # 0-level Reference Record Start
            (r'^(0)( )(@)([^@ ]+)(@)( )(\w+)$', bygroups(Number, Whitespace, Operator, Name.Variable, Operator, Whitespace, Keyword)),
            # 0-level Reference-less Record Start
            (r'^(0)( )(\w+)$', bygroups(Number, Whitespace, Keyword)),
            # Regular record with reference
            (r'^(\d)( )([^@ ]+)( )(@)([^@ ]+)(@)$', bygroups(Number, Whitespace, Keyword, Whitespace, Operator, Name.Variable, Operator)),
            # Regular record without literal value
            (r'^(\d)( )([^@ ]+)$', bygroups(Number, Whitespace, Keyword)),
            # Regular record with literal value
            (r'^(\d)( )([^@ ]+)( )([^\n]+)$', bygroups(Number, Whitespace, Keyword, Whitespace, String)),
        ]
    }
