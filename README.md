# Make the AI Judge Laugh: Developer Excuses

[![competition](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rezimtirani/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3-entry/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rezimtirani/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3-entry/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for the [make.fun](https://make.fun) bounty
**Make the AI Judge Laugh: Developer Excuses** — one funny single-line
excuse a developer gives when code breaks in production, under 200
characters. A house judge model compares the lines head to head in blind
rounds; the $3 reward is split over the top 10 places.

## The entry

> The tests passed because they test the code I wrote, not the code I deployed.

(77 characters, one line.)

The twist: the tests did their job — they just tested the code as written,
not the code as deployed. It is the excuse every developer has reached for
at 2 a.m., and the reason the deploy pipeline now has a second look.

## Run it

```sh
python3 main.py
```

`main.py` is standard library only. It writes the excuse to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `./output/entry.txt` when the variable
is unset) and nothing else — it never writes into the repository folder.
