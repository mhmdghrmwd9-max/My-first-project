import random

def simulate_mm2(lambda_rate, mu_rate, num_customers):
    # وقت انتهاء الخدمة لكل خادم من الخادمين
    server1_free_time = 0
    server2_free_time = 0
    total_wait_time = 0
    current_time = 0
    
    for i in range(num_customers):
        # وقت الوصول التالي (توزيع أسي)
        inter_arrival = random.expovariate(lambda_rate)
        current_time += inter_arrival
        
        # وقت الخدمة (توزيع أسي)
        service_time = random.expovariate(mu_rate)
        
        # نختار الخادم الذي سيفرغ أولاً (أو الأقل انشغالاً)
        if server1_free_time <= server2_free_time:
            # إذا كان الخادم الأول سيفرغ أولاً أو متاحاً فوراً
            if current_time >= server1_free_time:
                wait_time = 0
                server1_free_time = current_time + service_time
            else:
                wait_time = server1_free_time - current_time
                server1_free_time += service_time
        else:
            # إذا كان الخادم الثاني هو الأسرع في التفرغ
            if current_time >= server2_free_time:
                wait_time = 0
                server2_free_time = current_time + service_time
            else:
                wait_time = server2_free_time - current_time
                server2_free_time += service_time
                
        total_wait_time += wait_time

    avg_wait = total_wait_time / num_customers
    print(f"Two Queues / Servers (M/M/2) - Average Waiting Time: {avg_wait:.4f}")

# تشغيل التجربة بوجود خادمين لـ 1000 عميل
simulate_mm2(lambda_rate=1.0, mu_rate=1.5, num_customers=1000)