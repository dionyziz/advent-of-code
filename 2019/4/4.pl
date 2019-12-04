repeat([H1, H2|_]) :-
  H1 = H2.
repeat([_|T]) :- repeat(T).

incr([]).
incr([_]).
incr([H1, H2|T]) :-
  H1 =< H2, incr([H2|T]).

good(X) :-
  string_codes(X, Y), repeat(Y), incr(Y).

candidate(X) :-
  between(356261, 846303, X), number_string(X, Y), good(Y).

main :-
  aggregate(count, X, candidate(X), N),
  write(N).
