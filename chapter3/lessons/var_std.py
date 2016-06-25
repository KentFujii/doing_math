def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff

def calculate_variance(numbers):
    diff = find_differences(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
variance = calculate_variance(donations)
print('The variance of the list of numbers is\t {0}'.format(variance))
std = variance**0.5
print('The standard deviation of the list of numbers is\t {0}'.format(std))
