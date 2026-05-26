import markdown2

INPUT_MD = "paper_v3.md"
OUTPUT_HTML = "paper_v3.html"

with open(INPUT_MD, "r", encoding="utf-8") as f:
    markdown_text = f.read()

html = markdown2.markdown(
    markdown_text,
    extras=["tables", "fenced-code-blocks"]
)

html_final = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Voynich Semantic Framework</title>

<style>

body {{
    font-family: Georgia, serif;
    max-width: 1000px;
    margin: 60px auto;
    line-height: 1.75;
    color: #222;
}}

h1 {{
    font-size: 34px;
}}

h2 {{
    margin-top: 40px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 8px;
}}

table {{
    border-collapse: collapse;
    width: 100%;
    margin-top: 20px;
}}

th, td {{
    border: 1px solid #999;
    padding: 10px;
}}

code {{
    background: #eee;
    padding: 2px 5px;
}}

pre {{
    background: #f4f4f4;
    padding: 14px;
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
    f.write(html_final)

print(f"HTML generado: {OUTPUT_HTML}")