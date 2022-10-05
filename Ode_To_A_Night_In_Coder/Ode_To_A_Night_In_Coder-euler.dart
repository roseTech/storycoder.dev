void main() {
  // 9:00 - 12:00: s =( b - α + 1) * (a + b) / 2
  int hour_bells = (12 - 9 + 1) * (9 + 12) ~/ 2;
  // 1:00 - 5:00: S = n * (n + 1) / 2
  hour_bells += 5 * (5 + 1) ~/ 2;

  // 8:45 + (9 - 12)(:15, :30, :45) + (0:00 - 6:00)(:15, :30, :45)
  int quarter_bells_per_hour = 1 + 2 + 3;
  int quarter_bells = 3 + (12 - 9) * (quarter_bells_per_hour) + 6 * quarter_bells_per_hour;

  print(hour_bells + quarter_bells);
}
