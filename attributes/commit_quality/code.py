from spellchecker import SpellChecker
import re
trim_commit = "This is a                corect.py10 100 sentce !@but \a wring one too"
tr = re.sub("[^0123456789 ]","",trim_commit)
print(tr)
trim_commit = re.sub("[^a-zA-Z ]+", "", trim_commit)
print(trim_commit)
length = len(trim_commit.split())
trim_commit = re.sub(r"\b[0123456789]\b", "", trim_commit)
print(length)
print(trim_commit)
print(len(trim_commit.split()))
trim_commit = re.sub(r"\b[a-zA-Z]\b", "", trim_commit)
trim_commit = re.sub(r"\b[a-zA-Z][a-zA-Z]\b", "", trim_commit)
#trim_commit = ' '.join(trim_commit.split())
spell = SpellChecker(distance=2)
misspelled = spell.unknown(trim_commit.split())
correctly_spelled = spell.known(trim_commit.split())
print('mis: ',misspelled)
print('corr: ',correctly_spelled)