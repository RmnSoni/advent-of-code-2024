import pandas as pd 
import collections

df = pd.read_csv("./day01.csv", names = ["Left","Right"])

score = 0
freqs = collections.Counter(df['Right'].values)

for num in df.Left.values:
    score += num * freqs[num]

print(score)
