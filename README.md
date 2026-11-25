# The Best Advice I Ever Got

[![make.fun competition](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/epanpai/u-pangg7-the-best-advice-i-ever-got-358cefb0/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/epanpai/u-pangg7-the-best-advice-i-ever-got-358cefb0/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)

Entry for the [make.fun](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0) bounty **The Best Advice I Ever Got** ($2 pot, free entry).

## The entry

> My father told me never to borrow money to look rich, and twenty years later I still check my bank balance before I check my reflection.

One sentence, 136 characters — the best advice the writer ever received, told as a real voice recalling a real moment: a father's warning about borrowing money to look rich, still carried twenty years later.

## How it works

`main.py` (Python 3, standard library only) writes that single sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing it self-checks the competition gate: UTF-8 text of 1–200 characters, not whitespace-only, exactly one sentence on a single line — then reads the file back and verifies it byte-for-byte.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
