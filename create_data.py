# coding=gbk
import json
from csv import excel

import pytest
import requests
import yaml
import xlrd

# with open("./data.yaml") as f:
#     data = yaml.load(f)
#     print("=========",data)
# data = [('qqaadd','hdd'),('tt111ds','yyw'),('zzdz','ppprrrd')]
def test_excel():
    wb = xlrd.open_workbook('excel_test/data.xlsx')
    sheet = wb.sheet_by_name('Sheet1')
    listAll = []
    for a in range(sheet.nrows):
        print()
        listStr = []
        for b in range(sheet.ncols):
            cols = sheet.col_values(b)
            listStr.append(cols[b])
        listAll.append(listStr)
    return listAll

@pytest.mark.parametrize("talk_domain,talk_intent,param_types,name1,name2,talk_reply",test_excel())
def test_a(talk_domain,talk_intent,param_types,name1,name2,talk_reply):
    url = "http://testdataquery.wsd.com/talkingmap/addOrUpdateTalkMap"
    name = name1.split("|")
    print("################################",name)
    nameList = name2.split("|")
    print("################################nameList", nameList)
    nameLen = len(name)
    if nameLen == 1:
        param1 = {
            "id": "",
            "talk_domain": talk_domain,
            "talk_intent": talk_intent,
            "param_types": param_types,
            "talk_param_input": [{
                "name": name[0],
                "value": [""]

            }],
            "talk_param_out": nameList,
            "talk_reply": talk_reply,
            "is_succ": True,
            "Operator": "v_vlnchen"
        }
        # r = requests.post(url, json=param1)
        # print(r.json())
        print()
        print(param1)
    elif nameLen == 2:
        param2 = {
            "id": "",
            "talk_domain": talk_domain,
            "talk_intent": talk_intent,
            "param_types": param_types,
            "talk_param_input": [{
                "name": name[0],
                "value": [""]

            },{
                "name": name[1],
                "value": [""]

            }
            ],
            "talk_param_out": nameList,
            "talk_reply": talk_reply,
            "is_succ": True,
            "Operator": "v_vlnchen"
        }
        # r = requests.post(url, json=param2)
        # print(r.json())
        print()
        print(param2)
    elif nameLen == 3:
        param3 = {
            "id": "",
            "talk_domain": talk_domain,
            "talk_intent": talk_intent,
            "param_types": param_types,
            "talk_param_input": [{
                "name": name[0],
                "value": [""]

            },{
                "name": name[1],
                "value": [""]

            },{
                "name": name[2],
                "value": [""]

            }
            ],
            "talk_param_out": nameList,
            "talk_reply": talk_reply,
            "is_succ": True,
            "Operator": "v_vlnchen"
        }
        # r = requests.post(url, json=param3)
        # print(r.json())
        print()
        print(param3)
def test_str():
    str = "TrackType|Lang"
    print(str.split("|")[0])
    print(str.split("|")[1])


