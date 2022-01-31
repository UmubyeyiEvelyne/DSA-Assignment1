
def sum_largest(l,list2):
    if l <= len(list2):
        list2.sort(reverse=True)
        sum = 0
        for number in list2[0:l]:
            sum +=number
        return sum
    else:
        return "K is greater than the list size!"


def main():
    list1 = [3, 7, 5, 12, 6]
    k = 3
    print(sum_largest(k,list1))


if __name__ == "__main__":
    main()
