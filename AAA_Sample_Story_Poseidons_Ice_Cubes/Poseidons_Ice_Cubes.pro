:- initialization(main).

main :-
  TempSeidon is 11.475 + 14.0,
  TempCelsius is TempSeidon / 1.37,
  format('~2f~n', [TempCelsius]),
  halt.
