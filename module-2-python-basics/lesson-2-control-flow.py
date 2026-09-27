"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Cortez, jerick daniel]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

a program decides what to do next. Instead of always running every line of code in the same way, 
we can give the program a condition and let it choose what to do based on the situation.


============================================
KEY VOCABULARY
============================================
- condition: something the program checks to decide what it should do
- if / elif / else: if checks the first condition, elif checks another condition if the first one is false, and else runs when none of the conditions are true.
- comparison operator: a symbol used to compare two values, such as >, <, ==, >= or <=
- boolean expression: an expression that results in either True or False. It is usually used when a program needs to make a decision.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
temperature = 30

if temperature > 35:
    print("It's very hot.")
elif temperature >= 25:
    print("The water is warm.")
else:
    print("The water is cool.")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
I want to avoid is using = instead of == when making a condition

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
