import emoji
from time import sleep
print('\033[1;7;35mContagem Regressiva\033[m')
for cr in range(10, -1, -1):
    print(cr)
    sleep(0.5)
print(emoji.emojize('\033[1;31mFOOOGOOOOOO! \U0001F4A5 \U0001F4A5 \U0001F4A5', use_aliases=True))
