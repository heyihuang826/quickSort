# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:18:00 2023

@author: user
"""
from tqdm import tqdm
import random
import copy



def quicksort(arr, low, hight):
    if low >= hight:
        return
    medium_of_three = min(arr[low], arr[(low + hight) // 2], arr[hight])
    key_idx = random.randint(low, hight) #low if arr[low] == medium_of_three else (low + hight) // 2 if arr[(low + hight) // 2] == medium_of_three else hight
    pivot = arr[key_idx]
    
    #print(f"{arr} pivot = {pivot} {low}({arr[low]})-{(low + hight) // 2}({arr[(low + hight) // 2]})-{hight}({arr[hight]})")
    
    i = low
    if i == key_idx: i += 1 #不更改pivot
    
    #idx i 的左方為 < pivot, 右方為 > pivot
    for j in range(low, hight + 1):
        if arr[j] < pivot:
            if j == key_idx: continue #不更改pivot
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            if i == key_idx: i += 1 #不更改pivot
    
    if i > key_idx: i -= 1
    arr[i], arr[key_idx] = pivot, arr[i]
    quicksort(arr, low, i - 1)
    quicksort(arr, i + 1, hight)



for i in tqdm(range(10000)):
    #a = [8, 2, 8, 5, 11, 10, 4, 1, 9, 7, 3]
    #a = [1, 2, 3]
    #a = [75 , -20, 40 , -66, 41 , -32, -82, -67, 14 , -35]
    #a = [-9 , 5  , -6 , 6  , 9  , 10 , 7  , 3  , 3  , -10]
    a = random.choice(
        [[random.randint(-10, 10) for _ in range(random.choice([1, 10, 100, 1000, 10000]))], 
          [random.randint(-100, 100) for _ in range(random.choice([1, 10, 100, 1000, 10000]))], 
          [random.randint(-1000000, 1000000) for _ in range(random.choice([1000, 10000]))]
          ])
    # a = random.choice(
    #     [[random.randint(-10, 10) for _ in range(random.choice([1, 10, 100]))]
    #       ])
    #a = [3, 2, 1]
    b = list(a)
    #print('[', ', '.join(f"{str(i):<3}" for i in a), '] -> Q', sep = '')
    quicksort(a, 0, len(a) - 1)
    #print('[', ', '.join(f"{str(i):<3}" for i in a), '] -> result', sep = '')
    b.sort()
    #print('[', ', '.join(f"{str(i):<3}" for i in b), '] -> ans', sep = '')
    if a != b:
        raise Exception("ans error")
    #print(a == b)