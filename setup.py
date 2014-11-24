from setuptools import setup, find_packages

setup (
    name = 'gedcomlexer',
    package = find_packages(),
    entry_points =
    """
    [pygments.lexers]
    gedcomlexer = gedcomlexer.lexer:GedcomLexer
    """,
)
