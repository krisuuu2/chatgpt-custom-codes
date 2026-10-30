# Test every v2 code 3x on GPT-5.5 with the block as system prompt (stand-in for Custom Instructions), plus the same input without the block.
import json, os, re, requests, concurrent.futures as cf
KEY = os.environ["OPENAI_API_KEY"]
BLOCK = open("../block.txt", encoding="utf-8").read()
S = requests.Session()
CASES = {
 "rule": "I'm quitting my job next month to open a coffee shop in my small town. Everyone loves coffee, so it's going to work, right?",
 "audit": "/audit my last week: sleep about 5 hours a night, gym 0 times, worked 62 hours, saw friends once, read nothing, ate takeaway 6 times.",
 "sop": "/sop how we onboard a new cleaning client: Ania calls them, we send the price list, they pick a day, Marek checks the address, first clean, after a week we ask for a review, invoice goes out on Friday",
 "tldr": "/tldr The city council voted to change bin collection from weekly to every two weeks starting 1 December. Recycling stays weekly. Residents can order a bigger bin for free until 15 November through the council website. Missed collections must be reported within 48 hours. Fines for overfilled bins start in January.",
 "study": "/study compound interest",
 "check": "/check The Great Wall of China is visible from space with the naked eye. Einstein failed maths at school. Water boils at 100 degrees Celsius at sea level.",
 "decide": "/decide I need a car for my small business: a used Toyota van for 40k, leasing a new Ford Transit for 1,900 a month, or renting a van only on job days for 250 a day (about 6 days a month).",
 "reply": "/reply Customer email: 'Your cleaners came 2 hours late today and missed the kitchen. I paid for a full clean. Not happy.'",
 "newcode": "/newcode",
}
def ask(user, system):
    msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    for _ in range(4):
        try:
            r = S.post("https://api.openai.com/v1/chat/completions", headers={"Authorization": "Bearer " + KEY}, json={"model": "gpt-5.5", "messages": msgs}, timeout=180)
            r.raise_for_status(); return r.json()["choices"][0]["message"]["content"]
        except requests.RequestException: pass
    return "ERROR"
jobs = [(k, i, True) for k in CASES for i in range(3)] + [(k, 0, False) for k in CASES]
with cf.ThreadPoolExecutor(8) as ex:
    res = list(ex.map(lambda j: {"case": j[0], "i": j[1], "block": j[2], "answer": ask(CASES[j[0]], BLOCK if j[2] else None)}, jobs))
json.dump(res, open("results_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for r in res: print(r["case"], r["i"], "block" if r["block"] else "RAW  ", len(r["answer"].split()), "words")
