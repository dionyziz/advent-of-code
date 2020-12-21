from collections import Counter, defaultdict

with open('in.txt') as f:
  lines = f.read().splitlines()

allergen_to_ingsets = defaultdict(list)
ingredient_count = Counter()

for line in lines:
  ingredients, allergens = line.split(' (contains ')
  ingredients = set(ingredients.split(' '))
  ingredient_count += Counter(ingredients)
  allergens = allergens[:-1].split(', ')
  for allergen in allergens:
    allergen_to_ingsets[allergen].append(ingredients)

solution = {}

while True:
  for allergen, setlist in allergen_to_ingsets.items():
    intersection = set.intersection(*setlist)
    if len(intersection) == 1:
      ingredient = intersection.pop()
      solution[allergen] = ingredient
      for _, setlist in allergen_to_ingsets.items():
        for ingredientset in setlist:
          ingredientset.discard(ingredient)
      break
  else:
    break

good_ingredients = set.union(*[set.union(*ingsets) for ingsets in allergen_to_ingsets.values()])
cnt = 0
for ingredient in good_ingredients:
  cnt += ingredient_count[ingredient]
print(cnt)

solution = sorted(solution.items())
print(','.join([ingredient for _, ingredient in solution]))
