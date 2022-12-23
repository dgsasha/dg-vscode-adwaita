from qualia_colors import get_qualia_colors


named_colors, _syntax_colors = get_qualia_colors('light')

def get_qualia_ui_colors(theme_type, accent):
    def _(name): return lambda value: named_colors[f'{name}_{value}']
    dark = theme_type == 'dark'

    ui_colors = {
        # libadwaita doesn't use shadows to indicate scrollable content.
        'scrollbar.shadow':                     '#00000000',

        'activityBar.background':               '#252525' if dark else '#f7f7f7',
        'titleBar.activeBackground':            '#252525' if dark else '#f7f7f7',
        'tab.activeBackground':                 '#3a3a3a' if dark else '#e4e4e4',
        'tab.inactiveBackground':               '#252525' if dark else '#f7f7f7',
        'editorGroupHeader.tabsBackground':     '#252525' if dark else '#f7f7f7',
        'breadcrumb.background':                '#252525' if dark else '#f7f7f7',
        'tab.hoverBackground':                  '#343434' if dark else '#e9e9e9',
        'tab.activeForeground':                 '#ffffff' if dark else '#313131',
        'tab.inactiveForeground':               '#ffffff' if dark else '#313131',

        'panel.background':                     '#252525' if dark else '#f7f7f7',
        'sideBar.background':                   '#252525' if dark else '#f7f7f7',
        'statusBar.background':                 '#252525' if dark else '#f7f7f7',
        'statusBar.noFolderBackground':         '#252525' if dark else '#f7f7f7',
        'statusBarItem.remoteBackground':       '#252525' if dark else '#f7f7f7',
        'panelSectionHeader.background':        '#00000000',
        'sideBarSectionHeader.background':      '#00000000',

        'activityBar.border':                   '#454545' if dark else '#e0e0e0',
        'editorBracketMatch.border':            '#454545' if dark else '#e0e0e0',
        'editorGroup.border':                   '#454545' if dark else '#e0e0e0',
        'editorGroupHeader.border':             '#454545' if dark else '#e0e0e0',
        'editorGroupHeader.tabsBorder':         '#454545' if dark else '#e0e0e0',
        'panel.border':                         '#454545' if dark else '#e0e0e0',
        'panelSectionHeader.border':            '#454545' if dark else '#e0e0e0',
        'sideBar.border':                       '#454545' if dark else '#e0e0e0',
        'sideBarSectionHeader.border':          '#454545' if dark else '#e0e0e0',
        'statusBar.border':                     '#454545' if dark else '#e0e0e0',
        'tab.border':                           '#454545' if dark else '#e0e0e0',
        'titleBar.border':                      '#454545' if dark else '#e0e0e0',
        'window.activeBorder':                  '#454545' if dark else '#e0e0e0',
        'tree.indentGuidesStroke':              '#45454599' if dark else '#e0e0e099',
        'editorIndentGuide.activeBackground':   '#45454599' if dark else '#e0e0e099',
        'editorIndentGuide.background':         '#45454580' if dark else '#e0e0e080',
        'editorRuler.foreground':               '#45454580' if dark else '#e0e0e080',
        'editorBracketMatch.background':        '#45454520' if dark else '#e0e0e080',
        # A dotted outline, not a solid border, but it's the best we can get.
        # 'list.inactiveFocusOutline':            '#454545' if dark else '#cfcfcf',

        'list.hoverBackground':                 '#333333' if dark else '#ececec',
        'list.inactiveSelectionBackground':     '#3a3a3a' if dark else '#e6e6e6',
        'input.background':                     '#3a3a3a' if dark else '#e6e6e6',

        'statusBar.foreground':                 '#ffffff' if dark else '#323232',
        'statusBar.noFolderForeground':         '#ffffff' if dark else '#323232',
        'statusBar.debuggingForeground':        '#ffffff' if dark else '#323232',
        'statusBarItem.remoteForeground':       '#ffffff' if dark else '#323232',
        'sideBar.foreground':                   '#ffffff' if dark else '#323232',
        'panelTitle.activeBorder':              '#ffffff' if dark else '#323232',
        'panelTitle.activeForeground':          '#ffffff' if dark else '#323232',

        'activityBar.activeBorder':             '#00000000',
        'activityBarBadge.background':          accent,
        'button.background':                    '#ffffff1a' if dark else '#00000014',
        'button.secondaryBackground':           '#ffffff1a' if dark else '#00000014',
        'button.hoverBackground':               '#ffffff26' if dark else '#0000001f',
        'button.secondaryHoverBackground':      '#ffffff26' if dark else '#0000001f',
        'button.border':                        '#ffffff0d',
        'button.foreground':                    '#ffffff' if dark else '#000000',
        'button.secondaryForeground':                    '#ffffff' if dark else '#000000',
        'list.activeSelectionBackground':       accent,
        'list.highlightForeground':             '#ffffff' if dark else '#323232',
        'list.activeSelectionForeground':       '#ffffff',
        'list.activeSelectionIconForeground':   '#ffffff',
        'list.focusHighlightForeground':        '#ffffff',
		'textLink.foreground':                  accent,
		'textLink.activeForeground':            accent,
		'list.focusOutline':                    accent + '80',
        'notebook.focusedCellBorder':           accent + '80',
		'notebook.focusedEditorBorder':         accent + '80',
        'notebook.cellInsertionIndicator':      accent + '80',
        'notebook.cellInsertionIndicator':      accent + '80',
        'focusBorder':                          accent + '80',
        'sash.hoverBorder':                     accent + '80',
		'panelSection.dropBackground':          accent + '4d',
		'sideBar.dropBackground':               accent + '4d',
		'editorGroup.dropBackground':           accent + '4d',
		'terminal.dropBackground':              accent + '4d',
		'list.dropBackground':                  accent + '4d',

        'editorGutter.addedBackground':                     _('green')(4),
        'editorGutter.deletedBackground':                   _('red')(4),
        'editorGutter.modifiedBackground':                  accent,
        'gitDecoration.addedResourceForeground':            _('green')(1) if dark else _('green')(5),
        'gitDecoration.renamedResourceForeground':          _('green')(1) if dark else _('green')(5),
        'gitDecoration.untrackedResourceForeground':        _('green')(1) if dark else _('green')(5),
        'gitDecoration.modifiedResourceForeground':         _('orange')(1) if dark else _('orange')(5),
        'gitDecoration.stageModifiedResourceForeground':    _('orange')(1) if dark else _('orange')(5),
        'gitDecoration.deletedResourceForeground':          _('red')(1) if dark else _('red')(5),
        'gitDecoration.stageDeletedResourceForeground':     _('red')(1) if dark else _('red')(5),
        'gitDecoration.ignoredResourceForeground':          _('dark')(1) if dark else _('dark')(5),

        'commandCenter.background':             '#444444' if dark else '#d9d9d9',
        'commandCenter.border':                 '#00000000',

        'activityBar.foreground':               '#ffffff' if dark else '#323232',
        'editor.background':                    '#292929' if dark else '#fcfcfc',
        'editorLineNumber.foreground':          '#666666' if dark else '#32323280',
    	'editorActiveLineNumber.foreground':    '#ffffff' if dark else '#323232',
        'widget.shadow':                        '#00000033' if dark else '#00000022',
        'editor.foreground':                    '#ffffff' if dark else '#323232',
    }

    return ui_colors
