import markdown
from weasyprint import HTML

# 读取 Markdown 文件
with open('your_file.md', 'r') as f:
    md_content = f.read()

# 将 Markdown 转换为 HTML
html_content = markdown.markdown(md_content)

# 将 HTML 转换为 PDF
HTML(string=html_content).write_pdf('output.pdf')

print("abc")