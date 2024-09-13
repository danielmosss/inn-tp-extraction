import spacy
from spacy import displacy
from datetime import datetime

text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
html = displacy.render(doc, style="ent")

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y-%H:%M:%S")
print("date and time =", dt_string)

with open("entities-{}.html".format(datetime), "w") as f:
    f.write(html)