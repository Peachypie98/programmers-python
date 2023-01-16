def solution(numbers, hand):
    answer = ""
    left_pos = [3, 0]
    right_pos = [3, 2]
    mydict = {1:[0, 0], 2:[0, 1], 3:[0, 2], 4:[1, 0], 5:[1, 1], 6:[1, 2], 7:[2, 0], 8:[2, 1], 9:[2, 2], 0:[3, 1]}
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left_pos = mydict[num]
        elif num in [ 3, 6, 9]:
            answer += "R"
            right_pos = mydict[num]
        else:
            current_pos = mydict[num]
            left_diff = (abs(left_pos[0]-current_pos[0])) + (abs(left_pos[1]-current_pos[1]))
            right_diff = (abs(right_pos[0] - current_pos[0])) + (abs(right_pos[1] - current_pos[1]))
            if left_diff < right_diff:
                answer += "L"
                left_pos = current_pos
            elif right_diff < left_diff:
                answer += "R"
                right_pos = current_pos
            else:
                if hand == "right":
                    answer += "R"
                    right_pos = current_pos
                else:
                    answer += "L"
                    left_pos = current_pos
    return answer