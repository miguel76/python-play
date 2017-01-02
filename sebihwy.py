num_tests = int(raw_input())
for test_index in range(num_tests):
    (sebi_speed, sebi_guess, father_guess, distance, time) = map(int, raw_input().split())
    car_speed = sebi_speed + distance * 3600 * 0.05 / time
    sebi_error = abs(car_speed - sebi_guess)
    father_error = abs(car_speed - father_guess)
    if (sebi_error == father_error):
        print "DRAW"
    elif (sebi_error < father_error):
        print "SEBI"
    else:
        print "FATHER"
