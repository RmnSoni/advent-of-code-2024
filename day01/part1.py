import pandas as pd 

df = pd.read_csv("./day01.csv", names = ["Left","Right"])

left = df.Left.values.tolist()
left.sort()

right = df.Right.values.tolist()
right.sort()

score = 0
print(right, left)

for i in range(0,1000):
    score += abs(right[i]-left[i])
print(score)
