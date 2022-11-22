input = """
Princess Salad: 1 piece
Lady Purple: 2 pieces
Madame Pumpkin: 3 pieces
Mister Onion: ….
Knight Tomato: …
Count Leek: …
Mister Carrot: …
Sir Potato: …
Knight Tomato: 1 piece
Sir Potato: 2 pieces
Lady Purple: 3 pieces
Princess Salad: …
Count Leek: …
Madame Pumpkin: …
Mister Carrot: …
Mister Onion: ….
Count Leek: 1 piece
Mister Onion: 2 pieces
Knight Tomato: 3 pieces
Mister Carrot: …
Lady Purple: …
Sir Potato: …
Madame Pumpkin: …
Princess Salad: …
"""

veggies = {}

order = 1
for line in input.strip().split('\n'):
    veggie = line.split(':')[0]
    # print(veggie, order)
    if veggie in veggies:
        veggies[veggie] += order
    else:
        veggies[veggie] = order
    if order < 8:
        order += 1
    else:
        order = 1

# How do I sort a dictionary by value? cc-by-sa Devin Jeanpierre <https://stackoverflow.com/a/613218>
print(dict(sorted(veggies.items(), key=lambda item: item[1])))
