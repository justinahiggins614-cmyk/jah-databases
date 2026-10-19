#!/usr/bin/env python3
"""Build script for the db-conversation-card-deck public + Signature database pair.
Wave 3 (1000 fun/social list). Property of Justin Addam Higgins (JAH).

Topics live in code/wave3-puzzles-social-build/topics/t_db_conversation_card_deck.py.
Run: python3 build.py
"""
import os
import sys

sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/wave3-puzzles-social-build"))
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/wave3-puzzles-social-build/topics"))

import w3lib
import t_db_conversation_card_deck as topics_mod


def main():
    built = w3lib.build_one(topics_mod)
    print("built pair:", topics_mod.CFG["slug"], "+", topics_mod.CFG["slug"] + "-signature")


if __name__ == "__main__":
    main()
