def recursive_solution(result_sum: int, cur_number: int = 9, cur_sum: int = 0, result_str: str = "9") -> str:
    cur_digit = abs(cur_number) % 10 - 1
    # базис рекурсии
    if cur_digit == -1 and cur_sum + cur_number == result_sum:
        return f"{result_str} = {result_sum}"
    elif cur_digit == -1:
        return "No solution"

    sign = cur_number // abs(cur_number)
    # поместить на текущем шаге ничего
    res_1 = recursive_solution(result_sum,
                               cur_number=cur_number * 10 + sign * cur_digit,
                               cur_sum=cur_sum,
                               result_str=result_str + str(cur_digit))
    if res_1 != "No solution":
        return res_1
    # поместить плюс на текущем шаге
    res_2 = recursive_solution(result_sum,
                               cur_number=cur_digit,
                               cur_sum=cur_sum + cur_number,
                               result_str=result_str + " + " + str(cur_digit))
    if res_2 != "No solution":
        return res_2
    # поместить минус на текущем шаге
    res_3 = recursive_solution(result_sum,
                               cur_number=-cur_digit,
                               cur_sum=cur_sum + cur_number,
                               result_str=result_str + " - " + str(cur_digit))
    if res_3 != "No solution":
        return res_3

    return "No solution"


# для разнообразия вернем все возможные варинты
def iter_solution(result_sum) -> list[str]:
    answer = []
    # переберем все возможные варинты выражений
    for i in range(3 ** 9):
        # построим троичную маску
        mask = []
        for j in range(9):
            mask.append(i % 3)
            i //= 3
        # построим вариант выражения по маске, где
        # 0 - вставить пустой символ
        # 1 - вставить +
        # 2 - вставить -
        res_str = "9"
        for j in range(8, -1, -1):
            if mask[j] == 1:
                res_str += " +"
            if mask[j] == 2:
                res_str += " -"
            res_str += str(j)
        # найдем сумму полученной строки чисел
        cur_sum = sum(map(int, res_str.split()))
        if cur_sum == result_sum:
            answer.append(f"{res_str} = {result_sum}")
    return answer


if __name__ == '__main__':
    result_sum = 200
    print("Рекурсивное решение:")
    print(recursive_solution(result_sum))
    print("Итерационное решение:(все варианты)")
    variants = '\n'.join(iter_solution(result_sum))
    print(variants if variants else "No solution")
