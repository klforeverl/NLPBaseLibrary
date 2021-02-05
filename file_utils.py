# -*- coding: utf-8 -*-
"""
   Description :
   Author :       ZhangLan
   date：          2021/2/5
"""

def read_file(file_name):
    """
    按行读取文件.

    Args:
        file_name: 文件名.

    Returns:
        list of data.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines