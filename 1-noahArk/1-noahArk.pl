% A man needs to ferry a wolf, a goat, and a cabbage to the opposite bank of a river
% but he has a boat that can carry at most two of them (in addition to the man).
% Furthermore, the goat cannot be left alone with either the wolf or the cabbage.



% Facts
animal(wolf).
animal(cabbage).
animal(goat).
animals([wolf, cabbage, goat]).



% Utilities

remove(E, [E|T], T).
remove(E, [H|T1], [H|T2]):-remove(E, T1, T2),!.

putf(List,E,NewList):-NewList=[E|List].

putl([],E,[E]).
putl([H|T1], E, [H|T2]):-putl(T1, E, T2).

count(0, []).
count(Count, [_|T]):-count(C,T),Count is C+1.

member2(E, [E|_]).
member2(X, [_|T]):-member2(X, T).



% This ensure that the two banks are safe for the goat

safe([]).
safe(Animals):-count(C, Animals),C=3.
safe(Animals):-count(C, Animals),C=2,not(member(goat, Animals)).
safe(Animals):-count(C, Animals),C=1.

transport([], TransportedAnimals, Solution, [], TransportedAnimals, Solution).
transport(RemAnimals, TransportedAnimals, Solution, NewRemAnimals, NewTransportedAnimals, NewSolution):-
    animal(X),
    member2(X, RemAnimals),
    remove(X, RemAnimals, RemAnimals1),
    safe(RemAnimals1),
    putl(TransportedAnimals, X, TransportedAnimals1),
    putl(Solution, ['move', X], Solution1),
    safe(TransportedAnimals1),
    transport(RemAnimals1, TransportedAnimals1, Solution1, NewRemAnimals, NewTransportedAnimals, NewSolution).
transport(RemAnimals, TransportedAnimals, Solution, NewRemAnimals, NewTransportedAnimals, NewSolution):-
    animal(X), animal(Y), not(X=Y),
    member2(X, RemAnimals), member2(Y, RemAnimals),
    remove(X, RemAnimals, RemAnimals1),
    remove(Y, RemAnimals1, RemAnimals2),
    safe(RemAnimals2),
    putl(TransportedAnimals, X, TransportedAnimals1),
    putl(TransportedAnimals1, Y, TransportedAnimals2),
    putl(Solution, ['move', X, 'and', Y], Solution1),
    safe(TransportedAnimals2),
    transport(RemAnimals2, TransportedAnimals2, Solution1, NewRemAnimals, NewTransportedAnimals, NewSolution).

main(Solution, TransportedAnimals):-
    animals(Animals),
    transport(Animals, [], [], _, TransportedAnimals, Solution).
