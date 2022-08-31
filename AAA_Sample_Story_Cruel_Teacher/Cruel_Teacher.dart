//approach for advanced learners
void main() {
  const iterations = 10;
  const p = 7;
  final sum =
      List.generate(iterations, (i) => p * (i + 1)).reduce((sum, e) => sum + e);
  print(sum);
}


// appraoch for beginners
void main() {
  const iterations = 10;
  const p = 7;
  var sum = 0;
  for (int i = 1; i <= iterations; i++) {
    final num = p * i;
    sum += num;
    print ('$i $num $sum');
  }
}


