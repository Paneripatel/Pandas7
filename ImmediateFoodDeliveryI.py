'''
Pandas7

1 Problem 1 : Immediate Food Delivery I ( https://leetcode.com/problems/immediate-food-delivery-i/ )
'''

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = len(delivery)
    delivery = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']]
    res = round((len(delivery)/df)*100, 2)
    return pd.DataFrame({'immediate_percentage': [res]})