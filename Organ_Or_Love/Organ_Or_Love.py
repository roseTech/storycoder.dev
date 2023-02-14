from statistics import median

pearls = []

for i in range(1, n_pearls + 1):
    if i in [56, 63, 72]:
        pearls.append(4)
    elif i % 7 == 0:
        pearls.append(12)
    elif i % 8 == 0:
        pearls.append(20)
    elif i % 9 == 0:
        pearls.append(8)
    else:
        pearls.append(6)

types_and_faces = {
    'pearls_of_love': sum(pearls[0:15]),
    'pearls_of_trust': sum(pearls[15:32]),
    'pearls_of_joy': sum(pearls[32:46]),
    'pearls_of_feelings': sum(pearls[47:65]),
    'pearls_of_hope': sum(pearls[65:76]),
    'pearls_of_romance': sum(pearls[76:86]),
    'pearls_of_strength': sum(pearls[86:101]),
}

print('max', max(types_and_faces, key=types_and_faces.get))
print('min', min(types_and_faces, key=types_and_faces.get))

print('###', sorted(types_and_faces, key=types_and_faces.get))
# print (types_and_faces)

print('median value', median(types_and_faces.values()))

labels = sorted(types_and_faces, key=types_and_faces.get)
print('median pearls', labels[(len(labels) - 1) // 2])
