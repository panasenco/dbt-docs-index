# dbt-docs-index
Generates an index of multiple dbt documentation sites

## Build prerequisite css files
After cloning this repository, run:

```bash
git submodule update --init --recursive
```

You'll also need to install jekyll and bundler if you don't already have them:
```bash
gem install jekyll bundler
```

To build the css files:

```bash
cd styles
bundle exec jekyll build
cd -
```

## Usage

```
python docs_index.py [ROOT DIRECTORY]
```

generates a file index.html in the root directory with a directory listing of your dbt projects:

![menu of dbt docs sites](/etc/screenshot.png?raw=true "dbt-docs-index screenshot")
