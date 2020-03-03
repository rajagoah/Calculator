def add(list_of_nums):
    sum = 0
    for i in range(len(list_of_nums)):
        sum = sum + list_of_nums[i]
    return sum, len(list_of_nums)

def mul (list_of_nums,i):
    prod = 1
    for i in range(len(list_of_nums)):
        prod = prod * list_of_nums[i] * result
    return prod

def add_range(result, i, list_of_nums):
    sum = 0
    print(list_of_nums)
    for i in range(len(list_of_nums)):
        sum = result + list_of_nums[i]
    return sum, i

if __name__=="__main__":
    #Kick starting the accepting of records
    list_of_nums = []
    num1 = int(input("enter the number"))
    op = input("enter the operator")
    num2 = int(input("enter the second number"))
    list_of_nums.append(num1)
    list_of_nums.append(num2)
    if op == "+":
        result_1, i = add(list_of_nums)
        print(result_1)
    elif op == "*":
        result_1, i = mul(list_of_nums)
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
                    result_2, i = add_range(result_1, i, list_of_nums)
                    print(result_2)
                    break
                elif op2 == "*":
                    result = mul(list_of_nums)
                    print(result)
                    break
        except ValueError:
            print("did not enter a number")
            break
