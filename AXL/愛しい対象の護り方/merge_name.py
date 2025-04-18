import pandas as pd

# 读取两个CSV文件
text_df = pd.read_csv('text.csv')
name_df = pd.read_csv('name.csv')

# 创建一个字典，用于快速查找id对应的name
name_dict = dict(zip(name_df['id'], name_df['name']))

# 更新disp列
for index, row in text_df.iterrows():
    # 检查条件：当前disp为空且name在name_dict中存在
    if pd.isna(row['disp']) or row['disp'] == '':
        if row['name'] in name_dict:
            text_df.at[index, 'disp'] = name_dict[row['name']]

# 保存更新后的text.csv
text_df.to_csv('text.csv', index=False)

print("更新完成！")