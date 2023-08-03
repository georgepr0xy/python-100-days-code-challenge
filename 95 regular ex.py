import re
 
pattern=r"[A-Z]+nimal"


text ='''Animals play an essential role in human life and planet earth. Ever since an early time, humans have been using animals for their benefit. Earlier, they came in use for transportation purposes.

Further, they also come in use for food, hunting and protection. Humans use oxen for farming. Animals also come in use as companions to humans. For instance, dogs come in use to guide the physically challenged people as well as old people.

In research laboratories, animals come in use for drug testing. Rats and rabbits are mostly tested upon. These researches are useful in predicting any future diseases outbreaks. Thus, we can protect us from possible harm.'''

matches=re.search(pattern,text)
matches=re.finditer(pattern,text)
print(matches)

for i in matches:
    print(i.span())
    print(i[i.span()[0]:i.span()[5]])