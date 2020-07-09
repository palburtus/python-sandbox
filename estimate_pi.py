import random

def estimate_pi(n):
    num_points_in_circle = 0
    num_points_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_points_in_circle += 1
        num_points_total +=1
    
    return 4 * num_points_in_circle/num_points_total

print(estimate_pi(10))
print(estimate_pi(100))
print(estimate_pi(1000))
print(estimate_pi(10000))
print(estimate_pi(100000))
print(estimate_pi(1000000))
print(estimate_pi(10000000))

#3.1415
#101 example of Monte Carlo method