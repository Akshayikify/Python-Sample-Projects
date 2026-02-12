import random
import time

OPERATORS=["+","-","*","/"]
MIN_OPERAND=3
MAX_OPERAND=12
TOTAL_PROBS=10

def generate_prob():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    Operators=random.choice(OPERATORS)
    expr=str(left)+" "+Operators+" "+str(right)
    ans=eval(expr)
    return expr,ans

wrong=0
input("Press enter to continue:")
print("--------------------------------")
start_time=time.time()
for i in range(TOTAL_PROBS):
    expr,ans=generate_prob()
    guess=input(f"Problem # {i+1} : {expr} = ")
    if guess==str(ans):
        break
    wrong+=1

end_time=time.time()
total_time=end_time-start_time
print("--------------------------------")
print(f"Nice work, You have completed in {round(total_time)} seconds")