%gender
male(homer).
male(abraham).
male(bart).
male(clancy).
male(seymourtSkiner).
male(milHouse).
male(santasLittleHelper).
male(kang).

female(marge).
female(lisa).
female(maggie).
female(mona).
female(jacque).
female(paty).
female(selma).
female(ednaKrabappe).
female(snowball).

%father
father(abraham,homer).
father(clancy,marge).
father(clancy, paty).
father(clancy,selma).
father(homer,bart).
father(homer,lisa).
father(homer,maggie).

%mother
mother(jacque,marge).
mother(jacque,paty).
mother(jacque,selma).
mother(mona,homer).
mother(marge,bart).
mother(marge,lisa).
mother(marge,maggie).

%parent
parent(X,Y):- father(X,Y) ; mother(X,Y).

%child
child(X,Y):- parent(Y,X).
son(X,Y):- child(X,Y), male(X).
daughter(X,Y):- child(X,Y), female(X).

%sibling
sibling(X,Y):- parent(Z,X), parent(Z,Y), X \= Y.
brother(X,Y):- sibling(X,Y), male(X). %revisarAfemale
sister(X,Y):- sibling(X,Y), female(X). %revisarAmale

%grandparent
grandparent(X,Y):- parent(X,Z), parent(Z,Y).
grandFather(X,Y):- grandparent(X,Y), male(X).
grandMother(X,Y):- grandparent(X,Y), female(X).

%grandchild
grandChild(X,Y):- grandparent(Y,X).
grandson(X,Y):- grandChild(X,Y), male(X).
granddaughter(X,Y):- grandChild(X,Y), female(X).

%uncle/aunt
parents_siblings(X,Y):- sibling(Z,X), parent(Z,Y).
uncle(X,Y):- parents_siblings(X,Y), male(X).
aunt(X,Y):- parents_siblings(X,Y), female(X).

%nephew
nibling(X,Y):- parents_siblings(Y,X).
nephew(X,Y):- nibling(X,Y), male(X); female(X).