import random
import math

def simulate_birthday_paradox(n, trials=10000):
    collisions = 0
    for _ in range(trials):
        # سحب عشوائي لـ n أيام ميلاد من بين 365 يوم
        birthdays = [random.randint(1, 365) for _ in range(n)]
        # التحقق من وجود أيام مكررة (تصادم)
        if len(birthdays) != len(set(birthdays)):
            collisions += 1
    return collisions / trials

# 1. تنفيذ التجربة لكل n من 5 إلى 70 بخطوة 5
n_values = list(range(5, 71, 5))
results = []

print("n\tالاحتمال العملي\tالاحتمال النظري")
print("-" * 40)

for n in n_values:
    # النتيجة العملية من المحاكاة
    empirical_prob = simulate_birthday_paradox(n, trials=10000)
    
    # النتيجة النظرية (الحسابية)
    theoretical_prob = 1.0
    for i in range(n):
        theoretical_prob *= (365 - i) / 365
    theoretical_prob = 1.0 - theoretical_prob
    
    results.append((n, empirical_prob, theoretical_prob))
    print(f"{n}\t{empirical_prob:.4f}\t\t{theoretical_prob:.4f}")