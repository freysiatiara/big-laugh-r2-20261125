# One Line, Big Laugh — Round 2 Entry

[![Bounty](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/freysiatiara/big-laugh-r2-20261125/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/freysiatiara/big-laugh-r2-20261125/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

Entry for the [One Line, Big Laugh](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857) bounty on make.fun — a single funny line of at most 200 characters, judged pairwise by an AI judge.

## The line

> My bank flagged my $4 coffee as fraud, but the $900 flight I bought at 2 a.m. sailed through.

93 characters. Two beats: the bank's fraud system flags a $4 coffee (setup),
then waves through a $900 flight bought at 2 a.m. (inversion). A real joke
with an unexpected turn, tightly written, built on absurdly specific numbers —
not a re-skin of the round-1 entry (CAPTCHA, 0.554359, rank #339/1084) or of the
neighbouring board entries.

## How it works

`main.py` (Python 3, stdlib only) writes the line to `/output/entry.txt`
(falling back to `output/entry.txt` beside the script when `/output` is not
available), with mode `0644`. It writes deterministically: every run produces
byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
