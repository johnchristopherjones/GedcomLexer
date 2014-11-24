# GedcomLexer

GedcomLexer is a plugin for the `pygments` python module.  It adds GEDCOM syntax highlighting to `pygments`.

## Installation

GedcomLexer can be installed directly from github using `pip`:

```bash
$ sudo pip install git+https://github.com/johnchristopherjones/GedcomLexer.git
```

For development, GedcomLexer can be installed using setuptools:

```bash
$ git clone https://github.com/johnchristopherjones/GedcomLexer.git
$ cd GedcomLexer
$ sudo python setup.py developer
```

or using pip:

```bash
$ git clone https://github.com/johnchristopherjones/GedcomLexer.git
$ sudo pip install --editable GedcomLexer/GedcomLexer
```

Installing using setuptools allows you to link the cloned git repository into your python `dist-packages` directory so that any changes you make to the repo are instantly reflected in your python installation.
