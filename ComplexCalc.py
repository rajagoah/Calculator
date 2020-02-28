def add(list_of_nums):
    sum = 0
    for i in range(len(list_of_nums)):
        sum = sum + list_of_nums[i]
    print("the sum is: ", sum)

def mul(list_of_nums):
    mul = 1
    for i in range(len(list_of_nums)):
        prd = prd * list_of_nums[i]
    print("the prod is: ", prd)


if __name__=="__main__":
    print("enter the numbers you want to add \n")
    list_of_nums = []
    while True:
        input_nums = int(input())
        list_of_nums.append(input_nums)
        add(list_of_nums)
