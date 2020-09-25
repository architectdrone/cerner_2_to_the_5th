#cerner_2^5_2020
a, b, c, d, e, round = 100, (lambda : ((lambda : (lambda k, l: (f"{l[0]} {k[0]}", (k[1][0]+l[1][0], k[1][1]+l[1][0], l[1][1])))(__import__("random").choice([("sword", (7, 3)),("rapier", (9, 1)),("battleaxe", (3, 7)),("hammer", (1, 9))]), __import__("random").choice([("flaming", (2, 10)),("toxic", (5, 5)),("sharp", (10, 0)),("glowing", (5, 15)),("enchanted", (0, 20))])))(), __import__("random").choice([("shield", (1, 9)),("chestplate", (5,5)),("chainmail", (9, 1))])))(), 100, (lambda : ((lambda : (lambda k, l: (f"{l[0]} {k[0]}", (k[1][0]+l[1][0], k[1][1]+l[1][0], l[1][1])))(__import__("random").choice([("sword", (7, 3)),("rapier", (9, 1)),("battleaxe", (3, 7)),("hammer", (1, 9))]), __import__("random").choice([("flaming", (2, 10)),("toxic", (5, 5)),("sharp", (10, 0)),("glowing", (5, 15)),("enchanted", (0, 20))])))(), __import__("random").choice([("shield", (1, 9)),("chestplate", (5,5)),("chainmail", (9, 1))])))(), True, 0
input(f"In the plains of desolation you met your timeless foe. \nThe sun glints off of his {d[1][0]} as he pulls out his {d[0][0]}.\nYour grip tightens on your {b[0][0]}. You pray to your gods that your {b[1][0]} will protect you.\nPRESS ENTER")
while min(((round := round + 1) - 50), 0) and max(0, a) and max(0, c):
    print(f"PLAYER HP: {a} ENEMY HP: {c}")
    f, g = [d, b][int(e)], [d, b][int(not e)]
    h, i, j = max(f[0][1][0]-g[1][1][0], 0), max(f[0][1][1]-g[1][1][1], 0), __import__("random").randrange(f[0][1][2]+1)
    if e: 
        print(f"You swing your {f[0][0]} hitting his {g[1][0]}, doing {h} piercing, {i} bashing, and {j} extra damage")
        c -= h + i + j
    else: 
        print(f"He swings his {f[0][0]} hitting your {g[1][0]}, doing {h} piercing, {i} bashing, and {j} extra damage")
        a -= h + i + j
    e = not e
    input("Press ENTER")
if c <= 0: print("You stand over the body of your defeated foe. Finally, you can rest.")
elif a <= 0: print("As the light fades, you hear a grim laugh taunting you.")
else: print("You and your enemy are at a stalemate. Your enemy nods, in respect of a worthy foe.")

'''
PS C:\dev\personal> python .\battle.py
In the plains of desolation you met your timeless foe. 
The sun glints off of his chestplate as he pulls out his sharp rapier.
Your grip tightens on your enchanted battleaxe. You pray to your gods that your chestplate will protect you.
PRESS ENTER
PLAYER HP: 100 ENEMY HP: 100
You swing your enchanted battleaxe hitting his chestplate, doing 0 piercing, 2 bashing, and 11 extra damage
Press ENTER
PLAYER HP: 100 ENEMY HP: 87
He swings his sharp rapier hitting your chestplate, doing 14 piercing, 6 bashing, and 0 extra damage
Press ENTER
PLAYER HP: 80 ENEMY HP: 87
You swing your enchanted battleaxe hitting his chestplate, doing 0 piercing, 2 bashing, and 18 extra damage
Press ENTER
PLAYER HP: 80 ENEMY HP: 67
He swings his sharp rapier hitting your chestplate, doing 14 piercing, 6 bashing, and 0 extra damage
Press ENTER
PLAYER HP: 60 ENEMY HP: 67
You swing your enchanted battleaxe hitting his chestplate, doing 0 piercing, 2 bashing, and 3 extra damage
Press ENTER
PLAYER HP: 60 ENEMY HP: 62
He swings his sharp rapier hitting your chestplate, doing 14 piercing, 6 bashing, and 0 extra damage
Press ENTER
PLAYER HP: 40 ENEMY HP: 62
You swing your enchanted battleaxe hitting his chestplate, doing 0 piercing, 2 bashing, and 10 extra damage
Press ENTER
PLAYER HP: 40 ENEMY HP: 50
Press ENTER
PLAYER HP: 20 ENEMY HP: 50
You swing your enchanted battleaxe hitting his chestplate, doing 0 piercing, 2 bashing, and 20 extra damage
Press ENTER
PLAYER HP: 20 ENEMY HP: 28
He swings his sharp rapier hitting your chestplate, doing 14 piercing, 6 bashing, and 0 extra damage
Press ENTER
As the light fades, you hear a grim laugh taunting you.
'''