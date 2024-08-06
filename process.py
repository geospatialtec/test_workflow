import os
import pandas as pd

text = []

for filename in os.listdir("asd/"):
   with open(os.path.join("asd/", filename), 'r') as f: # open in readonly mode
      text.append(f.read())

output_dir = "output/"
if not os.path.exists(output_dir):
   os.mkdir(output_dir)

df = pd.DataFrame({'col1': text})
df.to_csv(os.path.join(output_dir, "output.csv"), sep=',', index=False, encoding='utf-8')