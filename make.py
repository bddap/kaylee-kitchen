#!/usr/bin/env python3

import json


def div(id, content):
    return '<div id="{}">{}</div>'.format(id, content)


def div(id, content):
    return '<div id="{}">{}</div>'.format(id, content)


def section(id, content):
    return '<section id="{}">{}</section>'.format(id, content)


recipes = json.load(open("recipes.json"))

for recipe in recipes:
    print(
        section(
            "",
            div("author", recipe["author"])
            + div("serves", recipe["serves"])
            + div("prep_minutes", recipe["prep_minutes"]),
        )
    )
