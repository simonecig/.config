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

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty -e zsh"
launcher = "dmenu_run"

colors = []
cache = "/home/ciga/.cache/wal/colors"


def load_colors(cache):
    with open(cache, "r") as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append("#ffffff")
    lazy.reload()


load_colors(cache)

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # audio
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+ unmute")),
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10- --min-value=5")),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Cycle layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn(launcher), desc="Spawn a command using a prompt widget"),
    # Toggle floating layout
    Key(
        [mod, "shift"],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle floating layout",
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                "m",
                lazy.run_extension(
                    extension.WindowList(
                        dmenu_ignorecase=True,
                        fontsize=12,
                        item_format="{window}",
                        selected_background=colors[4],
                        selected_foreground=colors[8],
                    )
                ),
            ),
        ]
    )

layouts = [
    # layout.Columns(border_normal=colors[0], border_focus=colors[7], border_width=5, margin=3, num_columns=3, border_on_single=True),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, border_normal=colors[0], border_focus=colors[6]),
    layout.Bsp(
        margin=10,
        ratio=1,
        border_normal=colors[0],
        border_focus=colors[6],
        border_width=3,
    ),
    layout.Max(border_normal=colors[0], border_focus=colors[6], border_width=3),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="RobotoMono Nerd Font",
    # font="Roboto",
    fontsize=16,
    padding=3,
    background=colors[0],
    foreground=colors[7],
)
extension_defaults = widget_defaults.copy()


def open_stuff(qtile):
    qtile.cmd_spawn("chromium")


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=colors[1],
                    scale=0.5,
                    mouse_callbacks={"hover": open_stuff},
                ),
                widget.Sep(foreground=colors[0], size_percent=60),
                widget.GroupBox(),
                widget.Spacer(length=bar.STRETCH),
                widget.Systray(icon_size=20, padding=5, background=colors[0]),
                # widget.Spacer(length=10),
                widget.Sep(foreground=colors[0], size_percent=60),
                widget.Clock(format="  %a %I:%M %p ", background=colors[0]),
                widget.Clock(format=" %m-%d ", background=colors[0]),
                widget.Sep(size_percent=60),
                widget.Backlight(
                    backlight_name="amdgpu_bl0",
                    format="  {percent:2.0%} ",
                    background=colors[0],
                ),
                widget.Battery(
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    full_char="",
                    format="{char} {percent:2.0%} ",
                    notify_below=15,
                    update_interval=1,
                    show_short_text=False,
                    background=colors[0],
                ),
                widget.Volume(background=colors[0], fmt="墳 {0}"),
                widget.QuickExit(
                    default_text="  ", countdown_format="{}", background=colors[0]
                ),
            ],
            30,
            background=colors[0],
            opacity=1,
        )
    )
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="Nitrogen"),  # gitk
        Match(wm_class="lxappearence"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
