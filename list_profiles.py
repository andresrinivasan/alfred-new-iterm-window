#!/usr/bin/env python3

import json

import iterm2


async def main(connection):
    print(
        json.dumps(
            {
                "items": [
                    {
                        "uid": p.all_properties["Guid"],
                        "title": "New iTerm Window",
                        "subtitle": p.all_properties["Name"],
                        "arg": p.all_properties["Name"],
                        "match": p.all_properties["Name"],
                        "autocomplete": p.all_properties["Name"],
                    }
                    for p in await iterm2.PartialProfile.async_query(connection)
                ]
            }
        )
    )


if __name__ == "__main__":
    iterm2.run_until_complete(main)
