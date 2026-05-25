import markdown2

INPUT_MD = "paper_v2.md"
OUTPUT_HTML = "paper_v2.html"

with open(INPUT_MD, "r", encoding="utf-8") as f:
    markdown_text = f.read()

html = markdown2.markdown(
    markdown_text,
    extras=["tables", "fenced-code-blocks"]
)

html_completo = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Voynich Semantic Framework</title>
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 900px;
    margin: 50px auto;
    line-height: 1.65;
    color: #222;
}}
h1, h2, h3 {{
    color: #111;
}}
table {{
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}}
th, td {{
    border: 1px solid #999;
    padding: 8px;
}}
code {{
    background: #eee;
    padding: 2px 4px;
}}
pre {{
    background: #eee;
    padding: 12px;
    overflow-x: auto;
}}
</style>
</head>
<body>
{html}
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_completo)

print(f"HTML generado: {OUTPUT_HTML}")