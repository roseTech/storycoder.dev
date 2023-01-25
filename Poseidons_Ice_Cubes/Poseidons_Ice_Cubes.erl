
main([]) ->
  TempSeidon = 11.475 + 14.0,
  TempCelsius = TempSeidon / 1.37,
  io:fwrite("~.2f~n", [TempCelsius]).
