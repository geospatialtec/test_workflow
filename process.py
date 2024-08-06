import os
import pandas as pd

text = []

for filename in os.listdir("asd/"):
   with open(os.path.join("asd/", filename), 'r') as f: # open in readonly mode
      text.append(f.read())

df = pd.DataFrame({'col1': text})
df.to_csv("output.csv", index=False)