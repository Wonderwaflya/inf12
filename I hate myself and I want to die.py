"""
2.29. Сформировать матрицу размера 4 на 4. Матрица заполняется вручную строками, каждая из которых может
иметь не более 5 символов в длину. Допустимыми символами являются цифры и буквы английского алфавита. Каждая строка
рассматривается как число в некоторой системе счисления. Про-анализировать содержимое данной матрицы и сформировать
на ее основе дру-гую, элементами которой будут числа, являющиеся минимально возможными основаниями системы счисления
для соответствующих элементов исходной мат-рицы. Результаты преобразований вывести на экран.
"""
# Рекурсивная функция для получения способа заполнения матрицы элементами.
def matrix_input_type() -> bool:
    print("Введите число для выбора способа ввода данных:")
    print("1 —  для автоматического заполнения матрицы случайным образом;")
    print("0 — для ввода элементов вручную.")
    choice: str = input("Ваш выбор (0 или 1): ")
    if choice == "":
        print("[Ошибка]: На вход получена пустая строка.")
        print("Повторите ввод данных.")
        return matrix_input_type()
    quantity: int = 0
    for symbol in choice:
        quantity += 1
        if quantity > 1:
            print("[Ошибка]: Неверный тип входных данных.")
            print("Повторите ввод данных, учитывая, что на вход подаётся только одно число.")
            return matrix_input_type()
        if ord(symbol) < 48 or ord(symbol) > 49:
            print("[Ошибка]: Выход за границы диапазона.")
            print("Повторите ввод данных, учитывая, что на вход подаётся либо 0, либо 1.")
            return matrix_input_type()
    return bool(int(choice))


# Рекурсивная функция для получения элемента матрицы с помощью интерактивного ввода.
def matrix_element_input(index: int, n_columns: int) -> str:
    coord_i: int
    coord_j: int
    element: str
    quantity: int
    coord_i = index // 4 + 1
    coord_j = index % 4 + 1
    element = input(f"Введите элемент {coord_i}-ой строки {coord_j}-ого столбца матрицы: ")
    if element == "":
        print("[Ошибка]: На вход получена пустая строка.")
        print("Повторите ввод данных.")
        return matrix_element_input(index, n_columns)
    quantity = 0
    for symbol in element:
        quantity += 1
        if quantity > 5:
            print("[Ошибка]: Выход за границы диапазона.")
            print("Повторите ввод данных, учитывая, что на вход подаётся строка, длиной не бльше 5.")
            return matrix_element_input(index, n_columns)
        if ord(symbol) < 48 or ord(symbol) > 122 or 90 < ord(symbol) < 97 or 57 < ord(symbol) < 65:
            print("[Ошибка]: Неверный тип входных данных.")
            print("Повторите ввод данных, учитывая, что на вход подаётся строка из букв английского алфавита и цифр.")
            return matrix_element_input(index, n_columns)
    return element



# Функция для получения матрицы, заполненной элементами.
def matrix_input(input_type: bool) -> [str]:
    matrix: [str] = [""] * 16
    if input_type == 1:
        import random
        s: str
        upper_case: int
        ch: str = ""
        element: str
        for index in range(16):
            s = ""
            length = random.randint(1, 5)
            for ch_i in range(length):
                upper_case = random.randint(0, 2)
                if upper_case == 0:
                    # chr("65") = 'A', ... , chr("90") = 'Z'
                    ch = chr(random.randint(65, 90))
                    s += ch
                elif upper_case == 1:
                    # chr("97") = 'a', ... , chr("122") = 'z'
                    ch = chr(random.randint(97, 122))
                    s += ch
                else:
                    # chr("48") = '0', ... , chr("57") = '9'
                    ch = chr(random.randint(48, 57))
                    s += ch
            matrix[index] = s
    else:
        print("Заполняйте матрицу поэлементно.")
        for index in range(16):
            element = matrix_element_input(index, 4)
            matrix[index] = element
    return matrix


# Процедура вывода матрицы matrix размером m * n.
def matrix_output(matrix: [str]):
    for i in range(4):
        print("(", end=" ")
        for j in range(4):
            if j == 4 - 1:
                print(matrix[i * 4 + j], ")")
            else:
                print(matrix[i * 4 + j], end=" ")


#функция для получения матрицы, состоящей из оснований систем счисления
def element_base(matrix: [str]):
    mtrx: [str] = []
    for element in matrix:
        element = element.lower()
        base = 0
        c = 0
        for i in element:
            if i.isalpha():
                c = int(ord(i) - 87) + 1
            else:
                c = int(i) + 1
        if base < c:
            base = c
        mtrx.append(str(base))
    return mtrx


# Главная функция.
def main():
    #matrix: [str] = matrix_input()
    input_type: bool = matrix_input_type()
    matrix: [str] = matrix_input(input_type)
    print("Созданная матрица:")
    matrix_output(matrix)
    print("Матрица с элементами, являющимися минимально возможными основаниями системы счисления для соответствующих элементов исходной матрицы:")
    mtrx: [str] = element_base(matrix)
    matrix_output(mtrx)


if __name__ == "__main__":
    try:
        main()
    except:
        print('Упс, видимо вы допустили ошибку, такую как: KeyboardInterruption, EOFError, ValueError или TypeErrorё')

