# convert_your_turn

from microbit import *

sleep(1000)

s = "1234"
print("Before int conversion:")
print("s =", s)
print()

n = int(s)   # convert to int

n2 = n + n   # add

s2 = str(n2) # convert back

print("After convert, add ints, convert back:")
print("s2 =", s2)

# embed_intro

from microbit import *

sleep(1000)

s = "1 + 2 + 3 + 4"
reps = eval(s)

print("reps = ", reps)

# embed_try_this

from microbit import *

sleep(1000)

s = "1 + 2 + 3 + 4"
reps = eval(s)

print("reps = ", reps)

s = """                   # <- add
print('Start counting:')  # <- add
for n in range(0, reps):  # <- add
    print('n = ', n)      # <- add
"""                       # <- add

exec(s)                   # <- add

print('Done!')            # 