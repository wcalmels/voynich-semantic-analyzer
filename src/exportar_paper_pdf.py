import markdown2
from weasyprint import HTML

INPUT_MD = "paper_v2.md"
OUTPUT_PDF = "paper_v2.pdf"

print("Leyendo paper markdown...")

with open(INPUT_MD, "r", encoding="utf-8") as f:
    markdown_text = f.read()

html = markdown2.markdown(markdown_text)

html_completo = f"""
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 50px;
    line-height: 1.6;
}}
h1, h2, h3 {{
    color: #222;
}}
table {{
    border-collapse: collapse;
    width: 100%;
}}
th, td {{
    border: 1px solid #999;
    padding: 8px;
}}
</style>
</head>
<body>
{html}
</body>
</html>
"""

print("Generando PDF...")

HTML(string=html_completo).write_pdf(OUTPUT_PDF)

print(f"PDF generado: {OUTPUT_PDF}")