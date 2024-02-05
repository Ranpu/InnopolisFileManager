def recursive_sum(lst):
    total_sum = 0

    for element in lst:
        if isinstance(element, list):
            total_sum += recursive_sum(element)
        else:
            total_sum += element

    return total_sum


if __name__ == "__main__":
    # Примеры использования
    list1 = [1, 2, 3, 4, 5]
    print(f"Сумма элементов списка 1: {recursive_sum(list1)}")

    list2 = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(f"Сумма элементов списка 2: {recursive_sum(list2)}")

    list3 = [1, [2, [3, 4], 5], 6, [7, 8], [[[9, [10]]]]]
    print(f"Сумма элементов списка 3: {recursive_sum(list3)}")
