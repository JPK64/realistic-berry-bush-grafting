from re import sub, DOTALL
from sys import argv
from minify_html import minify

with open(argv[1]) as f:
	content = f.read()

content = sub(r' dir="auto"|<br>', "", content, flags=DOTALL)
content = sub(r'<p>\s*</p>', "", content, flags=DOTALL)
content = sub(
r"<details>\s*<summary>(.*?)</summary>\s*(.*?)\s*</details>", 
r'''<div class="spoiler">
	<div class="spoiler-toggle">\1</div>
	<div class="spoiler-text">
		\2
	</div>
</div>''',
content,
flags=DOTALL)

content = minify(content, remove_processing_instructions=True)

with open(argv[1], "w", encoding="utf-8") as f:
	f.write(content)