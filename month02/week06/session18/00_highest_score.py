import random

start_range = 1
end_range = 100

random_score = random.sample(range(start_range, end_range + 1), 50)

max_score = max(random_score)

print(random_score)
print(max_score)