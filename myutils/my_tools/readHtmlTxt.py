# -*- coding: utf-8 -*-
"""
@Time : 2024/5/24 16:59
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : readHtmlTxt.py
"""
__author__ = "梦无矶小仔"

import re


# 定义一个函数来读取文件并提取所需内容
def extract_chinese_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式匹配所需的内容
    pattern = re.compile(r'<span[^>]*class="course-play__list-course-title"[^>]*>(.*?)</span>')
    matches = pattern.findall(content)

    # 返回匹配到的内容
    return matches


import os


def rename_files_with_prefix(directory):
    # 获取文件夹中的所有文件
    files = os.listdir(directory)

    # 对文件进行排序，以确保按顺序重命名
    files.sort()

    # 遍历文件并重命名
    for index, filename in enumerate(files, start=1):
        # 构建新的文件名，前缀加上顺序编号
        # 使用 zfill(3) 确保编号是三位数，不足三位的用0补齐
        new_filename = f"{str(index).zfill(3)}_{filename}"

        # 获取完整的文件路径
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)

        # 重命名文件
        os.rename(old_file, new_file)
        print(f"Renamed '{filename}' to '{new_filename}'")




if __name__ == '__main__':

    #################################
    #
    # # 指定文件路径
    # file_path = 'xx.txt'
    #
    # # 调用函数并打印结果
    # extracted_content = extract_chinese_content(file_path)
    # for index, content in enumerate(extracted_content):
    #     print(index + 1, "", content)
    ####################################
    # 文件加前缀
    directory_path = 'E:\M_Home\奶奶收音机音乐\赣南采茶戏'  # 替换为你的文件夹路径
    rename_files_with_prefix(directory_path)
    ##########################
