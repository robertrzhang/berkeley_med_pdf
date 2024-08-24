import csv
import pandas as pd

with open("output.txt", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    col_names = []
    for i in range(5):
        col_names.extend(next(reader))

    school = []
    tot_berk = []
    tot_berk_mat = []
    first_time = []
    re_mat = []
    arr = [school, tot_berk, tot_berk_mat, first_time,re_mat]
    s = ""
    count = 0

    for r in reader:

        if not r:
            continue
        r = r[0]
#        print(r)
        if r.isdigit():
            if s:
                arr[0].append(s)
                s = ""
                count += 1
            arr[count].append(r)
            count += 1
        else:
            count = 0
            s += r
    

    dic = {}
    for i in range(5):
        # print(col_names[i])
        dic.update({col_names[i]:arr[i]})
    df = pd.DataFrame(dic)
    df.to_csv("better_formatted.csv", sep='\t', index=False, header=True)
    
