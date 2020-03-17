import numpy as np

members = ["Nat", "Matt", "Ben"]

seed1 = 5682
seed2 = 5678
seed3 = 8888
seed = seed1 + seed2 + seed3

np.random.seed(seed)

np.random.shuffle(members)

print(members)
