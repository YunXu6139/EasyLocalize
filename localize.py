# -*- coding: utf-8 -*-
import pandas as pd
import os
import codecs

def generate_strings_files(excel_file):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file)

    # 检查是否有足够的数据
    if df.shape[1] < 2:
        print("Excel 文件至少需要两列数据：第一列为 key，其他列为不同语言的值。")
        return

    # 提取第一行作为文件名
    languages = df.columns[1:]  # 除去第一列
    keys = df.iloc[:, 0]  # 第一列是 key

    # 遍历每种语言，生成对应的 .strings 文件
    for idx, language in enumerate(languages):
        filename = u"{}.strings".format(language)  # 使用 Unicode 格式
        with codecs.open(filename, 'a', 'utf-8') as f:  # 使用 codecs 处理 UTF-8 编码
            for i, key in enumerate(keys):
                if pd.isnull(key):  # 跳过空的 key
                    continue
                value = df.iloc[i, idx + 1]
                if pd.isnull(value):  # 如果 value 为空，跳过
                    continue
                # 写入 "key" = "value"; 格式的字符串
                f.write(u'"{}" = "{}";\n'.format(key, value))  # 使用 Unicode 格式化字符串
        print(u"生成并写入 {} 成功！".format(filename))

if __name__ == "__main__":
    # 将 Excel 文件路径传入
    excel_path = raw_input("请输入 Excel 文件路径：").strip()  # raw_input 用于 Python 2
    if not os.path.isfile(excel_path):
        print("提供的文件路径无效，请检查后重试。")
    else:
        generate_strings_files(excel_path)
