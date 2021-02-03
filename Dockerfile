# Build the file styles.css using Jekyll

FROM ruby AS css_builder

WORKDIR /tmp/styles

COPY Gemfile .

RUN gem install bundler && \
    bundle install

COPY styles .

RUN bundle exec jekyll build


# Build the actual dbt-docs-index image

FROM python:3.8-buster

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY --from=css_builder /tmp/styles/_site styles/_site

COPY . .

ENTRYPOINT ["python", "docs_index.py"]
