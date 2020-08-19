from rdkit import Chem


def smi2inchi(smi):
    return Chem.MolToInchi(Chem.MolFromSmiles(smi))


def smi2inchikey(smi):
    return Chem.MolToInchiKey(Chem.MolFromSmiles(smi))


def inchi2smi(inchi):
    return Chem.MolToSmiles(Chem.MolFromInchi(inchi))


def inchi2ikey(inchi):
    return Chem.InchiToInchiKey(inchi)


def flatten(smi):
    return Chem.MolToSmiles(Chem.MolFromSmiles(smi), isomericSmiles=False)
    # m = Chem.MolFromSmiles(smi)
    # Chem.RemoveStereochemistry(m)
    # return Chem.MolToSMiles(m)
