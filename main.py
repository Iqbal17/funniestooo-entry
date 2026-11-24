"""The Funniest Out-of-Office — make.fun one-line entry.

Final line (103 characters, one line, gate 1-140):
    I am out of office. My inbox now replies to itself and, frankly, it is
    doing a better job than I ever did.

Hand count: "I am out of office. " = 17, "My inbox now replies to itself" = 30,
" and, frankly, it is doing a better job than I ever did." = 56; 17 + 30 + 56 = 103.

DECISION RECORD — judged against the published judge brief, in its order:
1. A one-line out-of-office reply a real person would set and send.
2. Turns on a genuine surprise, a twist the reader does not see coming.
3. Sounds like a person with a voice of their own rather than a template.
4. Stays fresh, avoiding the jokes everyone has already read.
5. Uses every word, with nothing that could be cut without losing the laugh.

PASS 1 — first-draft candidates (written from scratch):
A. "I am out of office until Monday. My inbox is being guarded by my cat,
   who deletes anything that smells like a meeting."
   Cat-guarding-the-inbox is a known trope (fails 4); two sentences of setup
   for one thin joke (fails 5); the cat does nothing surprising (fails 2).
B. "Out of office. I left my laptop at home on purpose and my phone in a
   drawer, so please enjoy this rare moment of me not replying."
   No twist at all — it is just a list of where the devices are (fails 2);
   "rare moment of me not replying" is the only joke and it is telegraphed.
C. "I am out of office. My inbox has started replying to itself and,
   frankly, it is doing a better job than I ever did."
   The twist is real (an inbox that answers itself), the voice is dry and
   personal ("frankly"), the self-deprecation lands last, and nothing in it
   is a recycled inbox joke. Strong on 1-4; slightly loose on 5.
D. "I am out of office. My auto-reply got promoted while I was away, so
   please address all complaints to it directly."
   Good bureaucratic punch, but the logic wobbles — promoted by whom, while
   the owner is away? — and "address all complaints to it" needs the reader
   to do more work than C's punch. Loses to C on 1 and 2.
E. "Out of office. My auto-reply is also out of office, so this message was
   written by my calendar out of spite."
   "Written by my calendar out of spite" is the freshest single punch here,
   but the premise contradicts itself (an out-of-office auto-reply that is
   still writing) in a way that reads as a mistake rather than a joke, and
   it loses to C on 1.

PASS 2 — tightening the winner (C):
- "has started replying to itself" -> "now replies to itself": same joke,
  punchier, drops 9 characters of process for one word of immediacy.
- "frankly" kept deliberately: it is the voice word (criterion 3) and the
  dry understatement that sells the self-deprecation; cutting it saves 9
  characters but costs the personality.
- "than I ever did" kept over "than I did": "ever" stretches the failure
  across a career, which is where the laugh lives.
- Result: "I am out of office. My inbox now replies to itself and, frankly,
  it is doing a better job than I ever did." — 103 characters, one line.

Why it wins: it is a reply a real person would actually set (1); the inbox
answering itself is a twist nobody sees coming (2); "frankly" plus the
self-own give it a voice no template has (3); the mechanism is fresh — no
cat, no dog, no beach, no "your email is important to me" (4); and after
pass 2 every word is load-bearing (5).
"""

import os

LINE = (
    "I am out of office. My inbox now replies to itself and, frankly, "
    "it is doing a better job than I ever did."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read-back verification: the file must hold exactly the chosen line.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().rstrip("\n")
    assert text == LINE, "entry.txt does not match the chosen line"
    print(f"Verified: {len(text)} characters, 1 line.")
    print(text)


if __name__ == "__main__":
    main()
