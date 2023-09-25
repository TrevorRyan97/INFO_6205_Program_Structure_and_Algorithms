# World Cup Gale-Shapley Example. 16 teams in Group A and B - Trevor Ryan

import random
import time

# Start timer
t0 = time.time()

def gale_shapley_world_cup_example(GroupA_prefs, GroupB_prefs):
    n = len(GroupA_prefs)
    A_matches = [-1] * n
    B_matched = [False] * n

    while A_matches.count(-1) > 0:
        for GroupA in range(n):
            if A_matches[GroupA] == -1:
                for GroupB in GroupA_prefs[GroupA]:
                    if not B_matched[GroupB]:
                        A_matches[GroupA] = GroupB
                        B_matched[GroupB] = True
                        break
                    else:
                        current_partner = A_matches.index(GroupB)
                        if GroupB_prefs[GroupB].index(GroupA) < GroupB_prefs[GroupB].index(current_partner):
                            A_matches[GroupA] = GroupB
                            B_matched[GroupB] = False
                            A_matches[current_partner] = -1

    stable_matches = [(GroupA, GroupB) for GroupA, GroupB in enumerate(A_matches)]
    return stable_matches

# Initialize preferences
GroupA_prefs = []
GroupB_prefs = []

# Create preferences for teams in Group A
for i in range(16):
    pref1 = list(range(16))
    random.shuffle(pref1)
    GroupA_prefs.append(pref1)

# Create preferences for teams in Group B
for i in range(16):
    pref2 = list(range(16))
    random.shuffle(pref2)
    GroupB_prefs.append(pref2)

# Call the Gale Shapley code using the randomized preferences
stable_matches = gale_shapley_world_cup_example(GroupA_prefs, GroupB_prefs)

for GroupA, GroupB in stable_matches:
    print(f"Team {GroupA} from Group A is matched with Team {GroupB} from Group B")

t1 = time.time()
total = t1-t0

# Print the total time that it took to run the algorithm
print(f" Total time to run code is {total} seconds")