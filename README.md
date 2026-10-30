# ChatGPT codes that actually work (because you define them)

ChatGPT has no secret codes. A code like `/study` only works when ChatGPT knows exactly what it means, so you tell it once and it follows the rule in every chat.

I picked these codes from about 4,800 real comments under "ChatGPT tips" videos (what people actually ask for and like), then tested every one on GPT-5.5.

**Test (29.10.2026):** each code 3 times with the definitions saved, and once without. With the definitions: **27 of 27** answers had the exact format. Without them: 2 of 9, and only by luck. Without its definition, `/newcode` was read as a request to write programming code.

---

## 1. Set it up (1 minute)

**ChatGPT:** Settings → Personalization → Custom instructions → paste the block into the field → Save.
The block is about 1,050 characters, so it fits the 1,500-character limit on the free plan.

**Gemini:** Settings & help → Personal context (Saved info) → Add → paste → Submit. (Not available to users under 18.)

**Claude:** Settings → the field for the personal preferences Claude should consider in responses → paste. You can also put it in a Project's instructions.

Then start any message with a code, for example: `/tldr` + the text you paste.

## 2. The block to paste

```
Don't agree with me by default. Before you back an idea, plan or opinion of mine, name its weakest point and what would make it fail. If you're unsure of a fact, say so.
When my message starts with a code, follow its rule exactly:
/audit = rate each area I list 1-10, brutally honest, then the 3 changes that matter most.
/sop = turn my notes or transcript into a numbered checklist anyone can follow (step, who, when).
/tldr = 3 bullets, max 40 words, then one line "Do this:" with the next action.
/study = explain in 3 short sentences, 1 everyday example, then 3 quiz questions with the answers at the very end.
/check = list each factual claim and mark it verified, unsure or wrong; say how to check it; never invent sources.
/decide = table of my options (pros, cons, cost, risk), then recommend one in 2 sentences.
/reply = short reply to the message I paste: polite, direct, max 5 sentences, in my tone; ask me first if key info is missing.
/newcode = ask me 3 short questions about a task I repeat, then write a new code line in this same format.
```

## 3. What each part does (with real test answers)

**The first line: no yes-man.** The most-liked instruction people shared in those comments was "never agree with me by default". So it is always on, not a code.
> *"I'm quitting my job to open a coffee shop. Everyone loves coffee, so it's going to work, right?"*
> → "Weakest point: 'everyone loves coffee' doesn't prove enough people will buy *your* coffee often enough at prices that cover rent, wages…" followed by how to test demand before quitting.

**/audit**: an honest score for your week, your business or your plan.
> `/audit my last week: sleep 5 hours, gym 0 times, worked 62 hours, saw friends once…`
> → a table: Sleep 2/10, Gym 1/10, Work 4/10… then the 3 changes that matter most.

**/sop**: notes, a voice-note transcript or a YouTube transcript turned into steps anyone can follow.
> `/sop how we onboard a new cleaning client: Ania calls them, we send the price list…`
> → 1. Initial call (who: Ania, when: as soon as the enquiry comes in), 2. Send price list…

**/tldr**: long text in, 3 bullets and one action out.
> → "…Do this: order a bigger bin on the council website before 15 November."

**/study**: learn anything with a built-in quiz.
> `/study compound interest` → 3 sentences, "$100 at 10% → $110 → $121", 3 questions, then the answers.

**/check**: catches made-up "facts".
> `/check The Great Wall is visible from space. Einstein failed maths. Water boils at 100 °C at sea level.`
> → Wrong / Wrong / Verified, each with how to check it.

**/decide**: options in a table, then one clear pick.
> `/decide used van for 40k, lease for 1,900 a month, or rent at 250 a day (6 days a month)` → the table, then a recommendation, starting with the weakest point of the cheapest-looking option.

**/reply**: customer messages answered in 5 sentences or fewer.
> `/reply "Your cleaners came 2 hours late and missed the kitchen."` → an apology, a fix (come back or a partial refund) and a question about what the customer prefers.

## 4. Make your own code

Type `/newcode`. ChatGPT asks you 3 questions (the task you repeat, what the answer should look like, any limits) and writes a new line for you to add to the block.

Or write one yourself: `/name = what to do + what the answer must look like + limits.`
Good codes are for things you do **every week**: invoices, quotes, posts, meal plans, homework help.

## 5. If a code stops working
- Check that the block is saved (open Custom instructions again).
- Start a new chat, because instructions apply to new chats.
- Too long with your own text? On paid plans the field holds 5,000 characters. On the free plan, move the block into a Project's instructions.

## 6. Never paste
Passwords, card or bank numbers, ID numbers, or your clients' personal data. Replace names with "Client A".

## Files in this repo
- `block.txt`: the block above as a plain file, ready to copy.
- `test/test_v2.py`: the test I ran (GPT-5.5 via the OpenAI API, the block as the system prompt, standing in for Custom Instructions). Run it from `test/` with `OPENAI_API_KEY` set.
- `test/results_v2.json`: every answer from that run; `test/scores_v2.json`: the counts (each code: answers in the right format with the block, without it).

---
Kris | @aipractically. Comment on the reel if you want more codes for a specific job.
