import os

from pyswip import Prolog

prolog = Prolog()

# Resolve kb.pl next to this script so the demo runs from any directory.
KB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kb.pl")
prolog.consult(KB_PATH.replace(os.sep, "/"))

print(list(prolog.query("grandparent(X, bart)")))   
print(list(prolog.query("grandparent(X, lisa)")))   
print(list(prolog.query("grandparent(X, maggie)"))) 
print(list(prolog.query("grandparent(abe, Y)")))
print(list(prolog.query("male(X)")))     