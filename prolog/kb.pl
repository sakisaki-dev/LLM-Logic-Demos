male(homer).
male(bart).
male(abe).
female(marge).
female(lisa).
female(maggie).
female(mona).

parent(abe, homer).
parent(mona, homer).
parent(homer, bart).
parent(homer, lisa).
parent(homer, maggie).
parent(marge, bart).
parent(marge, lisa).
parent(marge, maggie).

% Rule: X is a grandparent of Y if X is a parent of Z and Z is a parent of Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
