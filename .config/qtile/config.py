# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget
import libqtile.hook  # need to use hooks
import logging
import os
import subprocess

mod = "mod4"

keys = [
    ## Bob Custom ##
    # Switch focus to specific monitor (out of two)
     Key([mod], "z",
         lazy.to_screen(0),
         desc='Keyboard focus to monitor 1'
         ),
     Key([mod], "x",
         lazy.to_screen(1),
         desc='Keyboard focus to monitor 2'
         ),
    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    ## Bob Custom ##
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("kitty")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

groups.extend([
    Group('1', spawn='firefox', layout='columns', persist=False,
          matches=[Match(wm_class=['Firefox'])]),
    Group('1', spawn='google-chrome', layout='columns', persist=False,
          matches=[Match(wm_class=['google-chrome', 'Google-chrome'])]),
    Group('1', spawn='qutebrowser', layout='columns', persist=False,
          matches=[Match(wm_class=['qutebrowser'])]),
    Group('2', spawn='kitty', layout='column', persist=False,
          matches=[Match(wm_class=['kitty'])]),
    Group('2', spawn='kitty', layout='column', persist=False,
          matches=[Match(wm_class=['kitty'])]),
    Group('3', spawn="/home/bob/.local/share/JetBrains/Toolbox/apps/PyCharm-P/ch-0/201.6668.115/bin/pycharm.sh",
          layout='max', persist=False,
          matches=[Match(wm_class=['jetbrains-pycharm'])]),
    Group('8', spawn='slack', layout='columns', persist=False,
          matches=[Match(wm_class=['slack', 'Slack'])]),
    Group('8', spawn='run_keybase', layout='columns', persist=False,
          matches=[Match(wm_class=['keybase', 'Keybase'])]),
    Group('9', spawn='spotify', layout='max', persist=False,
          matches=[Match(wm_class=['spotify', 'Spotify'])]),
])

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

##### Bob DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "09E397",    #BOB CHANGE "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

##### Bob THE LAYOUTS #####
layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND"],
        section_fontsize=11,
        bg_color="141414",
        active_bg="90C435",
        active_fg="000000",
        inactive_bg="384323",
        inactive_fg="a0a0a0",
        padding_y=5,
        section_top=10,
        panel_width=320
    ),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=16,
    padding=3,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(font="Ubuntu Bold",
                                this_screen_border='#e1acff',#Purple
                                this_current_screen_border='#09E397', #Hot Green
                                other_current_screen_border='#09E397', #Hot Green
                                other_screen_border='#e1acff' #Purple
                               ),
                widget.Prompt(),
                widget.WindowName(),
                #widget.TextBox("default config", name="default"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
            ],
            30,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []


# def app_or_group(group, app):
#     """ Go to specified group if it exists. Otherwise, run the specified app.
#     When used in conjunction with dgroups to auto-assign apps to specific
#     groups, this can be used as a way to go to an app if it is already
#     running. """
#
#     def f(qtile):
#         try:
#             qtile.groupMap[group].cmd_toscreen()
#         except KeyError:
#             qtile.cmd_spawn(app)
#
#     return f


# @libqtile.hook.subscribe.startup_once
# def autostart():
#     logging.basicConfig(
#         filename="/tmp/qtile.log",
#         filemode="a",
#         format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#         level=logging.WARN,
#     )
#     logging.warning("autostart function called BOB2")
#     #lazy.function(app_or_group("7", "spotify"))
#     lazy.function(app_or_group("5", "Alacritty"))


# use xprop to get app info
@libqtile.hook.subscribe.client_new
def client_new_hook(window):
    logging.basicConfig(
        filename="/tmp/qtile.log",
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.WARN,
    )
    logging.warning("function client_new_hook called...")
    logging.warning(window)


#### STARTUP APPLICATIONS ####
@libqtile.hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

    # if window.match(wname="Slack"):
    #     window.togroup("8")
    # elif window.match(wname="Keybase"):
    #     window.togroup("8")
    # elif window.match(wname="qutebrowser"):
    #     window.togroup("1")
    # elif window.match(wname="Mozilla Firefox"):
    #     window.togroup("1")
    # elif window.match(wname="New Tab - Google Chrome"):
    #     window.togroup("1")

# @libqtile.hook.subscribe.client_new
# def clent_new_hook_spot(windows):
#    if window.math(wname="Spotify Premium"):
#        window.togroup("8")

# def func(c):
#    if c.name == "spotify":
#        c.togroup("9")


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
