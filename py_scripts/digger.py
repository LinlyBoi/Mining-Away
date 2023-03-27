# Getting and combining data
import pandas as pd
import numpy as np

#reading the data
# -> MAKE SURE OF THE DATA FRAMES NAMES PEFORE YOU RUN IT




df1= pd.read_csv('output_6th_df.csv')
df2= pd.read_csv('vgsales-12-4-2019-short.csv')


#----------------------------------------------------------


#print(pf1.head)
#print(pf2.head)

#---------------------------------------------------------


#                    merging

df_compine= df1.merge(df2, left_on='Name',right_on='Name',how='left')
print(df_compine)
df_compine.to_csv('output_final_df.csv')
df = df_compine
output_df = 'N There U Have It'

#---------------------------------------------------------



#                          CLEANING -> REMOVING THE WORD REVIOW AND ANY THING AFTER IT




# nuke=df1['GameName'].to_list()
# nuke2 = list()

# for orphan in nuke : 
#     orphan = orphan.split('Review')[0]
#     nuke2.append(orphan)

# df1['GameName']=nuke


# print(df1)

# nuke_frame = pd.DataFrame(nuke2)
# df1=df1.drop(columns=['GameName'])

# df1['Name'] = nuke2

# df1.to_csv('output_6th_df.csv')
# print(df1)

