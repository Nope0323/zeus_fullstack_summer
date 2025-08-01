import random

score = [random.randint(0,100) for _ in range(0,50)]

print(score)
print(f"max:{max(score)}")