# dbt-docs-index
Generates an index of multiple dbt documentation sites

## Prep
After cloning this repository, run:

```bash
git submodule update --init --recursive
```

## Docker Usage

```
docker build -t dbt_index_builder .
docker run --rm -v [ROOT DIRECTORY]:/projects dbt_index_builder /projects
```

generates a file index.html in the root directory with a directory listing of your dbt projects:

![menu of dbt docs sites](/etc/screenshot.png?raw=true "dbt-docs-index screenshot")

## Native Usage

Do everything like it's done in the Dockerfile:
 * Install Ruby, bundler, Jekyll.
 * Generate `styles.css`
 * Install Python dependencies

Then run:

```
python docs_index.py [ROOT DIRECTORY]
```
