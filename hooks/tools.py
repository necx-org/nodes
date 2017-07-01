"""Some tools for encryption management."""
import os
import glob
import itertools


REPO_ROOT = os.path.dirname(os.path.dirname(__file__))
KEYS_FILE = os.path.join(REPO_ROOT, 'keys.json')
ANS_PREFIXES = ['a-', 'ans-', 'sol-']
ANS_PRE_STAR = [_ + '*' for _ in ANS_PREFIXES]


def find_nodes(abspath=False):
    """Find node directories in the repo"""
    infos = glob.glob(os.path.join(REPO_ROOT, '*', 'info.yml'))
    nodes = [os.path.dirname(i) for i in infos]
    if not abspath:
        nodes = [os.path.basename(n) for n in nodes]
    return nodes


def find_answers(nodes=None, abspath=False):
    """Finds the answer files in the nodes"""
    if nodes is None:
        nodes = find_nodes(abspath=abspath)
    answers = []
    for node, apre in itertools.product(nodes, ANS_PRE_STAR):
        answers.extend(glob.iglob(os.path.join(node, apre)))
    return answers


def encrypted_answer_filenames(answers):
    """Returns the filenames for the hash files ans the enrcrypted files."""
    sha256s = []
    encs = []
    for answer in answers:
        d, base = os.path.split(answer)
        sha256s.append(os.path.join(d, '.' + b + '.sha256'))
        encs.append(os.path.join(d, '.' + b + '.enc'))
    return sha256s, encs

