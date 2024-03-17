def solution(id_list, report, k):
    answer = []
    # output : answer(list)
    #0 delete duple- suiting apply
    report_li =[]
    for n in report : 
        if n not in report_li:
            report_li.append(n)
    #1. report : 1d -> 2d with splite both
    for i in range(len(report_li)):
        report_li[i]=report_li[i].split()
    #2. report : list -> dict
    v=[]
    for i in range(len(id_list)):
        li= []
        for m in range(len(report_li)):
            if id_list[i] == report_li[m][0]:
                li.append(report_li[m][1])
        v.append(li)
    dict1 =dict(zip(id_list,v))

    #3. count suiting 
    count_li = []
    for i in range(len(id_list)):
        count=0
        for values in dict1.values():
            for m in range(len(values)):  
                  if id_list[i] == values[m]:
                    count+=1
        count_li.append(count)
    dict2 = dict(zip(id_list,count_li))


    # 4. suting list
    suiting_li = []
    for suiting,v in dict2.items() :
        if v >= k:
            suiting_li.append(suiting)
    # 5. find the num of suited_id depends on suiting_id 
    for m,n in dict1.items():
        count=0
        for i in range(len(n)):
            for z in suiting_li:
                  if z == n[i]:
                        count +=1
        answer.append(count)

    return answer