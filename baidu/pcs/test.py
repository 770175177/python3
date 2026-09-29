#!/bin/python3


from baidupcsapi import PCS

# 使用你的百度账号信息初始化
pcs = PCS('19960786641', 'lh@770175177')

# 查询存储空间
print(pcs.quota().content)

# 获取根目录文件列表
print(pcs.list_files('/').content)
