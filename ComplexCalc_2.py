#Writing methods that will be used by the kick start process
def add(list_of_nums):
    sum = 0
    for i in range(len(list_of_nums)):
        sum = sum + list_of_nums[i]
    return sum, len(list_of_nums)

def mul (list_of_nums):
    prod = 1
    for i in range(len(list_of_nums)):
        prod = prod * list_of_nums[i]
    return prod, len(list_of_nums)

def div (list_of_nums):
    div = 1
    for i in range(len(list_of_nums)):
        div = div / list_of_nums[i]
    return div, len(list_of_nums)

def sub (list_of_nums):
    sub = 0
    for i in range(len(list_of_nums)):
        sub = list_of_nums[i] - sub
    return sub, len(list_of_nums)

#writing methods that will be used by the continuation process
def add_range(result, i, list_of_nums):
    sum = 0
    print(list_of_nums)
    for i in range(len(list_of_nums)):
        sum = result + list_of_nums[i]
    return sum, i

def mul_range(result, i, list_of_nums):
    prod = 1
    print(list_of_nums)
    for i in range(len(list_of_nums)):
        prod = result * list_of_nums[i]
    return prod, i

def div_range(result, i, list_of_nums):
    div = 1
    print(list_of_nums)
    for i in range(len(list_of_nums)):
        div = result / list_of_nums[i]
    return div, i

def sub_range(result, i, list_of_nums):
    sub = 0
    print(list_of_nums)
    for i in range(len(list_of_nums)):
        sub = result - list_of_nums[i]
    return sub, i
if __name__=="__main__":
    #showing the physical layout of calculator by storing the values in dictionaries
    top_left = {"key":9}
    top_mid = {"key":8}
    top_rite = {"key":7}

    mid_left = {"key":6}
    mid_mid = {"key":5}
    mid_rite = {"key":4}

    bot_left = {"key":3}
    bot_mid = {"key":2}
    bot_rite = {"key":1}

    bottom_zero = {"key":0}
    op_left = {"key":"/"}
    op_mid = {"key":"-"}
    op_rite = {"key":"*"}

    below_op = {"key":"+"}

    #writing code to display the calculator
    print("\t",top_left["key"],"  ",top_mid["key"],"  ",top_rite["key"],"\n\t"
          , mid_left["key"],"  ",mid_mid["key"],"  ",mid_rite["key"],"\n\t"
          ,bot_left["key"],"  ",bot_mid["key"],"  ",bot_rite["key"],"\n\t-----",bottom_zero["key"],"-----\n\t",
          op_left["key"],"  ",op_mid["key"],"  ",op_rite["key"],
          "\n\t-----",below_op["key"],"-----\n\t")

    #Kick starting the accepting of records
    list_of_nums = []
    num1 = float(input("enter the number"))
    op = input("enter the operator")
    num2 = float(input("enter the second number"))
    list_of_nums.append(num1)
    list_of_nums.append(num2)
    if op == "+":
        result_1, i = add(list_of_nums)
        print(result_1)
    elif op == "*":
        result_1, i = mul(list_of_nums)
        print(result_1)
    elif op == "/":
        result_1, i = div(list_of_nums)
        print(result_1)
    elif op == "-":
        result_1, i = sub(list_of_nums)
        print(result_1)

    print(list_of_nums)

    # looping the input acceptance
    while True:
        try:
            op2 = input("enter the operator")
            num3 = int(input("enter the number"))
            list_of_nums.append(num3)
            print("value of i is: ", i)
            while True:
                if op2 == "+":
                    result_1, i = add_range(result_1, i, list_of_nums)
                    print(result_1)
                    break
                elif op2 == "*":
                    result_1, i = mul_range(result_1, i, list_of_nums)
                    print(result_1)
                    break
                elif op2 == "/":
                    result_1, i = div_range(result_1, i, list_of_nums)
                    print(result_1)
                    break
                elif op2 == "-":
                    result_1, i = sub_range(result_1, i, list_of_nums)
                    print(result_1)
                    break
        except ValueError:
            print("did not enter a number")
            break
