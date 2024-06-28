% The backpack problem is a classic operational research problem formulated as follows:
% We have a backpack in which we can place items that have a weight and a value. 
% The objective of the problem is to maximize the value of the knapsack without exceeding its capacity.

% Utilities 

member2(E, [E|_]).
member2(E, [_| T]):-member2(E, T).

putl(E, [], [E]).
putl(E, [H|TS], [H|TD]):-putl(E, TS, TD).

count(0, []).
count(C, [_|T]):-count(C1, T), C is C1 + 1.

max(_, []):-!.
max(E, [H|T]):-E>H,max(E, T).

findMax([H|T], H):-max(H, T).
findMax([H|T], Max):-not(max(H,T)),findMax(T, Max),!.



% Available items with ID, weight (kg), and value

item(1, 2, 3).
item(2, 4, 2).
item(3, 9, 3).
item(4, 7, 5).

maxCapacity(50).



weight_calculator([], 0).
weight_calculator([item(_, Weight, _) | T], Sum):-
    weight_calculator(T, Sum1),
    Sum is Sum1 + Weight.

value_calculator([], 0).
value_calculator([item(_, _, Value) | T], Sum):-
    value_calculator(T, Sum1),
    Sum is Sum1 + Value.

check_capacity(Backpack):-
    maxCapacity(MaxCapacity),
    weight_calculator(Backpack, Weight),
    Weight =< MaxCapacity.



fill(Backpack, RetFilledBackpacks, RetFilledBackpacks):-count(C, Backpack), C=4.
fill(Backpack, FilledBackpacks, RetFilledBackpacks):-
    item(ID, Weight, Value),
    not(member2(item(ID, Weight, Value), Backpack)),
    count(C, Backpack), C=<3,
    putl(item(ID, Weight, Value), Backpack, Backpack1),
    check_capacity(Backpack1),
    value_calculator(Backpack1, ValueBackpack),
    putl((Backpack1, ValueBackpack), FilledBackpacks, FilledBackpacks1),
    fill(Backpack1, FilledBackpacks1, RetFilledBackpacks).



findBestBackpack([], _MaxValue, BestBackpacks, BestBackpacks).
findBestBackpack([(Backpack, Value) | TBackpacks], MaxValue, BestBackpacks, RetBestBackpacks) :-
    Value = MaxValue,
    putl((Backpack, Value), BestBackpacks, BestBackpacks1),
    findBestBackpack(TBackpacks, MaxValue, BestBackpacks1, RetBestBackpacks).
findBestBackpack([(Backpack, Value) | TBackpacks], MaxValue, BestBackpacks, RetBestBackpacks) :-
    not(Value = MaxValue),
    findBestBackpack(TBackpacks, MaxValue, BestBackpacks, RetBestBackpacks).
findBestBackpacks(Backpacks, BestBackpacks) :-
    findall(Value, member((_, Value), Backpacks), Values),
    findMax(Values, MaxValue),
    findBestBackpack(Backpacks, MaxValue, [], BestBackpacks).



main(BestBackpacks):-
    fill([], [], FilledBackpacks),
    findBestBackpacks(FilledBackpacks, BestBackpacks).