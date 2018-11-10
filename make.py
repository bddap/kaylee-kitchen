#!/usr/bin/env python3

import json
import pathlib
from jinja2 import Template


def title_to_name(title):
    return title.replace(" ", "-").lower() + ".html"


def dump_index(recipes):
    index = ul(
        anchor(title_to_name(recipe["title"]), recipe["title"]) for recipe in recipes
    )
    open("docs/index.html", "w").write(index)


recipes = json.load(open("recipes.json"))
recipe_template = Template(open("recipe.template.html").read())
index_template = Template(open("index.template.html").read())

for r in recipes:
    r["name"] = title_to_name(r["title"])

open("docs/index.html", "w").write(index_template.render(recipes=recipes))

for recipe in recipes:
    out = open("docs/" + recipe["name"], "w")
    out.write(recipe_template.render(recipe=recipe))
