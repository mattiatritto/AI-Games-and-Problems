% Maze solver



% Facts about the maze

walls([(4,3), (2,2), (5,1), (1,3)]).

start((1, 1)).
exit_maze((5, 5)).
max_time(8).



% The possible moves are 4

move(up, (X,Y), (X1, Y)):-X1 is X-1.
move(down, (X,Y), (X1, Y)):-X1 is X + 1.
move(left, (X,Y), (X, Y1)):-Y1 is Y -1.
move(right, (X,Y), (X, Y1)):-Y1 is Y + 1.



is_in_maze((X,Y)):-X > 0, Y > 0, X =< 5, Y =< 5.
valid((X, Y)):-is_in_maze((X,Y)), walls(Walls), not(member2((X,Y), Walls)).



% List utilities

member2(E, [E|_]).
member2(E, [_|T]):-member(E, T).

putl(E, [], [E]):-!.
putl(E, [H | TS], [H | TD]):-putl(E, TS, TD).



main():-
    start(Start),
    exit_maze(Exit),
    max_time(MaxTime),
    find_path(Start, Exit, 0, MaxTime, [], RetPath),
    draw_maze(RetPath).

find_path((Xe, Ye), (Xe, Ye), Time, _, Path, RetPath):-putl((Xe, Ye), Path, RetPath),write('\nTime used to solve the maze: '),write(Time),write('\n').
find_path((X,Y), Exit, Time, MaxTime, Path, RetPath):-
    Time < MaxTime,
    move(_, (X, Y), (X1, Y1)),
    valid((X1, Y1)),
    not(member2((X1, Y1), Path)),
    putl((X1, Y1), Path, Path1),
    Time1 is Time + 1,
    find_path((X1, Y1), Exit, Time1, MaxTime, Path1, RetPath).



% Written with ChatGPT, just for debugging purposes

draw_maze(Path) :-
    findall((X, Y), (between(1, 5, X), between(1, 5, Y)), Cells),
    draw_cells(Cells, Path).
draw_cells([], _).
draw_cells([(X, Y) | Rest], Path) :-
    (member((X, Y), Path) -> write('*'); 
    walls(Walls), member((X, Y), Walls) -> write('|');
    start((X, Y)) -> write('S');
    exit_maze((X, Y)) -> write('E');
    write('.')),
    (Y = 5 -> nl; true),
    draw_cells(Rest, Path).