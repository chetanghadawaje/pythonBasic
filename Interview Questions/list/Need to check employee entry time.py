# Need to check employee entry time. If some employee entry more than one time within hour then we need to return particular employee name.
input1 = ["cris", "peter", "gorge", "Hendry", "jatin", "cris", "Hendry", "Malik", "peter"]
input2 = ["11:30", "12:10", "14:00", "16:00", "10:40", "12:00", "15:40", "15:30", "16:00"]

# Expected output= ["cris","Hendry"]

def time_convert(data):
    d = data.split(":")
    total = (int(d[0]) * 60) + int(d[1])
    return total


output_list = []
for i in range(len(input1)):
    if input1[i] not in output_list:
        x = [y for y in range(len(input1)) if input1[i] == input1[y]]
        if len(x) > 1:
            temp = input2[x[0]]
            for time_index in range(1, len(x)):
                time_to_check = time_convert(input2[x[time_index]]) - time_convert(temp)
                if 60 >= time_to_check >= -60:
                    output_list.append(input1[i])

print(output_list)
