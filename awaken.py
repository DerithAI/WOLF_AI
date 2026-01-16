#!/usr/bin/env python3
"""
WOLF_AI - Awaken the Pack

Run this to bring the pack to life.
"""

import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from core.pack import awaken_pack


def main():
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║     🐺 W O L F _ A I 🐺                                 ║
    ║                                                          ║
    ║     The Pack Awakens...                                  ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    pack = awaken_pack()

    print(f"\n✅ Pack Status: {pack.status}")
    print(f"🐺 Wolves Active: {len(pack.wolves)}")
    print()

    for name, wolf in pack.wolves.items():
        print(f"   {name.upper():8} | {wolf.role:10} | {wolf.status}")

    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║     AUUUUUUUUUUUUUUUUUUUUUUUU! 🐺🐺🐺                   ║
    ║                                                          ║
    ║     The pack is ready to hunt.                          ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    return pack


if __name__ == "__main__":
    main()
