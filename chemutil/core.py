from rdkit import Chem


def smi2inchi(smi):
    return Chem.MolToInchi(Chem.MolFromSmiles(smi))


def smi2inchikey(smi):
    return Chem.MolToInchiKey(Chem.MolFromSmiles(smi))


def inchi2smi(inchi):
    return Chem.MolToSmiles(Chem.MolFromInchi(inchi))


def inchi2ikey(inchi):
    return Chem.InchiToInchiKey(inchi)


def flatten_smi(smi):
    return Chem.MolToSmiles(Chem.MolFromSmiles(smi))


def flatten_inchi(inchi):
    return Chem.MolToSmiles(Chem.MolFromInchi(inchi), isomericSmiles=False)
