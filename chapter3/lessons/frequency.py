from collections import Counter
def frequency_table(numbers):
    table = Counter(numbers).most_common()
    table.sort()
    print('Number\tFrequency')
    for number in table:
        print('{0}\t{1}'.format(number[0], number[1]))

scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
frequency_table(scores)
