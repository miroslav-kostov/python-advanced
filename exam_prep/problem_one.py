from collections import deque

firework_effects = [int(x) for x in input().split(", ") if int(x) > 0]
explosive_power = [int(x) for x in input().split(", ") if int(x) > 0]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0


def fireworks_ready():
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        return True
    return False


while firework_effects:
    if fireworks_ready() or explosive_power == []:
        break

    current_sum = firework_effects[0] + explosive_power[-1]
    if current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette_fireworks += 1
        firework_effects.pop(0) and explosive_power.pop(-1)
    elif current_sum % 3 == 0:
        palm_fireworks += 1
        firework_effects.pop(0) and explosive_power.pop(-1)
    elif current_sum % 5 == 0:
        willow_fireworks += 1
        firework_effects.pop(0) and explosive_power.pop(-1)
    else:
        current_effect = firework_effects[0] - 1
        firework_effects.pop(0)
        if current_effect > 0:
            firework_effects.append(current_effect)

if fireworks_ready():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(y) for y in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(y) for y in explosive_power)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")