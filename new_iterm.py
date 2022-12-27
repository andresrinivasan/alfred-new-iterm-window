#!/usr/bin/env python3

import sys

import iterm2


async def main(connection):
    if len(sys.argv) > 1:
        p = sys.argv[1]
    else:
        p = None

    w = await iterm2.Window.async_create(connection, p)
    await w.async_activate()  # Not sufficient to always raise the window

    a = await iterm2.async_get_app(connection)
    await a.async_activate(False, True)  # Raise only current active window


if __name__ == "__main__":
    iterm2.run_until_complete(main)
