repeat([H1, H2|_]) :-
  H1 = H2.
repeat([_|T]) :- repeat(T).

incr([]).
incr([_]).
incr([H1, H2|T]) :-
  H1 =< H2, incr([H2|T]).

good(Z, 1) :-
  repeat(Z), incr(Z).
good(Z, 2) :-
  clearRepeat(Z, 0), incr(Z).

clearRepeat([H1, H2, H3|_], 0) :-
  H1 = H2, H2 \= H3.
clearRepeat([H1, H2, H3, H4|_], _) :-
  H1 \= H2, H2 = H3, H3 \= H4.
clearRepeat([H1, H2, H3], _) :-
  H1 \= H2, H2 = H3.
clearRepeat([_|T], I) :-
  clearRepeat(T, I + 1).

candidate(X, Question) :-
  between(356261, 846303, X),
  number_string(X, Y), string_codes(Y, Z),
  good(Z, Question).

main :-
  aggregate(count, X, candidate(X, 1), N1),
  aggregate(count, X, candidate(X, 2), N2),
  writeln(N1),
  writeln(N2).
