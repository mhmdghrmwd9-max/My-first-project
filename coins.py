import random

def simulate_coin_toss(num_flips):
    heads = 0
    tails = 0
    
    for _ in range(num_flips):
        # اختيار عشوائي بين 0 و 1 (مثلاً 0 وجه، 1 كتابة)
        result = random.choice(['وجه (Head)', 'صورة/كتابة (Tail)'])
        if 'وجه' in result:
            heads += 1
        else:
            tails += 1
            
    print(f"Total Flips: {num_flips}")
    print(f"Heads Count: {heads} ({(heads/num_flips)*100:.2f}%)")
    print(f"Tails Count: {tails} ({(tails/num_flips)*100:.2f}%)")

# تشغيل التجربة 1000 مرة
simulate_coin_toss(1000)