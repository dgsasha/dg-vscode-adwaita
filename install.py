#!/usr/bin/env python3

from os import path, environ, makedirs
from shutil import copytree, ignore_patterns, copyfile
from pathlib import Path
import argparse

NC = '\033[0m'
BOLD = '\033[1m'
BGREEN = '\033[1;32m'

USER = environ.get('USER')
HOME = path.expanduser(f'~{USER}')
REPO_DIR = path.dirname(path.realpath(__file__))
USER_CONFIG_DIR = f'{HOME}/.config/Code/User'
CODE_CONFIG = f'{USER_CONFIG_DIR}/settings.json'
BACKUP_CONFIG = f'{USER_CONFIG_DIR}/settings.json.bak'
EXTENSION_DIR = f'{HOME}/.vscode/extensions/qualia'

ACCENTS = (
    'orange',
    'bark',
    'sage',
    'olive',
    'viridian',
    'prussiangreen',
    'lightblue',
    'blue',
    'purple',
    'magenta',
    'pink',
    'red'
)

makedirs(EXTENSION_DIR, exist_ok=True)
makedirs(USER_CONFIG_DIR, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument(
    '-c',
    choices = ACCENTS,
    default = ACCENTS[0],
    help = 'choose accent color'
)

parser.add_argument(
    '-t',
    choices = ('light', 'dark'),
    default = 'light',
    help = 'choose theme variant'
)

parser.add_argument(
    '-d',
    action = 'store_true',
    help = 'use default syntax highlighting'
)

args = parser.parse_args()

accent = args.c
theme = args.t
accent_name = ' ' + accent if accent != 'orange' else ''
default_syntax = ' & default syntax highlighting' if args.d else ''

css_file = f'file:///{EXTENSION_DIR}/css/qualia-{accent}-{theme}.css'
settings_json = [
    '{',
    f'    "workbench.preferredDarkColorTheme": "qualia{accent_name} dark{default_syntax}",',
    f'    "workbench.preferredLightColorTheme": "qualia{accent_name} light{default_syntax}",',
    f'    "workbench.colorTheme": "qualia{accent_name} {theme}{default_syntax}",',
    '    "window.titleBarStyle": "native",',
    '    "window.menuBarVisibility": "toggle", // Menu bar will be hidden until you press Alt',
    '    "window.autoDetectColorScheme": true,',
    '    "window.title": "${rootPath}${separator}Code",',
    '    "breadcrumbs.enabled": false,',
    '    "editor.renderLineHighlight": "none",',
    '    "workbench.iconTheme": null,',
    '    "workbench.tree.indent": 12,',
    '}'
]

print(f'{BGREEN}Installing{NC} the{BOLD} qualia VS Code theme {NC} in {BOLD}{EXTENSION_DIR}{NC}')
copytree(REPO_DIR, EXTENSION_DIR, ignore=ignore_patterns('.*'), dirs_exist_ok=True)
        
output = []

if not Path(BACKUP_CONFIG).is_file() and Path(CODE_CONFIG).is_file():
    copyfile(CODE_CONFIG, BACKUP_CONFIG)

if Path(CODE_CONFIG).is_file():
    for line in settings_json:
        dont_write = False
        r = open(CODE_CONFIG, "r")
        for l in r:
            if not l.strip().startswith('"workbench.colorTheme') \
            and not l.strip().startswith('"workbench.preferredLightColorTheme') \
            and not l.strip().startswith('"workbench.preferredDarkColorTheme') \
            and l.strip().startswith(line.strip().split(':')[0]):
                output.append(l)
                dont_write = True
        if not dont_write:
            output.append(line + '\n')
        r.close()
else:
    for line in settings_json:
        output.append(line + '\n')

print(f'Writing VS Code confgiguration to {CODE_CONFIG}.')
print(f"In VS Code, the menu bar will be hidden until you press 'alt'.")
print(f"If you want to change this behavior, or any other settings, edit the 'settings.json' file.")
f = open(CODE_CONFIG, "w+")
f.writelines(output)
f.close()