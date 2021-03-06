# -*- coding:utf-8 -*-
import pandas as  pd
import time
import json
import sys
import os
module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from pyfiles.pyfuncs import *
from flask import Flask, request, render_template
app = Flask(__name__)

app.debug = True

func_filename = "Q:\\qa\\work_areas\\xkk\\do_not_delete\\workspace\\fun_dash\\files\\function_data.xlsx"
print ("Last Refresh ... {}" .format(time.ctime(os.path.getmtime(func_filename))))

df_out = read_dataframe(func_filename)
new_json_data = df_out[0]
pd_columns = df_out[1]

@app.route('/')
def dataIndex():
    ref = time.ctime(os.path.getmtime(func_filename))
    return render_template('data.html', columns=pd_columns, lst_ref =ref)
#workbranch code
@app.route('/fun_data')
def get_fun_data():
    df_out = read_dataframe(func_filename)
    new_json_data = df_out[0]
    return new_json_data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
