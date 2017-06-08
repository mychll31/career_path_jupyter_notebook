# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 04:35:31 2016

@author: Animesh Kumar Jha
"""

import os
import json
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np

"""Change the current working directory"""
path=""

if(path==""):
    path=os.getcwd()

os.chdir(path)
"""End the Working Directory change snippet"""

def json_to_csv(newFile, outFile):
    myFile=open(newFile, 'r')
    myObject=myFile.read()
    myFile.close()
    myData=json.loads(myObject)
    myData = json_normalize(myData)
    myFrame=pd.DataFrame(myData)

    school_name = []
    end_date = []
    start_date = []
    degree = []
    field_of_study = []
    for j in range(0, myFrame.shape[0]):
        try: 
            if(pd.isnull(myFrame["educations"][j])):
                end_date.append("--undefined--")
                start_date.append("--undefined--")
                degree.append("--undefined--")
                field_of_study.append("--undefined--")
                school_name.append("--undefined--")
            else:
                res = json_normalize(myFrame["educations"][j])
                if 'degree' in res.columns:
                    degree.append(res.iloc[0]["degree"])
                else:
                    degree.append("--undefined--")
                if 'school-name' in res.columns:
                    school_name.append(res.iloc[0]["school-name"])
                else:
                    school_name.append("--undefined--")
                if 'end-date' in res.columns:
                    end_date.append(res.iloc[0]["end-date"])
                else:
                    end_date.append("--undefined--")
                if 'start-date' in res.columns:
                    start_date.append(res.iloc[0]["start-date"])
                else:
                    start_date.append("--undefined--")
                if 'field-of-study' in res.columns:
                    field_of_study.append(res.iloc[0]["field-of-study"])
                else:
                    field_of_study.append("--undefined--")
        except:
            try: 
                if(np.isnan(myFrame["educations"][j])):
                    school_name.append("--undefined--")
                    end_date.append("--undefined--")
                    start_date.append("--undefined--")
                    degree.append("--undefined--")
                    field_of_study.append("--undefined--")
            except:
                res = json_normalize(myFrame["educations"][j]) ##temporary
                #print(res)
                if 'degree' in res.columns:
                    degree.append(res.iloc[0]["degree"])
                else:
                    degree.append("--undefined--")
                if 'school-name' in res.columns:
                    school_name.append(res.iloc[0]["school-name"])
                else:
                    school_name.append("--undefined--")
                if 'end-date' in res.columns:
                    end_date.append(res.iloc[0]["end-date"])
                else:
                    end_date.append("--undefined--")
                if 'start-date' in res.columns:
                    start_date.append(res.iloc[0]["start-date"])
                else:
                    start_date.append("--undefined--")
                if 'field-of-study' in res.columns:
                    field_of_study.append(res.iloc[0]["field-of-study"])
                else:
                    field_of_study.append("--undefined--")
                 

    #print(myFrame.shape)
    #print(len(school_name))


    myFrame["educations-school-name"] = school_name
    myFrame["educations-end_date"] = end_date
    myFrame["educations-start_date"] = start_date
    myFrame["educations-degree"] = degree
    myFrame["educations-field_of_study"] = field_of_study

    del myFrame["educations"]

    title = []
    is_current = []
    company_name = []
    for j in range(0, myFrame.shape[0]):
        try: 
            if(pd.isnull(myFrame["positions"][j])):
                title.append("--undefined--")
                is_current.append("--undefined--")
                company_name.append("--undefined--")
            else:
                res = json_normalize(myFrame["positions"][j])
                if 'title' in res.columns:
                    title.append(res.iloc[0]["title"])
                else:
                    title.append("--undefined--")
                if 'is-current' in res.columns:
                    is_current.append(res.iloc[0]["is-current"])
                else:
                    is_current.append("--undefined--")
                if 'company-name' in res.columns:
                    company_name.append(res.iloc[0]["company-name"])
                else:
                    company_name.append("--undefined--")
        except:
            try: 
                if(np.isnan(myFrame["positions"][j])):
                    title.append("--undefined--")
                    is_current.append("--undefined--")
                    company_name.append("--undefined--")
            except:
                myFrame["positions"][j] ##temporary
                # print(myFrame["positions"][j])
                title.append("--undefined--")
                is_current.append("--undefined--")
                company_name.append("--undefined--")

    myFrame["positions-title"] = title
    myFrame["positions-is-current"] = is_current
    myFrame["positions-company-name"] = company_name

    del myFrame["positions"]

    myFrame.to_csv(outFile, index=False)
