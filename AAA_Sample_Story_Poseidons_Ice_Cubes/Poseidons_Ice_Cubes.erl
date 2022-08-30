-module(main). 
-export([start/0]). 

start() -> 
  TempSeidon = 11.475 + 14.0, 
  TempCelsius = TempSeidon / 1.37, 
  io:fwrite("~.2f", [TempCelsius]).
