import math


# Функция для расчета среднего значения
def mean(data):
    return sum(data) / len(data)


# Функция для расчета корреляции Пирсона
def pearson_correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator = math.sqrt(
        sum((x[i] - mean_x) ** 2 for i in range(len(x))) * sum((y[i] - mean_y) ** 2 for i in range(len(y))))

    correlation = numerator / denominator
    return correlation


# Пример использования
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

print("Корреляция Пирсона:", pearson_correlation(x, y))