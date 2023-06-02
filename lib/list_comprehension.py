#!/usr/bin/env python3

def return_evens(num_list):
    num_comp = [i for i in num_list if i % 2 == 0]
    return num_comp

def make_exclamation(sentence_list):
    new_list = [f"{i}!" for i in sentence_list]
    return new_list