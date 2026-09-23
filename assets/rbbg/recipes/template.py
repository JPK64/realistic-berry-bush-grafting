barrel_template = """	{{
		"code": "fruitingbushcutting",
		"sealHours": 48,
		"ingredients": [
			{{
				"type": "item",
				"code": "game:weaktanninportion",
				"litres": 0.5,
				"consumeLitres": 0.5
			}},
			{{
				"type": "block",
				"code": "graftedcutting-*",
				"quantity": 1,
				"name": "fruit"{0}
			}}
		],
		"output": {{
			"type": "block",
			"code": "game:fruitingbushcutting-{{fruit}}-free"{1},
			"quantity": 1
		}}
	}}"""

grid_template = """	{{
		"ingredientPattern": "NG,KB",
		"ingredients": {{
			"K": {{
				"type": "item",
				"tags": [
					"tool-knife"
				],
				"isTool": true
			}},
			"B": {{
				"type": "block",
				"code": "game:fruitingbushcutting-{{base}}-free"{1}
			}},
			"G": {{
				"type": "block",
				"code": "game:fruitingbushcutting-{{graftedon}}-free"{2}
			}},
			"N": {{
				"type": "block",
				"code": "game:{{nutrient}}-*"
			}}
		}},
		"allowedVariants": {{
			"nutrient": [
				"aquatic-kelp",
				"seaweed"
			],
			"graftedon": [
{0}
			],
			"base": [
{0}
			]
		}},
		"width": 2,
		"height": 2,
		"recipeGroup": 1,
		"output": {{
			"type": "block",
			"code": "graftedcutting-{{graftedon}}"{3}
		}},
		"quantity": 1
	}}"""

family_template = '				"{0}"'

input_template = """,
				"attributes": {{
					"traits": "{0}"
				}}"""
output_template = """,
			"attributes": {{
				"traits": "{0}"
			}}"""

array_template = """[
{0}
]
"""
array_separator = """,
"""

if not __debug__:
	from re import sub
	whitespace = r"\s+"

	barrel_template = sub(whitespace, '', barrel_template)
	grid_template = sub(whitespace, '', grid_template)
	family_template = sub(whitespace, '', family_template)

	input_template = sub(whitespace, '', input_template)
	output_template = sub(whitespace, '', output_template)

	array_template = sub(whitespace, '', array_template)
	array_separator = sub(whitespace, '', array_separator)

def format_template(traits, empty, nonempty):
	return empty if len(traits) == 0 else nonempty.format(",".join(traits))

def format_barrel(traits):
	return barrel_template.format(
		format_template(traits, "", input_template),
		format_template(traits, "", output_template)
	)

def format_grid(family, base, graftedon, merged):
	return grid_template.format(
		array_separator.join(family_template.format(member) for member in family),
		format_template(base, "", input_template),
		format_template(graftedon, "", input_template),
		format_template(merged, "", output_template)
	)

def format_array(array):
	return array_template.format(array_separator.join(array))
