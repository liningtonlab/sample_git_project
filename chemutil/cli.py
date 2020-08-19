import sys
from .core import *

OPTIONS = (
    "smi2inchi",
    "smi2inchikey",
    "flatten",
    "inchi2smi",
    "inchi2ikey",
)


def error():
    print("Usage: chemutil option input_structure")
    print(f"Options: {', '.join(OPTIONS)}")
    sys.exit(1)


def cli():
    if len(sys.argv) != 3:
        error()
    opt = sys.argv[1]
    inp = sys.argv[2]
    if opt not in OPTIONS:
        error()
    print(globals()[opt](inp))


if __name__ == "__main__":
    cli()
