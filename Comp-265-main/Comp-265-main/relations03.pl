parent(kim,holly).
parent(margaret,kim).
parent(margaret,kent).
parent(esther, margaret).
parent(herbert,margaret).
parent(herbert,jean).
parent(adam,david).
parent(david,solomon).
grandparent(GP,GC):- parent(GP,X),parent(X,GC).
ancestor(X,Y):- parent(X,Y).
ancestor(X,Y):-parent(Z,Y),ancestor(X,Z).   
