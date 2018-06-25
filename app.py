# -*- coding:utf-8 -*-
import pandas as  pd
import time
import os
import json

from flask import Flask, request, render_template
app = Flask(__name__)

app.debug = True

print ("Last Refresh ... {}" .format(time.ctime(os.path.getmtime('Q:\\qa\\work_areas\\xkk\\do_not_delete\\workspace\\fun_dash\\files\\function_data.xlsx'))))
pd.set_option('display.max_colwidth', -1)
df = pd.read_excel("Q:\\qa\\work_areas\\xkk\\do_not_delete\\workspace\\fun_dash\\files\\function_data.xlsx")
me = df['Func Indus Resp'].str.contains('HT1')
nt_rel = df['Func State'] != 'Released'
release = df['Func Regular Name'].str.contains('FD04')
imp_st = df['Implement State'] == 'Done'
qaj = df['QA Judgment'].str.contains('Red')
new_df=df[me & release&nt_rel]
pd_columns = df.columns
json_data = new_df.to_json(orient='records')
s1 = '{\"data\" :'
s2 = "}"
new_json_data = s1+json_data+s2
print (pd_columns)

@app.route('/')
def dataIndex():
    return render_template('data.html', columns=pd_columns)
    return 'Hello Data World!'

@app.route('/fun_data')
def get_fun_data():
    return new_json_data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
