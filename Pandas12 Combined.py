# Pandas12

# 1 Problem 1 : Managers with at Least 5 Direct Reports	( https://leetcode.com/problems/managers-with-at-least-5-direct-reports/ )

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby(['managerId']).size().reset_index(name = 'cnt')
    df = df[df['cnt']>=5]
    result = df.merge(employee, left_on = 'managerId', right_on ='id', how = 'inner')
    return result[['name']]

# 2 Problem 2 : Sales Person	(https://leetcode.com/problems/sales-person/ )

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    t1 = orders.merge(company, on = 'com_id', how ='left')
    t1 = t1[t1['name']=='RED']
    result = sales_person.merge(t1, on = 'sales_id', how = 'left')
    result = result[result['name_y'].isna()]
    return result[['name_x']].rename(columns = {'name_x':'name'})