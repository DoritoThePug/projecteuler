i = 1
prev_i = 1

sum = 0

while i < 4000000:
    if not i%2:
        sum += i

    t_prev_i = prev_i
    prev_i = i
    i+=t_prev_i


print(sum)