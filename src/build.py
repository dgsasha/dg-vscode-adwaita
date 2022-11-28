#!/usr/bin/env python3
import json
import re
import itertools
import subprocess
from os import remove, path, chdir

from qualia_colors import get_qualia_colors
from qualia_ui_colors import get_qualia_ui_colors

SRC_DIR = path.dirname(path.realpath(__file__))
MAIN_SASS = 'qualia.scss'

chdir(SRC_DIR)

ACCENTS = {
    'orange': '#ed5b28',
    'bark': '#8d6b4c',
    'sage': '#737d5a',
    'olive': '#518e3c',
    'viridian': '#1fa36a',
    'prussiangreen': '#27b397',
    'lightblue': '#5298ce',
    'blue': '#465acb',
    'purple': '#9851c4',
    'magenta': '#c752c7',
    'pink': '#e86ba9',
    'red': '#df4242'
}

def load_jsonc(path):
    '''Read JSON with comments.'''
    original = open(path).read()
    stripped = re.sub(r'[^:]//.+$', '', original, flags=re.MULTILINE)
    return json.loads(stripped)


def get_default_syntax_colors(theme_type):
    return load_jsonc(f'default_themes/{theme_type}.jsonc')['tokenColors']


extra_syntax_colors = [
    {
        'scope': ['markup.italic.markdown'],
        'settings': {
            'fontStyle': 'italic'
        }
    },
    {
        'scope': ['markup.strikethrough.markdown'],
        'settings': {
            'fontStyle': 'strikethrough'
        }
    }
]

package_json_entry = {
    'contributes': {
        'themes': []
    }
}

for (
    theme_type,
    syntax_colors_type,
    accent
) in itertools.product(
    ('dark', 'light'),
    ('qualia', 'default'),
    list(ACCENTS.keys())
):
    accent_name = ' ' + accent if accent != 'orange' else ''

    name = f'qualia{accent_name} {theme_type}'

    ui_colors = get_qualia_ui_colors(theme_type, ACCENTS[accent])

    if syntax_colors_type == 'qualia':
        _named_colors, syntax_colors = get_qualia_colors(theme_type)
        syntax_colors += extra_syntax_colors
    else:
        syntax_colors = get_default_syntax_colors(theme_type)
        name += ' & default syntax highlighting'

    theme = {
        '$schema': 'vscode://schemas/color-theme',
        'name': name,
        'type': 'light',
        'colors': ui_colors,
        'tokenColors': syntax_colors
    }

    file_name = f'{name.lower().replace(" ", "-").replace("-&-", "-")}.json'
    json.dump(theme, open(f'../themes/{file_name}', 'w'), indent=2)

    package_json_entry['contributes']['themes'].append({
        'label': name,
        'uiTheme': 'vs-dark' if theme_type == 'dark' else 'vs',
        'path': f'./themes/{file_name}'
    })

print('Suggested package.json entry:')
print(json.dumps(package_json_entry, indent=2)[2:-2])