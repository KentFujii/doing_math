def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest-lowest
    return lowest, highest, r

donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
lowest, highest, r = find_range(donations)
print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))
