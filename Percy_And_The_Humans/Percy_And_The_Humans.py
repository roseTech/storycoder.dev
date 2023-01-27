def all_explorers_full(explorers):
    for explorer in explorers:
        for size, pieces in explorer.items():
            if pieces < 117:
                return False
    return True

fishes = {'big': 19, 'medium': 11, 'small': 5}
# explorers = [[0, 0, 0], 0, 0, 0, 0, 0, 0, 0]
# https://stackoverflow.com/questions/2397754/how-can-i-create-an-array-list-of-dictionaries-in-python
explorers  = [{'big': 0, 'medium': 0, 'small': 0} for i in range(8)]
# print(explorers)

current_explorer = 0

# TODO: count the number of fishes of each type or do the sum at then and divide by n of pieces
while not all_explorers_full(explorers):    
    for size, pieces in fishes.items():
        # print(size, pieces)
        for piece in range(pieces):
            explorers[current_explorer][size] += 1
            # TODO: check if all_explorers are full
            current_explorer = (current_explorer + 1) % 8
            # print(i)
print(explorers)
# big fish 117 / 19  = 6.15...

totals = {'big': 0, 'medium':0, 'small': 0}
for explorer in explorers:
    for size, pieces in explorer.items():
        totals[size] += pieces

print(totals)
for size, total in totals.items():
    print(size, total / fishes[size])
