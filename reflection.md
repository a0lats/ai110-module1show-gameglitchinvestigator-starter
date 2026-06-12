# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first thing I noticed when playing the game was that my score kept going up even when I was guessing wrong. That immediately felt off because you should not be rewarded for a bad guess. After playing a few more rounds I also noticed the hints were sending me in the wrong direction and Hard mode seemed way too easy compared to Normal.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 80, secret is 73|Go LOWER hint|Go HIGHER hint shown|none|
|Correct guess on attempt 2|Win declared|Game continued like I was wrong|none|
|Switch to Hard difficulty|Harder range than Normal|Range was 1 to 50, easier than Normal|none|
---

## 2. How did you use AI as a teammate?

I used Claude as my AI assistant. It correctly suggested moving all the game logic into logic_utils.py which made testing way easier and I verified it by running pytest and seeing all 10 tests pass. On the other hand the original AI generated code had a bug disguised as a feature where it converted the secret to a string on even attempts, which broke win detection, and I only caught it by actually playing the game.

---

## 3. Debugging and testing your fixes

I verified fixes by running pytest and playing the game in the browser. For the hint bug I guessed 80 against a secret of 73 and confirmed it said "Go LOWER." For the score bug I watched the debug panel and confirmed the score dropped after every wrong guess.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the whole script every time you interact with anything, so session state is what keeps the game from resetting the secret number every time you click submit.
---

## 5. Looking ahead: your developer habits

I want to keep writing tests right after fixing bugs instead of at the end because it forces you to define what fixed actually means. This project taught me that AI generated code still needs a human to actually play with it and catch what the AI cannot see.
