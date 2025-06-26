'''
2 Problem 2 : Count Salary Categories ( https://leetcode.com/problems/count-salary-categories/ )
'''

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowdf = accounts[accounts['income']<20000]
    averagedf = accounts[(accounts['income'] >= 20000 ) & (accounts['income'] <= 50000)]
    highdf = accounts[accounts['income'] > 50000]

    return pd.DataFrame([['Low Salary', len(lowdf)], ['Average Salary', len(averagedf)], ['High Salary', len(highdf)]], columns = ['category', 'accounts_count'])