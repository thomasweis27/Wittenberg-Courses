female(alice).
female(betty).
female(barbara).
female(susan).
female(carol).
female(fran).
female(ellen).
female(elizabeth).
female(heidi).
male(george).
male(bob).
male(tom).
male(charles).
male(carl).
male(frank).
male(finn).
male(ed).
male(henry).
male(herbert).
parent(alice,betty).
parent(george,betty).
parent(alice,bob).
parent(george,bob).
parent(alice,barbara).
parent(george,barbara).
parent(susan,charles).
parent(tom,charles).
parent(susan,carol).
parent(tom,carol).
parent(susan,carl).
parent(tom,carl).
parent(betty,frank).
parent(charles,frank).
parent(betty,fran).
parent(charles,fran).
parent(betty,finn).
parent(charles,finn).
parent(bob,ellen).
parent(carol,ellen).
parent(bob,ed).
parent(carol,ed).
parent(bob,elizabeth).
parent(carol,elizabeth).
parent(barbara,henry).
parent(carl,henry).
parent(barbara,heidi).
parent(carl,heidi).
parent(barbara,herbert).
parent(carl,herbert).
tailof([_|A],A).

% question 1
firstCousin(X,Y) :-
    parent(P1, X),
    parent(P2, Y),
    P1 \= P2,
    parent(GP, P1),
    parent(GP, P2),
    \+ (parent(GP, X) ; parent(GP, Y)).

% question 2
descendent(X, Y) :- 
    parent(Y, X).
% recursion
descendent(X, Y) :- 
    parent(Z, Y),
    descendent(X, Z).

% question 3
doubleTailof(X, Y) :- 
    tailof(X, T), 
    tailof(T, Y).

% question 4
isDuped([]). % when runs out of elements
isDuped([X, X | T]) :- doubleTailof(T, NewT), isDuped(NewT). 
    % this calls question 3 and recursivly calls the remaining elements 

% question 5 - is this right???? This took me forever and I am not sure
isDifference([], _, []).
isDifference([H | T], Y, Z) :-
    member(H, Y), !, isDifference(T, Y, Z).
isDifference([H | T], Y, [H | Z]) :- isDifference(T, Y, Z).