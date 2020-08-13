# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:15:59 2020
@author: U201812776 孟治宇
"""

from datetime import datetime

def is_leap(year):
    isLeap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return isLeap

def get_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 30


def main():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    total = 0
    for m in range(1, month):
        total += get_days(year, m)
    total += day
    print(f'今天是{year}年{month}月{day}日是{year}年')
    print(f'{year}年{month}月{day}日是{year}年的第{total}天')


if __name__ == '__main__':
    main()