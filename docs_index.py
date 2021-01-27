from jinja2 import Environment, FileSystemLoader

def contents(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    env = Environment(loader = FileSystemLoader(searchpath="."))
    template = env.get_template('docs-index.html')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(template.render(css=contents('styles/_site/ui/css/styles.css')))
