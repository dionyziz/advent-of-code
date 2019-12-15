import math

with open('14.txt') as f:
    lines = f.read().split('\n')

def parse_material(str):
    amount, ingredient = str.split(' ')
    return int(amount), ingredient

nodes = {'ORE': {'make_amount': 1,
                 'ingredients': []}}

for line in lines[:-1]:
    src, dst = line.split(' => ')
    amount, dst = parse_material(dst)
    ingredients = list(map(parse_material, src.split(', ')))
    nodes[dst] = {'make_amount': amount,
                  'ingredients': ingredients}

def ore_needed(fuel):
    for node in nodes:
        nodes[node]['used'] = nodes[node]['capacity'] = 0

    nodes['FUEL']['used'] = fuel
    q = ['FUEL']
    while len(q):
        node = nodes[q.pop()]
        if node['used'] > node['capacity']:
            need_to_make = node['used'] - node['capacity']
            reactions = math.ceil(need_to_make / node['make_amount'])
            node['capacity'] += node['make_amount'] * reactions
            for ingredient_amount, ingredient in node['ingredients']:
                nodes[ingredient]['used'] += ingredient_amount * reactions
                q.append(ingredient)

    return nodes['ORE']['capacity']

print(ore_needed(1))

ORE_LIMIT = 1000000000000
lo = 0 # inclusive
hi = ORE_LIMIT + 1 # exclusive
while hi > lo + 1:
    mid = (hi + lo) // 2
    if ore_needed(mid) > ORE_LIMIT:
        hi = mid
    else:
        lo = mid

print(lo)
