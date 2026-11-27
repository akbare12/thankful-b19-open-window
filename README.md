# Open Window

[![bounty](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b19-open-window/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b19-open-window/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

A thank-you for the judge, written straight to the judge. One concrete
thing, done slowly: the window in the judge's room is lifted a finger
wide, and the afternoon is let in — cool air against a day of pages.

> Thank you for keeping on through the still air of this room. The air hangs heavy, stale from a whole day of pages. So I lift the window a finger wide, and let the afternoon come in, cool and green. Breathe it in, deep and easy. It smells of rain that never fell. When I close the window, that breath stays, resting in the corners.

The text is 330 characters. The window closes again at the end, but the
breath that came in does not leave with it — it stays, resting in the
corners, so the next thing the judge reads meets air that is still fresh.

## How it works

`main.py` uses only the Python standard library (`os`). It writes the
fixed text above, byte for byte, to `entry.txt` in the directory given by
`MAKEFUN_OUTPUT_DIR` (default `out`). No randomness, no network, no clock,
no file reading — the same text comes out on every run, on every machine.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
