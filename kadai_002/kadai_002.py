# -*- coding: utf-8 -*-
"""python-excel-kadai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mv59p8nFW_RSoM7oZhgo5mnVh4UVzbUJ
"""

import pandas as pd

# データフレームの作成
df = pd.DataFrame({
    '日付': ['2023-05-17', '2023-05-18', '2023-05-19', '2023-05-20', '2023-05-21'],
    '社員名': ['山田', '佐藤', '鈴木', '田中', '高橋'],
    '売上': [100, 200, 150, 300, 250],
    '部門': ['メーカー', '代理店', 'メーカー', '商社', '代理店'],
})

# 平均売上に50を加えた値を計算
average_sales_plus_50 = df['売上'].mean() + 50

# 新しい列 '平均売上' を作成
df['平均売上'] = df['売上'].mean()

# 新しい列 '業績ランク' を作成
df['業績ランク'] = pd.cut(df['売上'],
                         bins=[-float('inf'), df['売上'].mean(), average_sales_plus_50, float('inf')],
                         labels=['C', 'B', 'A'],
                         right=False)

# Excelファイルを作成
writer = pd.ExcelWriter('業務.xlsx')

# DataFrameオブジェクトをExcelファイルに書き込む
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Excelファイルを閉じる
writer.close()