def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest-lowest
    return {'lowest':lowest, 'highest':highest, 'range':r}

donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
result = find_range(donations)
print('Lowest: {0} Highest: {1} Range: {2}'.
      format(result['lowest'], result['highest'], result['range']))
