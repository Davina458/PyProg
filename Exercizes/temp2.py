

def average(list):
    average = sum(list)/len(list)
    return average

def min_and_max(list):
    min = list[0]
    max = list[0]
    for i in list:
        if i > max:
            max = i
        elif i < min:
            min = i
    print(f"Min temp: {min}\nMax temp: {max}")



def temp_average():
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    temp = []
    count = 0
    for day in days:
        try:
            temp.append(int(input(f"What the temp on {day}?: ")))
        except ValueError:
            print("Not a whole number")
            return
    averag = round(average(temp), 2)
    print(f"The average temp was {averag}°c")
    min_and_max(temp)
    for i in temp:
        if i > averag:
            count += 1
    print(f"There was {count} days over average")
        




temp_average()