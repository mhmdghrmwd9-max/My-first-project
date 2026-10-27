import random

def simulate_sales(num_days):
    # جدول الاحتمالات والطلبات بناءً على بياناتك
    # (الطلب، الاحتمال التراكمي CDF)
    demand_dist = [
        (0, 0.10),
        (1, 0.25),
        (2, 0.45),
        (3, 0.75),
        (4, 0.95),
        (5, 1.00)
    ]
    
    total_demand = 0
    
    for day in range(1, num_days + 1):
        r = random.random() # توليد رقم عشوائي بين 0 و 1
        chosen_demand = 0
        
        for demand, cdf in demand_dist:
            if r <= cdf:
                chosen_demand = demand
                break
                
        total_demand += chosen_demand
        print(f"Day {day}: Random = {r:.2f} | Demand = {chosen_demand}")

    avg_demand = total_demand / num_days
    print(f"\nAverage Daily Demand over {num_days} days: {avg_demand:.2f}")

# تشغيل التجربة لمدة 10 أيام مثلاً
simulate_sales(10)