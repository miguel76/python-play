def gcd(a, b):
    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d

def lcm(a, b):
    return a * b / gcd(a, b)

num_tests = int(raw_input())
for test_index in range(num_tests):
    num_sensors = int(raw_input())
    sensor_intervals = map(int, raw_input().split())
    min_lcm = -1
    for sensor_index_a in range(num_sensors - 1):
        interval_a = sensor_intervals[sensor_index_a]
        for interval_b in sensor_intervals[sensor_index_a + 1:]:
            lcm_ab = lcm(interval_a, interval_b)
            if min_lcm == -1 or lcm_ab < min_lcm:
                min_lcm = lcm_ab
    print(min_lcm)
