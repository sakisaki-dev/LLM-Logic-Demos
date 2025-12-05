from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z, male, female, parent, grandparent')

+male('homer')
+male('bart')
+male('abe')

+female('marge')
+female('lisa')
+female('maggie')

+parent('abe', 'homer')
+parent('homer', 'bart')
+parent('homer', 'lisa')
+parent('homer', 'maggie')

grandparent(X, Y) <= parent(X, Z) & parent(Z, Y) 

# Test Set 

print("Grandparent's of Bart: ")
print(grandparent(X, 'bart'))
print('\nGrandchildren of Abe: ')
print(grandparent('abe', Y))