families = {
	"currants": ["blackcurrant", "redcurrant", "whitecurrant"],
	"brambles": ["blackberry", "cloudberry", "raspberry"],
	"heathers": ["blueberry", "cranberry"],
	"beautyberry": ["beautyberry"],
	"strawberry": ["strawberry"]
}

pairs = [
	# Yield
	["shybearer", "heavybearer"],
	# Ripe Duration
	["thinskinnedfruit", "thickskinnedfruit"],
	# Nutrient Uptake
	["weakrooted", "strongrooted"],
	# Harvest Speed
	["weakclusteredberries", "strongclusteredberries"]
]

def combinations():
	result = [[]]
	for [negative, positive] in pairs:
		result = [
			combination + ([] if trait is None else [trait])
			for combination in result
			for trait in [negative, None, positive]
		]

	return result

def combinations_for_trait(traits, pair):
	[negative, positive] = pair
	return [
		[negative, negative],
		[negative, None],
		[None, negative]
	] if negative in traits else [
		[positive, None],
		[None, positive],
		[positive, positive]
	] if positive in traits else [
		[positive, negative],
		[None, None],
		[negative, positive]
	]

def combinations_for_traits(traits):
	result = [[[], []]]
	for pair in pairs:
		result = [
			[
				rootstock + ([] if r is None else [r]),
				scion + ([] if s is None else [s])
			] for [rootstock, scion] in result
			for [r, s] in combinations_for_trait(traits, pair)
		]

	return result

from os import makedirs
from pathlib import Path

from template import format_barrel, format_grid, format_array

recipes = Path(__file__).parent.parent / "assets/rbbg/recipes"
combinations = combinations()

makedirs(f"{recipes}/barrel", exist_ok=True)
with open(f"{recipes}/barrel/fruitingbushcutting.json", "w", encoding="utf-8") as f:
	f.write(format_array(
		format_barrel(traits)
		for traits in combinations
	))

makedirs(f"{recipes}/grid/graftedcutting", exist_ok=True)
for name, family in families.items():
	with open(f"{recipes}/grid/graftedcutting/{name}.json", "w", encoding="utf-8") as f:
		f.write(format_array(
			format_grid(family, rootstock, scion, grafted)
			for grafted in combinations
			for [rootstock, scion] in combinations_for_traits(grafted)
			if rootstock != grafted and scion != grafted
		))
