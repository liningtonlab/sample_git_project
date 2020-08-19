# Sample Git Project

This is a sample Git project for the Linington Lab, presentation Aug. 19, 2020.

#### Requirements

Requires the RDKit, which is easiest to install using `conda`. Here is how to create a conda virtual environment with RDKit installed.

`conda create -n chemutil -c conda-forge rdkit`

Make sure to activate this environment.

`conda activate chemutil`

#### Installation

This will create a copy of the Python code to the virtual environments `bin` folder.

`python setup.py install`

#### Development

Install pytest

`conda install pytest`

This will create a sym-link and update the CLI with code changes.

`python setup.py develop`
