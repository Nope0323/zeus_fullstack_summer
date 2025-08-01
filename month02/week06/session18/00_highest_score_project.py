import random



scores=[]

for i in range(0,50):
    random_score = random.randint(0,100)
    scores.append(random_score)
print(scores)


print(f"max {max(scores)}")
