import random

def simulate_mm1(lambda_rate, mu_rate, num_customers):
    t_arrival = 0
    t_service_end = 0
    total_wait_time = 0
    
    current_time = 0
    
    for i in range(num_customers):
        # وقت الوصول التالي (توزيع أسي)
        inter_arrival = random.expovariate(lambda_rate)
        current_time += inter_arrival
        
        # وقت الخدمة (توزيع أسي)
        service_time = random.expovariate(mu_rate)
        
        # حساب وقت الانتظار
        if current_time < t_service_end:
            wait_time = t_service_end - current_time
            t_service_end += service_time
        else:
            wait_time = 0
            t_service_end = current_time + service_time
            
        total_wait_time += wait_time

    avg_wait = total_wait_time / num_customers
    print(f"Average Waiting Time: {avg_wait:.4f}")

# مثال للتجربة (معدل الوصول 1، ومعدل الخدمة 1.5، لـ 1000 عميل)
simulate_mm1(lambda_rate=1.0, mu_rate=1.5, num_customers=1000)