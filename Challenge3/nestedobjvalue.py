#""""""""""""""""""""""""""""""""""""""""""""""""""""""
#@author: Kapil Mahishi
#Created on  18/06/2023

#Description:-  Following python program retrieve value 
#of deep nested object by using key.

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""
from functools import reduce
from operator import getitem
import json

def get_key_value(dataset, keys):
    try:
      return reduce(getitem, keys, dataset)
    except (KeyError, IndexError):
      return None

dataset_input1 = {"a":{"b":{"c":"d"}}}
dataset_input2 = {"x":{"y":{"z":"a"}}}

key_input1 = "a/b/c"
key_input2 = "x/y/z"




key_inp_mod1 = (list(key_input1.split("/")))
key_inp_mod2 = (list(key_input2.split("/")))




print("Value for dataset1 and key1 - :",get_key_value(dataset=dataset_input1, keys=key_inp_mod1))

print("Value for dataset2 and key2 - :",get_key_value(dataset=dataset_input2, keys=key_inp_mod2))
