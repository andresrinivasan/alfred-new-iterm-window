#!/usr/bin/env python3

import json

import iterm2


async def get_most_profiles(c):
    all = await iterm2.PartialProfile.async_query(c)
    return [p for p in all if p.all_properties["Name"] != "Hotkey Window"]


async def main(connection):
    print(
        json.dumps(
            {
                "items": [
                    {
                        "title": "New iTerm Window",
                        "subtitle": f"Start {p.all_properties['Name']}",
                        "arg": p.all_properties["Name"],
                        "match": p.all_properties["Name"],
                        "autocomplete": p.all_properties["Name"],
                        "mods": {
                            "alt": {
                                "subtitle": f"Start {p.all_properties['Name']} profile in last Finder directory"
                            }
                        },
                    }
                    for p in await get_most_profiles(connection)
                ]
            }
        )
    )


if __name__ == "__main__":
    iterm2.run_until_complete(main)
