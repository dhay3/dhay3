#!/usr/bin/env python
import time
import sys
from typing import List

STEP = 0.1
BIO = """👋 Bio
 • Gnu Believer. Support it now.
 • Tux Cultist(We suck Windows).
 • Disciple of RTFM & STFW. Ps. ATFL(Ask The Fucking LLM)
"""

CONTACT = """✉️ Contact me
 • Gmail - ■■■■■■■
   Please Sign the email with GPG.
 • Gvoice - ■■■■■■■
   Feel free to leave voice messages.
 • Telegram - ■■■■■■■
"""


def __type(content: List[str]) -> None:
    def t(s: str) -> None:
        for char in s:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(STEP)

    f = lambda x: t(x)

    for segment in content: f(segment)


if __name__ == '__main__':
    try:
        __type([BIO, CONTACT])
    except KeyboardInterrupt:
        pass
