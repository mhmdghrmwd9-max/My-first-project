import random

def simulate_dice_rolls(num_rolls):
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        counts[roll] += 1
        
    print(f"Dice Simulation Results for {num_rolls} rolls:")
    for face, count in counts.items():
        percentage = (count / num_rolls) * 100
        print(f"Face {face}: {count} times ({percentage:.2f}%)")

# تشغيل التجربة 1000 مرة
simulate_dice_rolls(1000)