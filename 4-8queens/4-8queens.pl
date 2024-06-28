domain([1, 2, 3, 4, 5, 6, 7, 8]).



% Utilities
putl(E, [], [E]).
putl(E, [H|TS], [H|TD]):-putl(E, TS, TD).

all_different([]).
all_different([H|T]):-
    different(H, T),
    all_different(T).

different(_, []):-!.
different(E, [H|T]):-
    not(E=H),
    different(E, T).

permute([], []).
permute(List, [H|Perm]) :-
    select(H, List, Rest),
    permute(Rest, Perm).




all_on_different_diagonals(List):-
    pairs_rows_columns([1, 2, 3, 4, 5, 6, 7, 8], List, Pairs),
    extract_diagonals(Pairs, MainDiagonals, AntiDiagonals),
    all_different(MainDiagonals),
    all_different(AntiDiagonals).

pairs_rows_columns([], [], []).
pairs_rows_columns([RH|RT], [CH|CT], [(RH,CH)|Pairs]) :-
    pairs_rows_columns(RT, CT, Pairs).

extract_diagonals([], [], []).
extract_diagonals([(R, C)|TPairs], [HMain|TMains], [HAnti|TAntis]) :-
    HMain is R - C,
    HAnti is R + C,
    extract_diagonals(TPairs, TMains, TAntis).

queens(State, [], State):-all_on_different_diagonals(State).
queens(State, [HDomain|TDomain], Final_state):-
    putl(HDomain, State, State2),
    all_different(State2),
    queens(State2, TDomain, Final_state).

solve(Final_state):-
    domain(Domain),
    permute(Domain, NewDomain),
    queens([], NewDomain, Final_state).