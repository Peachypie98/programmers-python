def solution(numbers, target):
    calc = []
    calc_temp = []
    calc.append(numbers[0])
    calc.append(-numbers[0])
    for i in range(1, len(numbers)):
        for j in range(len(calc)):
            calc_temp.append(calc[j] + numbers[i])
            calc_temp.append(calc[j] - numbers[i])
        calc = calc_temp.copy()
        calc_temp = []
    answer = calc.count(target)
    return answer
print(solution([1,2,3],0))