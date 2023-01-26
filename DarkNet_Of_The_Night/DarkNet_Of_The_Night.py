import re

# by a.l.e
# ArT was HiR

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

def get_line_length_difference(lines):
    min = 0
    max = 0
    for line in lines:
        n = len(re.sub(r'\W', '', re.sub(r'^\d+\.\s+', '', line)))
        if n < min or min == 0:
            min = n
        if n > max or max == 0:
            max = n
    return max - min

results=[]

for paragraph in poem.split('\n\n'):
    diff=(get_line_length_difference(paragraph.split('\n')))
    results.append(diff)
    
print(results)

index_min = min(range(len(results)), key=results.__getitem__) #find index of smallest value

print(f"Answer: {index_min+1}") #+1 because list index are counted from 0

