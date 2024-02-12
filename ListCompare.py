def calculate_average(input_list):
    """
    Рассчитать среднее значение списка.

    :param input_list: Список чисел.
    :return: Среднее значение.
    """
    if len(input_list) == 0:
        return 0
    return sum(input_list) / len(input_list)


class ListCompare:
    """
    Этот класс сравнивает средние значения двух списков.
    """

    def __init__(self, list_one, list_two):
        """
        Конструктор класса.

        :param list_one: Первый список чисел.
        :param list_two: Второй список чисел.
        """
        self.list_one = list_one
        self.list_two = list_two

    def compare_lists(self):
        """
        Сравнить средние значения двух списков и вернуть сообщение.

        :return: Сообщение, указывающее, какой список имеет большее среднее значение.
        """
        average_one = calculate_average(self.list_one)
        average_two = calculate_average(self.list_two)

        if average_one > average_two:
            return "Первый список имеет большее среднее значение"
        if average_one < average_two:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
