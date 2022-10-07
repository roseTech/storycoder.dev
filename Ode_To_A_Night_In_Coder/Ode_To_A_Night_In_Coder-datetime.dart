void main() {
  final now = DateTime.now();
  var startTime = DateTime(now.year, now.month, now.day, 20, 43, 00);
  var endTime = DateTime(now.year, now.month, now.day, 5, 49, 00)
    .add(const Duration(days: 1));

  var sinceQuarter = startTime.minute % 15;
  if (sinceQuarter > 0) {
    startTime = startTime.add(Duration(minutes: 15 - sinceQuarter));
  }

  int bellCounter = 0;
  for (var time = startTime; time.isBefore(endTime); time = time.add(const Duration(minutes: 15))) {
    if (time.minute == 0) {
      // print('hour: ${time.hour % 12 == 0 ? 12 : time.hour % 12}');
      bellCounter += time.hour % 12 == 0 ? 12 : time.hour % 12;
    } else {
      // print('minute: ${time.minute ~/ 15}');
      bellCounter += time.minute ~/ 15;
    }
  }

  print(bellCounter);
}
