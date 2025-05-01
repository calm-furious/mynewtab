import markdown
import os
from datetime import datetime
from jinja2 import Template

def main():
    # Create dist directory
    os.makedirs('dist', exist_ok=True)

    # Read and convert markdown
    with open('src/links.md', 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['tables'])

    # Read template
    with open('src/template.html', 'r', encoding='utf-8') as f:
        template = Template(f.read())

    # Render template
    rendered = template.render(
        content=html_content,
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    )

    # Write output
    with open('dist/index.html', 'w', encoding='utf-8') as f:
        f.write(rendered)

    # Copy CSS
    with open('src/style.css', 'r', encoding='utf-8') as f:
        css = f.read()
    with open('dist/style.css', 'w', encoding='utf-8') as f:
        f.write(css)

if name == 'main':
    main()