barrel_template = """	{{
		"code": "fruitingbushcutting",
		"sealHours": 48,
		"ingredients": [
			{{
				"type": "item",
				"code": "game:weaktanninportion",
				"litres": 1,
				"consumeLitres": 1
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
				"code": "game:fruitingbushcutting-{0}-free"{1}
			}},
			"G": {{
				"type": "block",
				"code": "game:fruitingbushcutting-{2}-free"{3}
			}},
			"N": {{
				"type": "block",
				"code": "game:seaweed-top"
			}}
		}}{4},
		"width": 2,
		"height": 2,
		"output": {{
			"type": "block",
			"code": "graftedcutting-{2}"{5}
		}}
	}}"""

variants_template = """,
		"allowedVariants": {{
			"base": [
{0}
			],
			"graftedon": [
{0}
			]
		}}"""
variant_template = '				"{0}"'

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
]"""
array_separator = """,
"""

if not __debug__:
	from re import sub
	whitespace = r"\s+"

	barrel_template = sub(whitespace, '', barrel_template)
	grid_template = sub(whitespace, '', grid_template)

	variants_template = sub(whitespace, '', variants_template)
	variant_template = sub(whitespace, '', variant_template)

	input_template = sub(whitespace, '', input_template)
	output_template = sub(whitespace, '', output_template)

	array_template = sub(whitespace, '', array_template)
	array_separator = sub(whitespace, '', array_separator)

def format_trait_template(traits, empty, nonempty):
	return empty if len(traits) == 0 else nonempty.format(",".join(traits))

def format_variant_template(variants, single, multi):
	return single if len(variants) == 1 else multi

def format_barrel(traits):
	return barrel_template.format(
		format_trait_template(traits, "", input_template),
		format_trait_template(traits, "", output_template)
	)

def format_grid(variants, base, graftedon, merged):
	return grid_template.format(
		format_variant_template(variants, variants[0], "{base}"),
		format_trait_template(base, "", input_template),
		format_variant_template(variants, variants[0], "{graftedon}"),
		format_trait_template(graftedon, "", input_template),
		format_variant_template(variants, "", variants_template.format(array_separator.join(variant_template.format(variant) for variant in variants))),
		format_trait_template(merged, "", output_template)
	)

def format_array(array):
	return array_template.format(array_separator.join(array))
