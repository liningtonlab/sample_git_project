import pytest

from chemutil import core


def test_smi2inchi(TEST_SMI, TEST_INCHI):
    for idx, smi in enumerate(TEST_SMI):
        assert core.smi2inchi(smi) == TEST_INCHI[idx]


def test_smi2inchikey(TEST_SMI, TEST_INCHIKEY):
    for idx, smi in enumerate(TEST_SMI):
        assert core.smi2inchikey(smi) == TEST_INCHIKEY[idx]


def test_flatten(TEST_SMI, TEST_FLAT_SMI):
    for idx, smi in enumerate(TEST_SMI):
        assert core.flatten(smi) == TEST_FLAT_SMI[idx]


def test_inchi2smi(TEST_INCHI, TEST_SMI):
    for idx, smi in enumerate(TEST_INCHI):
        assert core.inchi2smi(smi) == TEST_SMI[idx]


def test_inchi2inchikey(TEST_INCHI, TEST_INCHIKEY):
    for idx, smi in enumerate(TEST_INCHI):
        assert core.inchi2ikey(smi) == TEST_INCHIKEY[idx]
