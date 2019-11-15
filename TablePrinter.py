#! Python3
#


def print_table(table_list):
    maxlength = determine_max_length(table_list)
    for i in range(len(table_list[0])):
        for j in range(len(table_list)):
            print(table_list[j][i].rjust(maxlength[j] + 1), end='')
        print()


def determine_max_length(tablelist):
    maxlength = [0] * len(tablelist)
    for i in range(len(tablelist)):
        for string in tablelist[i]:
            maxlength[i] = len(string) if len(string) > maxlength[i] else maxlength[i]
    return maxlength


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
