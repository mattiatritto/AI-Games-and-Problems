% Facts about our problem
domain([red, blue, green]).
regions([wa, nt, q1, nsw, v, sa, t]).



% Utilities
putl(E, [], [E]).
putl(E, [H|TS], [H|TD]):-putl(E, TS, TD).

permute([], []).
permute(List, [H|Perm]) :-
    select(H, List, Rest),
    permute(Rest, Perm).



takeValue([], _, _).
takeValue([HSolution | TSolution], Region, Value):-
    not(HSolution = (Region, Value)),
    takeValue(TSolution, Region, Value).
takeValue([HSolution | _], Region, Value):-
    HSolution = (Region, Value).

differentValues(Region1, Region2, Solution):-
    takeValue(Solution, Region1, Value1),
    takeValue(Solution, Region2, Value2),
    not(Value1 = Value2).
    
checkConstraints(Solution):-
    differentValues(wa, sa, Solution),
    differentValues(wa, nt, Solution),
    differentValues(nt, q1, Solution),
    differentValues(q1, sa, Solution),
    differentValues(q1, nsw, Solution),
    differentValues(sa, v, Solution),
    differentValues(nsw, v, Solution).

pickColor(_, [], Solution, Solution).
pickColor(Region, [HDomain | _], Solution, ReturnedSolution):-
    putl((Region, HDomain), Solution, ReturnedSolution).

pickRegion([], _, Solution, Solution):-checkConstraints(Solution).
pickRegion([HRegions | TRegions], Domain, Solution, ReturnedSolution):-
    permute(Domain, Domain1),
    pickColor(HRegions, Domain1, Solution, Solution1),
    pickRegion(TRegions, Domain1, Solution1, ReturnedSolution).
    
solve(ReturnedSolution):-
    domain(Domain),
    regions(Regions),
    pickRegion(Regions, Domain, [], ReturnedSolution).