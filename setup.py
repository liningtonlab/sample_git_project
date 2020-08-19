from setuptools import setup

setup(
    name="chemutil",
    version="0.0.1",
    packages=["chemutil"],
    entry_points={"console_scripts": ["chemutil = chemutil.cli:cli",]},
    # install_requires=["rdkit",], # requires conda
    python_requires=">=3.6",
)
