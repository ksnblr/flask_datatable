import pandas as pd
import time
import os
pd.set_option('display.max_colwidth', -1)


def read_dataframe(filename):
    df = pd.read_excel(filename)

    # Dataframe filter variables
    me = df['Func Indus Resp'].str.contains('QUR')
    nt_rel = df['Func State'] != 'Released'
    release = df['Func Regular Name'].str.contains('FD04')
    imp_st = df['Implement State'] == 'Done'
    qaj = df['QA Judgment'].str.contains('Red')

    pd_columns = df.columns
    new_df = df[me&release&nt_rel]
    json_data = new_df.to_json(orient='records')
    s1 = '{\"data\" :'
    s2 = "}"
    return [s1+json_data+s2,pd_columns]
