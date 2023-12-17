# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:03:36 2023

@author: user
"""
from colorama import Fore, Style
from tqdm import tqdm
import random
import copy



def quicksort(arr, low, hight, trace_code = 'o'):
    if low >= hight:
        return
    #select pivot index
    #medium_of_three = min(arr[low], arr[(low + hight) // 2], arr[hight])
    key_idx = random.randint(low, hight) #low if arr[low] == medium_of_three else (low + hight) // 2 if arr[(low + hight) // 2] == medium_of_three else hight
    pivot = arr[key_idx] #pivot
    
    l, r = low, hight #l, r temp variable
    #idx r == l 的左方為 < pivot, 右方為 > pivot
    while(True):
        while((arr[r] >= pivot or r == key_idx) and l < r): r -= 1 #insure arr[r] < pivot or r == l
        while((arr[l] <= pivot or l == key_idx) and l < r): l += 1 #insure arr[l] > pivot or r == l
        if r <= l: #if r == l
            break
        else:
            arr[r], arr[l] = arr[l], arr[r] #swap arr[l], arr[r]
            #print('->[', ', '.join(f"{Fore.CYAN}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == l else f"{Fore.RED}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == r else f"{Fore.YELLOW}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == key_idx else f"{Fore.WHITE}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if low <= i <= hight else f"{Fore.WHITE}{Style.DIM}{str(arr[i]):<3}{Fore.RESET}" for i in range(len(a))), f'] {Fore.YELLOW}{Style.BRIGHT}{pivot}{Fore.RESET} trace {trace_code}', sep = '')
    if arr[r] < pivot and key_idx > r: r += 1 #because r runs before l, so it will be too left if smaller than pivot and make issue swaped to right side
    #print('  [', ', '.join(f"{Fore.CYAN}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == l else f"{Fore.RED}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == r else f"{Fore.YELLOW}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == key_idx else f"{Fore.WHITE}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if low <= i <= hight else f"{Fore.WHITE}{Style.DIM}{str(arr[i]):<3}{Fore.RESET}" for i in range(len(a))), f'] {Fore.YELLOW}{Style.BRIGHT}{pivot}{Fore.RESET} trace {trace_code}', sep = '')
    arr[r], arr[key_idx] = pivot, arr[r] #put pivot to appropriate index
    #print('  [', ', '.join(f"{Fore.CYAN}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == l else f"{Fore.RED}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == r else f"{Fore.YELLOW}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if i == key_idx else f"{Fore.WHITE}{Style.BRIGHT}{str(arr[i]):<3}{Fore.RESET}" if low <= i <= hight else f"{Fore.WHITE}{Style.DIM}{str(arr[i]):<3}{Fore.RESET}" for i in range(len(a))), f'] {Fore.YELLOW}{Style.BRIGHT}{pivot}{Fore.RESET} trace {trace_code}', sep = '')
    quicksort(arr, low, r - 1, trace_code + '-l') #sort left side
    quicksort(arr, r + 1, hight, trace_code + '-r') #sort right side



for i in tqdm(range(100)):
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