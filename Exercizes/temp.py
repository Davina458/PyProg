def temp():
        try:
            temp = int(input("Whats the temp?: "))
        except ValueError:
            print("Not Valid Number")
            return
        return "turn heating off" if temp >= 21 else "turn heating off"

while True:
    print(temp())