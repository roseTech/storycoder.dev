# 1. define a distance and print it
# 2. define a list of streets
# 3. go through each street in the list of streets
# 4. find a way to convert the letters to the values given above
# 5. go through each letter in each street names
# 6. sum the values and get the total distance

streets = [
    'Egame Street',
    'Branch Road',
    'DartLang Lane',
    'Azerty Avenue',
    'Pixel Way',
    'Less than or equal Street',
    'OpenSourcePath',
    'Readme Road',
    'Frame Work Way',
    'Element Lane',
    'Tab Street',
    'Night Mode Ave',
    'Julia Lang Lane',
    'Stack Overflowed Way',
    'Roaming Steet',
]

distance = 0

letters = {}
abc = 'abcdefghijklmnopqrstuvwxyz'
i = 1
for a in abc:
    letters[a] = i
    i+=1
# print(letters)

# 'a' -> 97
# print(ord('b') - 96)

letters_heard = ''

for street in streets:
    # print(street)
    letters_heard += street[1]
    for letter in street.lower():
        # print(letter)
        if letter == ' ':
            continue
        distance += (ord(letter) - 96) * 10

print(distance)
print(letters_heard)
