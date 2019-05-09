

if __name__ == "__main__":
    # Find the number for which the proportion of bouncy numbers
    # is exactly a porcentage received.
    def bouncy(n):
        str_list = str(n)
        up, down = False, False
        for i in range(1, len(str_list)):
            left = str_list[i - 1]
            right = str_list[i]
            if (left < right):
                up = True
            elif (left > right):
                down = True
            if (up and down):
                return True
        return False

    while True:
        # Testing for input mistakes
        try:
            text = input("Inform an integer value between 1 and 99 = ")
            received = int(text)
            if received <= 99 and received >= 1:
                break
        except Exception as e:
            pass

    count = 0
    i = 99
    while count < int(text) / 100 * i:
        i = i + 1
        if bouncy(i):
            count = count + 1
    print("The least number is {}".format(i))
