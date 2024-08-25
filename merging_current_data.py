import pandas as pd

df_2021 = pd.read_csv('data/2021-Medical-School-Applications.csv')
df_2022 = pd.read_csv('data/Med-School-Acceptance-Stats-2022.csv')
df_2023 = pd.read_csv('data/Med-School-Acceptance-Stats-2023.csv')

merge = pd.concat([df_2021, df_2022, df_2023]).groupby(['School']).sum().sort_values(by=['Total UC Berkeley Applicants'], ascending=False).reset_index()

print(merge)

merge.to_csv(f"data/aggregated_data.csv", index=False, header=True)

