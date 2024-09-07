import time
import sys
import subprocess

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


def __type(content: str) -> None:
    for char in content:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(STEP)


if __name__ == '__main__':
    __type(BIO)
    __type(CONTACT)
