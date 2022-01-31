list1 = [1, 3, 3, 5, 4]
dict1 = {}


def occurenceChecker(list2):
    for item in list2:
        dict1.update({str(item): 0})

    for item in list2:
        dict1[str(item)] += 1

    for key in dict1:
        if dict1[key] % 2 == 0:
            return False
    return True


print(occurenceChecker(list1))

# The Big O-notation of this program is: O(n)

