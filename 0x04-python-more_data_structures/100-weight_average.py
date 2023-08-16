#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) <= 0:
        return 0
    t_score = 0
    t_weight = 0
    average = 0
    for elements in my_list:
        score, weight = elements
        t_weight += weight
        t_score += score * weight
    average = t_score / t_weight
    return average
