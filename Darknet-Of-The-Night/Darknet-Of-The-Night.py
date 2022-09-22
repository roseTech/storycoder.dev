import re

# by a.l.e

poem = '''
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
'''.strip()

def min_and_max_line_lengths(lines):
    min = len(lines[0])
    max = 0
    for line in lines:
        n = len(re.sub(r'\W', '', re.sub(r'^\d+\.\s+', '', line)))
        if n < min:
            min = n
        if n > max:
            max = n
    return min, max

for paragraph in poem.split('\n\n'):
    min, max = min_and_max_line_lengths(paragraph.split('\n'))
    print(100 * min / max)
