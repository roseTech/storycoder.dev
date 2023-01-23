main([]) ->
  DaysBetweenAFullMoon = 29,
  NumberOfWaterLilies = math:pow(2.0, DaysBetweenAFullMoon),
  io:fwrite("~f~n", [NumberOfWaterLilies]).
