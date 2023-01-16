def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    # 1.
    for i in terms:
        terms_dict[i[0]] = i[2:]
    # 2.
    today_year, today_month, today_day = today.split(".")
    today = int(today_year)*12*28 + int(today_month)*28 + int(today_day)
    # 3.
    for idx, x in enumerate(privacies, start = 1):
        month_add_value = int(terms_dict.get(x[-1]))*28
        year = int(x[:4])*12*28
        month = x[5:7]
        day = x[8:10]
        month = (int(month)*28) + month_add_value
        date = year + month + int(day) - 1
        # 4. 
        if (today > date):
            answer.append(idx)
    return answer