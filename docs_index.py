import os
from pathlib import PurePath, PurePosixPath
import sys

import dpath.util
from jinja2 import Environment, FileSystemLoader

TEST_TREE = {
    'Dimensional Models': {
        'Model Category 1': {
            'Model Site 1-1': 'm1-1',
        }
    },
    'Table Discovery (Read-Only)': {
        'Source DB 1': 's1',
        'Source DB 2': 's2',
    },
    'Top-Level Model': 'mt',
}

def contents(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    root = PurePath(sys.argv[1] if len(sys.argv) > 1 else '.')
    tree = {}
    for dirpath, dirnames, filenames in os.walk(root):
        if 'dbt_project.yml' in filenames and 'target' in dirnames:
            relative_path = PurePath(dirpath).relative_to(root)
            url = PurePosixPath(relative_path, 'target', 'index.html')
            print(f'Found dbt project: {url}')
            dpath.util.new(tree, relative_path.parts, str(url))
            del dirnames[:] # Don't look for dbt projects inside dbt projects
    print(tree)
    env = Environment(loader = FileSystemLoader(searchpath=sys.path[0]))
    template = env.get_template('docs-index.html')
    with open(PurePath(root, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(
            template.render(
                css=contents('styles/_site/ui/css/styles.css'),
                tree=tree,
                )
            )
