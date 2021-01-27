from dataclasses import dataclass, field
from typing import List

from jinja2 import Environment, FileSystemLoader

@dataclass
class Node:
    name: str
    children: List['Node'] = field(default_factory=lambda: [])
    href: str = ''

TEST_TREE = [Node('p1', [Node('p11', [Node('c111', href='c111')])]), Node('p2', [Node('c21', href='c21')]), Node('c2', href='c2')]

def contents(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    env = Environment(loader = FileSystemLoader(searchpath="."))
    template = env.get_template('docs-index.html')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(
            template.render(
                css=contents('styles/_site/ui/css/styles.css'),
                tree=TEST_TREE,
                )
            )
