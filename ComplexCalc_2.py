def add(list_of_nums):
    sum = 0
    for i in range(len(list_of_nums)):
        sum = sum + list_of_nums[i]
    return sum,i

def mul (result, list_of_nums,i):
    prod = 1
    for i in range(len(list_of_nums)):
        prod = prod * list_of_nums[i] * result
    return prod

if __name__=="__main__":
    list_of_nums = []

    while True:
        try:
            num1 = int(input("enter the number"))
            op = input("enter operator")
            num2 = int(input("enter the second number"))
            list_of_nums.append(num1)
            list_of_nums.append(num2)
            if op == "+":
                result, i = add(list_of_nums)
                print(result)
                op = input("enter operator")
                if op == "*":
                    result = mul(result, list_of_nums, i)
                    print(result)
        except ValueError:
            print("did not enter a number")
            break
