import sys

gemstones = ["Lapis", "Topaz", "Tourmaline", "Sapphire", "Peridot", "Ruby", "Pearl", "Emerald", "Diamond", "Aquamarine", "Amethyst", "Garnet"]

ponies = []
for pony in sys.stdin.read().splitlines():
    if pony == 'END':
        break

    ponies.append(pony)


royals = []
peasants = []
for pony in ponies:
    words = pony.split()
    gemstone = None
    for word in words:
        if word in gemstones:
            gemstone = word

    if gemstone is None:
        peasants.append(pony)
    else:
        royals.append(pony)


def royal_priority(pony):
    rankings = []
    for word in pony.split():
        if word in gemstones:
            rankings.append(gemstones.index(word))

    return min(rankings)


def sort_royalty(ponies):
    royal_key = [(pony, royal_priority(pony)) for pony in ponies]
    for i in range(len(gemstones)):
        matches = [x[0] for x in royal_key if x[1] == i]
        if len(matches) == 0:
            continue

        print('\n'.join(sort_peasants(matches)))


def sort_peasants(ponies):
    sorted_ponies = sorted(map(lambda x: x.lower(), ponies))
    return sorted(ponies, key=lambda x: sorted_ponies.index(x.lower()))


sort_royalty(royals)
print('\n'.join(sort_peasants(peasants)))
