from pyswip import Prolog

prolog = Prolog()

prolog.consult("kb.pl") 

print(list(prolog.query("grandparent(X, bart)")))   
print(list(prolog.query("grandparent(X, lisa)")))   
print(list(prolog.query("grandparent(X, maggie)"))) 
print(list(prolog.query("grandparent(abe, Y)")))
print(list(prolog.query("male(X)")))     