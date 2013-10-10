#read file
f = open("hw1_15_train.dat")
data = []
for line in f:
    data.append(map(float, line.split()))


w = [0,0,0,0,0]

count = 0

while True:
    correct_num = 0
    for i, e in enumerate(data):
        dot = (w[0] * e[0] + w[1] * e[1] + w[2] * e[2] + w[3] * e[3] + w[4] * 1)

        if  dot * e[4] <=0:
            #correct
            w[0] = w[0] + e[0] * e[4]
            w[1] = w[1] + e[1] * e[4]
            w[2] = w[2] + e[2] * e[4]
            w[3] = w[3] + e[3] * e[4]
            w[4] = w[4] + 1 * e[4]

            count = count + 1

        else:
            correct_num = correct_num + 1

    if correct_num == 400:
        break
    else: 
        print correct_num
        print count, w


print len(data)
