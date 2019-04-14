import pandas as  pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

df= pd.read_csv('2Basic_drug_recommender.csv', sep=',')


def test(var1):
    query= var1
    choices = list(df['condition'].unique())
    k=process.extractOne(query, choices)
    d=k[0]
    b= df[df['condition']==d]
    k=df[df['condition']==d]
    g = k.groupby('drugName').agg({'rating':['mean','count'],'Pred_SE':'mean','Pred_E':'mean','usefulCount_y':'mean'})

    g.columns=g.columns.get_level_values(0)
    g.columns = ['rating_mean','rating_count','Pred_SE','Pred_E','usefulCount']
    ki=list(g.sort_values(by=['rating_count','rating_mean','Pred_SE', 'Pred_E','usefulCount'],ascending=[False,False,True, False, False]).iloc[0:3].index)
    se=g.sort_values(by=['rating_count','rating_mean','Pred_SE', 'Pred_E','usefulCount'],
                      ascending=[False,False,True, False, False])
    return ki[0],ki[1],ki[2],str(round(se.iloc[0,2], 3)),str(round(se.iloc[1,2], 3)),str(round(se.iloc[2,2], 3)),str(round(se.iloc[0,3], 3)),str(round(se.iloc[1,3], 3)),str(round(se.iloc[2,3], 3)),d
