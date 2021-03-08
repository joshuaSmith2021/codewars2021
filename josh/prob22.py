import re
import sys

categories = []
ingredients = {}

conversions = {
    'WET': [
        ('gallon', 4),
        ('quart', 2),
        ('pint', 2),
        ('cup', 8),
        ('ounce', 2),
        ('tablespoon', 3),
        ('teaspoon', 1)
    ], 'DRY': [
        ('cup', 16),
        ('tablespoon', 3),
        ('teaspoon', 1)
    ], 'WEIGHTED': [
        ('pound', 16),
        ('ounce', 1)
    ]
}

def convert_unit(cat, quan, unit):
    conv = conversions[cat]
    start = [x[0] for x in conv].index(unit)
    current_quan = quan
    for i in range(start)[::-1]:
        current_quan /= conv[i][1]

    units = [(conv[0][0], current_quan)]
    for i, x in enumerate(conv):
        mult = x[1]
        if mult == 1:
            break

        unit_name = conv[i + 1][0]
        current_quan *= mult
        units.append((unit_name, current_quan))

    for x in units:
        if x[1] >= 1:
            return x

    return units[-1]

lines = sys.stdin.read().splitlines()

multiply = float(lines[0])

key = None
for line in lines[1:]:
    match = re.match(r'(?P<key>WET|DRY|WEIGHTED) INGREDIENTS', line)
    if match:
        key = match.group(1)
        categories.append(key)
        ingredients[key] = []
        continue

    quan, unit, name = line.split()
    quan = float(quan)
    ingredients[key].append((quan * multiply, unit, name))

for category in categories:
    ingreds = ingredients[category]
    print('{0} INGREDIENTS'.format(category))
    for ingred in ingreds:
        quan, unit, name = ingred
        new_unit, new_quan = convert_unit(category, quan, unit)
        print('{0:.2f} {1} {2}'.format(new_quan, new_unit, name))