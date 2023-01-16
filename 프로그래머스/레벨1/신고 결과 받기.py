def solution(id_list, report, k):
    table = dict()
    table_count = dict()
    table2 = set()
    answer = []
    count = 0
    for i in id_list:
        table[i] = ""
        table_count[i] = 0
        for x in report:
            if(x.startswith(i)): # x is "muzi frodo", i = "muzi" (1st loop)
                table[i] += x[x.find(" "):] 
                table[i] = table[i].lstrip()
                
    # {'frodo': 0, 'neo': 0, 'muzi': 0}            
    for i in table.items(): # i = ('frodo', 'muzi neo neo')
        tmp = i[1].split() # tmp = ['muzi', 'neo', 'neo']
        for x in tmp: 
            table2.add(x) # table2 = ['muzi', 'neo']
            
        for y in table2:
            table_count[y] += 1
        table2.clear()
        
    # table        = {'frodo': 'muzi neo neo', 'neo': 'muzi frodo', 'muzi': 'neo frodo neo'} 
    # table_count  = {'frodo': 2, 'neo': 2, 'muzi': 2}  
    # tmp          = ['muzi', 'neo', 'neo'], ['muzi', 'frodo']
    
    for i in table:
        temp_l =[]
        temp_s = table[i]
        while " " in temp_s:
            ind = temp_s.index(" ")
            first_name = temp_s[0:ind]
            temp_s = temp_s[ind+1:]
            if first_name not in temp_l:
                temp_l.append(first_name)
        if temp_s not in temp_l:
            temp_l.append(temp_s)
        count2 = 0
        for j in temp_l:
            if j in table_count:
                if table_count[j] >= k:
                    count2 = count2 + 1
        answer.append(count2)
    return answer