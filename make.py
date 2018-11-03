#!/usr/bin/env python3

import json
import pathlib


def div(id, content):
    return '<div id="{}">{}</div>'.format(id, content)


def div_class(clas, content):
    return '<div class="{}">{}</div>'.format(clas, content)


def p(content):
    return "<p>{}</p>".format(content)


def ingredients(id, ing):
    return "\n".join(
        ['<table id="{}">'.format(id)]
        + ["<tr><th>" + i + "</th></tr>" for i in ing]
        + ["</table>"]
    )


def img(src):
    assert pathlib.Path(src).exists()
    return '<img src="{}"/>'.format(src)


def section(id, content):
    return '<section id="{}">\n{}\n</section>'.format(
        id, "\n".join("  " + c for c in content.split("\n"))
    )


def render_portion(id, title, paragraphs):
    return div(
        "",
        div_class("name-header", title)
        + "\n"
        + "\n".join(p(par) for par in paragraphs),
    )


def render_recipe(recipe):
    return section(
        "title",
        "\n".join(
            [
                div("title", recipe["title"]),
                div("author", "From the kitchen of " + recipe["author"]),
                div("serves", recipe["serves"]),
                div("prep_minutes", recipe["prep_minutes"]),
                ingredients("ingredients", recipe["ingredients"]),
                render_portion("steps", "Steps", recipe["steps"]),
                render_portion("notes", "Notes", recipe["notes"]) if False else "",
            ]
        ),
    )


def head():
    return '<link type="text/css" href="style.css"/>'


recipes = json.load(open("recipes.json"))


print("\n\n".join([head()] + [render_recipe(recipe) for recipe in recipes]))
