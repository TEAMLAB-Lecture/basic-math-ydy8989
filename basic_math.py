#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list)/len(number_list)
    return mean


def get_median(number_list):
    lstsorted = sorted(number_list)
    lstlen = len(number_list)
    idx = (lstlen-1)//2
    if lstlen % 2:
        return lstsorted[idx]
    else:
        return (lstsorted[idx]+lstsorted[idx+1])/2.0
