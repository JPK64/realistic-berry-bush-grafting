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
	["sparselyclusteredberries", "denselyclusteredberries"]
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

def trait_merges(traits, pair):
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

def merges(traits):
	result = [[[], []]]
	for pair in pairs:
		result = [
			[
				first + ([] if f is None else [f]),
				second + ([] if s is None else [s])
			] for [first, second] in result
			for [f, s] in trait_merges(traits, pair)
		]

	return result

from os import makedirs
from template import format_barrel, format_grid, format_array

combinations = combinations()

makedirs("barrel", exist_ok=True)
with open("barrel/fruitingbushcutting.json", "w", encoding="utf-8") as f:
	f.write(format_array(
		format_barrel(traits)
		for traits in combinations
	))

makedirs("grid/graftedcutting", exist_ok=True)
for name in families:
	with open(f"grid/graftedcutting/{name}.json", "w", encoding="utf-8") as f:
		f.write(format_array(
			format_grid(families[name], base, graftedon, merged)
			for merged in combinations
			for [base, graftedon] in merges(merged)
			if base != merged and graftedon != merged
		))


