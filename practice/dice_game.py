import random as r
from collections import Counter
sum_list=[]
frequency_list=[]
two_die_roll_output = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
                       (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
                       (3,1), (3,2), (3,3), (3,4), (3,5), (3,6),
                       (4,1), (4,2), (4,3), (4,4), (4,5), (4,6),
                       (5,1), (5,2), (5,3), (5,4), (5,5), (5,6),
                       (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]
for d1,d2 in two_die_roll_output:
    sum_list.append(d1+d2)
frequency_distribution = dict(Counter(sum_list))
for key in frequency_distribution:
    frequency_list.append(frequency_distribution[key])
# print(f"frequency distribution of sums: {frequency_distribution}")
while True:
    playsum = 0
    AI_sum = 0
    print(f"Whelcome to the dice game player!")
    print(f"want to roll the dice? (y/n)")
    roll = input()
    if roll == "y":
        die1 = r.randint(1,6)
        die2 = r.randint(1,6)
        print(f"you rolled {die1} and {die2}")
        print(f"the sum is {die1+die2}")
        playsum = die1 + die2
    elif roll == "n":
        print(f"thank you for playing the dice game!")
        break
    print(f"AI rolled the dice!")
    ai_die1 = r.randint(1,6)
    ai_die2 = r.randint(1,6)
    print(f"AI rolled {ai_die1} and {ai_die2}")
    print(f"AI's sum is {ai_die1+ai_die2}")
    AI_sum = ai_die1 + ai_die2
    if frequency_distribution[playsum]==min(frequency_list) or frequency_distribution[playsum]< frequency_distribution[AI_sum]:
        print(f"you rolled the least frequent sum! you win!")
    elif frequency_distribution[AI_sum]==min(frequency_list)or frequency_distribution[AI_sum]< frequency_distribution[playsum]:
        print(f"AI rolled the least frequent sum! AI wins!")
    else:
        print(f"no one rolled the least frequent sum! it's a draw!")