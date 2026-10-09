while True:

    st = input("enter string: ")

    if st == "exit":
        break

    stack = []
    count = 0
    valid = True

    for i in st:

        if i == "(" or i == "[" or i == "{":
            stack.append(i)
            count += 1

        elif i == ")" or i == "]" or i == "}":

            if not stack:
                valid = False
                break

            if (i == ")" and stack[-1] == "(") or (i == "]" and stack[-1] == "[") or (i == "}" and stack[-1] == "{"):
                stack.pop()
                count -= 1

            else:
                valid = False
                break

    if valid and count == 0:
        print("Valid string.")
    else:
        print("Invalid string.")