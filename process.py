import pandas as pd

with open("asd/test.txt", 'r') as f:
    text = f.read()

df = pd.DataFrame({'col1': [text]})
df.to_csv("output.csv", index=False)