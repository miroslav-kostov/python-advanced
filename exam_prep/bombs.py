from collections import deque

DATURA_BOMBS_SIZE = 40
CHERRY_BOMBS_SIZE = 60
SMOKE_DECOY_BOMBS_SIZE = 120

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = list(map(int, input().split(", ")))


def pouch_full():
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        return True
    return False


while bomb_effects:
    if pouch_full() or bomb_casings == []:
        break
    if bomb_effects[0] + bomb_casings[-1] == SMOKE_DECOY_BOMBS_SIZE:
        smoke_decoy_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
        continue
    elif bomb_effects[0] + bomb_casings[-1] == CHERRY_BOMBS_SIZE:
        cherry_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
        continue
    elif bomb_effects[0] + bomb_casings[-1] == DATURA_BOMBS_SIZE:
        datura_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
        continue
    bomb_casings[-1] -= 5


if pouch_full():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    bomb_effects = [str(x) for x in bomb_effects]
    print(f"Bomb Effects: {', '.join(bomb_effects)}")


if not bomb_casings:
    print("Bomb Casings: empty")
else:
    bomb_casings = [str(x) for x in bomb_casings]
    print(f"Bomb Casings: {', '.join(bomb_casings)}")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")