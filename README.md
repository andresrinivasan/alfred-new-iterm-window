# New iTerm Window Workflow for Alfred

Start a new iTerm session from Alfred using the default profile or a selected profile and optionally starting in the last directory opened in Finder.

## Compatibility

This workflow requires Alfred 5 and iTerm 2. iTerm must already be running.

## Usage

A single keyword `ni` (i.e. New iTerm) is defined for Alfred. Unmodified, this keyword will launch a new iTerm window using the default profile. Typing `ni` and `<SPACE>` will show a list of profiles to select from and typing any portion of a profile name will filter down to that profile.

Hold `<OPTION>` while launching to have the iTerm session start in the last directory opened in Finder.

## Credit

This is a rewrite of [https://github.com/miromannino/alfred-new-terminal-window] using Python, the iTerm Python API, and Alfred 5 Automation.
