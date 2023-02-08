#!/usr/bin/env python3

from os import path, environ, makedirs
from shutil import copytree, ignore_patterns, copyfile
from pathlib import Path
import argparse
import json5 as json

NC = '\033[0m'
BOLD = '\033[1m'
BGREEN = '\033[1;32m'

USER = environ.get('USER')
HOME = path.expanduser(f'~{USER}')
REPO_DIR = path.dirname(path.realpath(__file__))

USER_CONFIG_DIRS = [
    f'{HOME}/.config/Code/User',
    f'{HOME}/.var/app/com.visualstudio.code/config/Code/User'
]

EXTENSIONS_DIRS = [
    f'{HOME}/.vscode/extensions',
    f'{HOME}/.var/app/com.visualstudio.code/data/vscode/extensions'
]

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

for user_config_dir, extensions_dir in zip(USER_CONFIG_DIRS, EXTENSIONS_DIRS):
    if not (path.isdir(user_config_dir) and path.isdir(extensions_dir)):
        continue

    code_config = f'{user_config_dir}/settings.json'
    backup_config = f'{user_config_dir}/settings.json.bak'

    extension_dir = f'{extensions_dir}/qualia'

    makedirs(extension_dir, exist_ok=True)

    override = {
        "workbench.preferredDarkColorTheme": f"qualia{accent_name} dark{default_syntax}",
        "workbench.preferredLightColorTheme": f"qualia{accent_name} light{default_syntax}",
        "workbench.colorTheme": f"qualia{accent_name} {theme}{default_syntax}"
    }
    optional = {
        "window.titleBarStyle": "native",
        "window.menuBarVisibility": "toggle",
        "window.autoDetectColorScheme": True,
        "window.title": "${rootPath}${separator}Code",
        "breadcrumbs.enabled": False,
        "editor.renderLineHighlight": "none",
        "workbench.iconTheme": None,
        "workbench.tree.indent": 12
    }

    full = {**override, **optional}
    print(f'{BGREEN}Installing{NC} the{BOLD} qualia VS Code theme {NC}in {BOLD}{extension_dir}{NC}')
    copytree(REPO_DIR, extension_dir, ignore=ignore_patterns('.*'), dirs_exist_ok=True)

    if not Path(backup_config).is_file() and Path(code_config).is_file():
        copyfile(code_config, backup_config)

    print(f'Writing VS Code configuration to {code_config}.')

    try:
        with open(code_config, 'r') as file:
            data = json.load(file)
        for key, value in optional.items():
            if key not in data.keys():
                data[key] = value
        for key, value in override.items():
            data[key] = value
        with open(code_config, 'w') as file:
            json.dump(data, file, indent=2)
    except:
        with open(code_config, 'w') as file:
            json.dump(full, file, indent=2)

print("In VS Code, the menu bar will be hidden until you press 'alt'.")
print("If you want to change this behavior, or any other settings, edit the 'settings.json' file.")
