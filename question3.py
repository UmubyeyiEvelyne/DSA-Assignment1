def knapsack(max_wei, number_of_pelettes, wei_list, val_list):
    options_table = [[0]*(max_wei +1)]*(number_of_pelettes+1)
    # for row in range(number_of_pelettes + 1):
    #     for column in range(max_wei + 1):
    #         options_table[row][column] = 0

    for row in range(1,number_of_pelettes + 1):
        for column in range(max_wei + 1):
            options_table[row][column] = options_table[row - 1][column]
            if (column >= wei_list[row-1]) and (options_table[row-1][column] < options_table[row-1][column-wei_list[row-1]] + val_list[row-1]):
                options_table[row][column] = options_table[row-1][column-wei_list[row-1]] + val_list[row-1]

            print(options_table[row][column], "")

        print("\n")

    print("These pellets would bring about the highest profit: ")

    for pelette in range(number_of_pelettes,0, -1):
        if options_table[pelette][max_wei] != options_table[pelette - 1][max_wei]:
            print(f"Pelette {pelette} whose weight is {wei_list[pelette-1]} and value {val_list - 1}")

            max_wei -= wei_list[pelette-1]
        pelette -= 1

    return f"The total profit from the selected pelettes is: {options_table[number_of_pelettes][max_weight]}"



max_weight = 8
pelettes = 4
weight_list = [2, 3, 4, 5]
value_list = [1, 2, 5, 6]
knapsack(max_weight,pelettes,weight_list,value_list)