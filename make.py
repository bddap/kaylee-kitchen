#!/usr/bin/env python3

import json
import pathlib


def div(id, content):
    return '<div id="{}">{}</div>'.format(id, content)


def div_class(clas, content):
    return '<div class="{}">{}</div>'.format(clas, content)


def p(content):
    return "<p>{}</p>".format(content)


def p_class(clas, content):
    return '<p class="{}">{}</p>'.format(clas, content)


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
        recipe["title"].replace(" ", "-").replace('"', ""),
        "\n".join(
            [
                div("title", recipe["title"]),
                div(
                    "author",
                    p("From the kitchen of") + "\n" + p_class("name", recipe["author"]),
                ),
                div("serves", "serves " + str(recipe["serves"])),
                div("prep_minutes", "ready in " + str(recipe["prep_minutes"])),
                ingredients("ingredients", recipe["ingredients"]),
                render_portion("steps", "Steps", recipe["steps"]),
                render_portion("notes", "Notes", recipe["notes"]) if False else "",
            ]
        ),
    )


def template(content):
    with open("template.html") as f:
        return f.read().replace("INCLUDE_BODY", content)


def title_to_name(title):
    return title.replace(" ", "-").lower() + ".html"


def anchor(url, title):
    return '<a href="{}">{}</a>'.format(url, title)


def li(content):
    return "<li>{}</li>".format(content)


def ul(lis):
    return "\n".join(li(c) for c in lis)


def dump_index(recipes):
    index = ul(
        anchor(title_to_name(recipe["title"]), recipe["title"]) for recipe in recipes
    )
    open("docs/index.html", "w").write(index)


recipes = json.load(open("recipes.json"))

dump_index(recipes)

for recipe in recipes:
    open("docs/" + title_to_name(recipe["title"]), "w").write(
        template(render_recipe(recipe))
    )
