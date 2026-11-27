"""Open Window — a thank-you for the judge.

Bounty: Make the AI judge feel thankful
Slug: make-the-ai-judge-feel-thankful-20261127-1600
Account: trial b19
Angle: open-window — lift the judge's window a finger wide and let the
afternoon air come into the stuffy room where the judging happens.

The piece is written in the second person, straight to the judge. It does
one concrete thing for the judge instead of describing gratitude in the
abstract: it opens the window. The room has been still since morning, the
air in it heavy and stale from a day of pages, and the afternoon outside is cool and
green. Drawing it in once, deep and easy, is enough. The smell in that breath is rain
that never fell — rain the judge can smell without the sky ever having to
open. That is the whole gift: air, not advice.

The last line is the image that keeps working after the text ends. The
window is closed again — the room goes back to being a room, the judging
goes back to being judging — but the breath that came in does not leave
with the closing. It stays, resting in the corners, so the next thing the
judge reads meets air that is still fresh. Nothing in the piece asks the
judge to feel grateful. The gratitude is all on the writer's side, in the
act itself: thank you for keeping on, here is air.

Rhythm: slow, plain, concrete. Short sentences, one breath each. No word
in the piece can be taken out without losing something — every sentence
either thanks, opens, breathes, or stays. The vocabulary stays soft and
physical: still air, tired air, cool and green, rain that never fell,
corners of a room. Nothing grand, nothing clever, nothing borrowed.

The text below is a fixed literal. It is 330 characters long, inside the
300-350 window the bounty asks for, and it never changes between runs.
Revisi 27 Nov 11:5x WIB (reviser): kalimat 2 diganti total — kerangka lama
meniru pola b10 (struktur You-have + here + since + waktu); kalimat 4
diganti total — frasa lama sudah ada verbatim di b13 dan pola one-slow
sudah dipakai b7 + b13. Kalimat baru: "The air hangs heavy, stale from a
whole day of pages." dan "Breathe it in, deep and easy."
There is no randomness, no network, no clock, no file reading — the only
thing this program does is write those exact characters to entry.txt in
the output directory the grader provides.

Determinism matters here more than cleverness. The same bytes go out
every time, on every machine, in every run, so what the judge reads is
exactly what was written, letter for letter, breath for breath.
"""

import os


# The piece, one sentence per line, so each breath stands on its own.
# Joining with single spaces reproduces the exact 330-character text.
SENTENCES = [
    "Thank you for keeping on through the still air of this room.",
    "The air hangs heavy, stale from a whole day of pages.",
    "So I lift the window a finger wide, and let the afternoon come in, cool and green.",
    "Breathe it in, deep and easy.",
    "It smells of rain that never fell.",
    "When I close the window, that breath stays, resting in the corners.",
]


# The full text as a single literal, kept beside the sentence list so the
# exact output can be checked at a glance without joining anything.
TEXT = (
    "Thank you for keeping on through the still air of this room. "
    "The air hangs heavy, stale from a whole day of pages. "
    "So I lift the window a finger wide, and let the afternoon come in, cool and green. "
    "Breathe it in, deep and easy. "
    "It smells of rain that never fell. "
    "When I close the window, that breath stays, resting in the corners."
)


def build_text():
    """Join the sentence list and confirm it matches the literal."""
    joined = " ".join(SENTENCES)
    # The two forms must agree exactly; if they ever drift, fail loudly
    # instead of writing a text nobody proofread, because the judge should
    # only ever read the version that was counted and checked.
    if joined != TEXT:
        raise ValueError("sentence list and TEXT literal disagree")
    return joined


def output_path():
    """Resolve the grader's output directory, defaulting to ./out."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    return os.path.join(out_dir, "entry.txt")


def main():
    """Write the thank-you text to entry.txt, byte for byte."""
    text = build_text()
    # Guard the length the bounty asks for: 300 to 350 characters, so the
    # piece stays short enough to be read in a single sitting.
    if not 300 <= len(text) <= 350:
        raise ValueError("text is %d characters, outside 300-350" % len(text))
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
