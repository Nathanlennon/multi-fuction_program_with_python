name = "random_name"
stop = "stop"
x = "none"


def ia():
    global name
    global stop
    global x
    name = input("hey user, what's your name ?")
    print(f"hi {name}, I'm Chara, your personal IA. If you want something, you just have to ask")
    print("What is your question ?")
    while x != "stop":
        x = input("")
        if "take" and "addition" in x:
            addition()

        '''if "how are you" in x:
            print("I'm fine, tank you")
            input("and you ?")'''

        if "substraction" in x:
            substraction()

        if "multiplication" in x:
            multiplication()

        if "division" in x:
            division()

        if "operation" in x:
            operation()


def addition():
    i = 1
    r = 1
    result = 0
    add = 0
    while r == 1:
        add = input(f"What's your number {i} ? (stop for stop)")
        if add == "stop":
            r = 0
        else:
            add = int(add)
            result += add
        i += 1
    print(result)


def substraction():
    i = 1
    r = 1
    result = 0
    sub = 0
    while r == 1:
        sub = input(f"What's your number {i} ? (stop for stop)")
        if sub == "stop":
            r = 0
        else:
            sub = int(sub)
            if i == 1:
                result = sub
            else:
                result -= sub
        i += 1
    print(result)


def multiplication():
    i = 1
    r = 1
    result = 0
    mult = 0
    while r == 1:
        mult = input(f"What's your number {i} ? (stop for stop)")
        if mult == "stop":
            r = 0
        else:
            mult = int(mult)
            if i == 1:
                result = mult
            else:
                result *= mult
        i += 1
    print(result)


def division():
    global x
    i = 1
    r = 1
    result = 0
    div = 0
    if "euclidean division" in x:
        other = 0
        while i != 3:
            div = input(f"What's your number {i} ? (stop for stop)")
            if div == "stop":
                r = 0
            else:
                div = int(div)
                if i == 1:
                    result = div
                else:
                    other = (result % div)
                    result //= div
            i += 1
        print(result, other)
    else:
        while r == 1:
            div = input(f"What's your number {i} ? (stop for stop)")
            if div == "stop":
                r = 0
            else:
                div = int(div)
                if i == 1:
                    result = div
                else:
                    result /= div
            i += 1
    print(result)


def operation():
    num = 1
    ope = []
    r = 1
    res = False
    x = input(f"What's your number {num}?")
    if x == "stop":
        return
    else:
        ope += [x]
    while r != 0:
        sign = input("What's your operation ? (stop for stop)")
        if sign == "stop":
            r = 0
        elif sign == "plus" or sign == "+":
            ope += ["+"]
        elif sign == "minus" or sign == "-":
            ope += ["-"]
        elif sign == "times" or sign == "*":
            ope += ["*"]
        elif sign == "over" or sign == "/":
            ope += ["/"]
        num += 1
        if r != 0:
            ope += [input(f"What's your number {num} ?")]
    print(ope)
    a = input("it's your calculation ?")
    if a == "yes":
        res = False
        while not res:
            index = 0
            sign = "none"
            if "*" in ope or "/" in ope:
                while "*" in ope or "/" in ope:
                    sign = (ope[index])
                    index += 1
                    if sign == "*":
                        x = float(ope[(ope.index("*") - 1)])
                        y = float(ope[(ope.index("*") + 1)])
                        re = x * y
                        ope.pop(ope.index("*") - 1)
                        ope.pop(ope.index("*") + 1)
                        ope.insert((ope.index("*") + 1), re)
                        ope.pop(ope.index("*"))
                        index = 0

                    elif sign == "/":
                        x = float(ope[(ope.index("/") - 1)])
                        y = float(ope[(ope.index("/") + 1)])
                        re = x / y
                        ope.pop(ope.index("/") - 1)
                        ope.pop(ope.index("/") + 1)
                        ope.insert((ope.index("/") + 1), re)
                        ope.pop(ope.index("/"))
                        index = 0

            else:
                while "+" in ope or "-" in ope:
                    sign = (ope[index])
                    index += 1

                    if sign == "+":
                        x = float(ope[(ope.index("+") - 1)])
                        y = float(ope[(ope.index("+") + 1)])
                        re = x + y
                        ope.pop(ope.index("+") - 1)
                        ope.pop(ope.index("+") + 1)
                        ope.insert((ope.index("+") + 1), re)
                        ope.pop(ope.index("+"))
                        index = 0

                    elif sign == "-":
                        x = float(ope[(ope.index("-") - 1)])
                        y = float(ope[(ope.index("-") + 1)])
                        re = x - y
                        ope.pop(ope.index("-") - 1)
                        ope.pop(ope.index("-") + 1)
                        ope.insert((ope.index("-") + 1), re)
                        ope.pop(ope.index("-"))
                        index = 0

                else:
                    res = True

        print(ope)


    elif a == "no":
        operation()



ia()
