void main() {
  const iterations = 10;
  const p = 7;
  final sum =
      List.generate(iterations, (i) => p * (i + 1)).reduce((sum, e) => sum + e);
  print(sum);
}
