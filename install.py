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

    css_file = f'file:///{extension_dir}/css/qualia-{accent}-{theme}.css'
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

    print(f'{BGREEN}Installing{NC} the{BOLD} qualia VS Code theme {NC}in {BOLD}{extension_dir}{NC}')
    copytree(REPO_DIR, extension_dir, ignore=ignore_patterns('.*'), dirs_exist_ok=True)

    output = []

    if not Path(backup_config).is_file() and Path(code_config).is_file():
        copyfile(code_config, backup_config)

    if Path(code_config).is_file():
        for line in settings_json:
            dont_write = False
            r = open(code_config, "r", encoding='UTF-8')
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

    print(f'Writing VS Code configuration to {code_config}.')
    f = open(code_config, "w+", encoding='UTF-8')
    f.writelines(output)
    f.close()

print("In VS Code, the menu bar will be hidden until you press 'alt'.")
print("If you want to change this behavior, or any other settings, edit the 'settings.json' file.")
