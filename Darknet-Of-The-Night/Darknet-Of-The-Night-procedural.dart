import 'dart:math';

// by a.l.e

main() {

  final poem = """
1. Coder Coder, typing bright,
2. in the darkNet of the night.
3. Useful hints that we can hear,
4. you provided them in here.

5. Some are lost and some are found;
6. we talk about the strings that bound.
7. Even when the stack was flowed,
8. you did not refrain, that showed.

9. On what day dare we say thanks?
10. For all the efforts in your ranks?
11. Forever grateful shall we be,
12. to share a great community.

13. Coder, Coder, program bright,
14. in the morning of the light.
15. To all the ideas that you aspire
16. and the codes that you inspire.
  """.trim();

  for (final stanza in poem.split('\n\n')) {
    var shortest = stanza.length;
    var longest = 0;
    for (final line in stanza.split('\n')) {
      final lineLength = line
        .replaceAll(new RegExp(r'^\d+\.\s+'), '')
        .replaceAll(new RegExp(r'\W'), '')
        .length;
      if (lineLength < shortest) {
        shortest = lineLength;
      }
      if (lineLength > longest) {
        longest = lineLength;
      }
    }
    final ratio = shortest / longest * 100;
    print(ratio);
  }

}
