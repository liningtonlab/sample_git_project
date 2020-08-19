import pytest


@pytest.fixture
def TEST_SMI():
    return ["c1ccccc1", "CC[C@@H](C)c1cccc2ccccc12"]


@pytest.fixture
def TEST_INCHI():
    return [
        "InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H",
        "InChI=1S/C14H16/c1-3-11(2)13-10-6-8-12-7-4-5-9-14(12)13/h4-11H,3H2,1-2H3/t11-/m1/s1",
    ]


@pytest.fixture
def TEST_INCHIKEY():
    return [
        "UHOVQNZJYSORNB-UHFFFAOYSA-N",
        "NDLQGVXBUFZFIX-LLVKDONJSA-N",
    ]


@pytest.fixture
def TEST_FLAT_SMI():
    return ["c1ccccc1", "CCC(C)c1cccc2ccccc12"]
