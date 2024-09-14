-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices
config.default_prog = { '/usr/bin/fish', '-l' }

-- For example, changing the color scheme:
config.color_scheme = 'Dracula'
config.font =
    wezterm.font('MonoLisa Nerd Font Mono', { weight = 'Regular', italic = false })

config.font_size = 18
--https://wezfurlong.org/wezterm/config/appearance.html#text-background-opacity
--config.text_background_opacity = 1.0
config.window_background_opacity = 0.9

config.window_frame = {
    -- The font used in the tab bar.
    -- Roboto Bold is the default; this font is bundled
    -- with wezterm.
    -- Whatever font is selected here, it will have the
    -- main font setting appended to it to pick up any
    -- fallback fonts you may have used there.
    --font = wezterm.font { family = 'Roboto', weight = 'Bold' },
    font = wezterm.font {
        family = 'MonoLisa',
        weight = 'Regular' },
    -- The size of the font in the tab bar.
    -- Default to 10.0 on Windows but 12.0 on other systems
    font_size = 14.0,

    -- The overall background color of the tab bar when
    -- the window is focused
    active_titlebar_bg = '#333333',

    -- The overall background color of the tab bar when
    -- the window is not focused
    inactive_titlebar_bg = '#333333',
}

config.colors = {
    tab_bar = {
        -- The color of the inactive tab bar edge/divider
        inactive_tab_edge = '#575757',
    },
}

-- and finally, return the configuration to wezterm
return config
