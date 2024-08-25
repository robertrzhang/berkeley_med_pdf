import csv
import pandas as pd

def formatFile(txt_path):
    with open(txt_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        col_names = ["School", 
        "Total UC Berkeley Applicants", 
        "Total UC Berkeley Applicants Matriculated", 
        "First Time Applicants Matriculated", 
        "Re-applicants Matriculated"]

        # for i in range(5):
        #     col_names.extend(next(reader))

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
            r = r[0].strip()
    #        print(r)
            if r.isdigit():
                if s:
                    arr[0].append(f'{s.strip()}')
                    s = ""
                    count += 1
                arr[count].append(r)
                count += 1
            else:
                count = 0
                s = s + " " + r
        
        # for i in arr:
        #     print(len(i))
        dic = {}
        name = txt_path.split("/")[-1]
        name = name.split(".")[0]
        for i in range(5):
            # print(col_names[i])
            dic.update({col_names[i]:arr[i]})
        df = pd.DataFrame(dic)
        df.to_csv(f"data/{name}.csv", index=False, header=True)
        print(f"Text extraction complete. Check 'data/{name}.csv' for results.")

if __name__ == "__main__":
    
    pdf_path = input("Enter your path to your file from root: ")
    try:
       formatFile(pdf_path)
    except FileNotFoundError:
        print("Your file name does not exist!")


    
