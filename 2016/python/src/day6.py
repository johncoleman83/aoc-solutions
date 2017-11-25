#!/usr/bin/env python3
"""
Advent of Code 2016: Day 6
"""
import os

def readdayinput():
    """
    Reads day input to solve
    """
    thisfile = os.path.basename(__file__)
    thisfile = thisfile[:len(thisfile) - 3]
    if __name__ == "__main__":
        resource = "../resources"
    else:
        resource = "./resources"
    dayinputfile = "{}/{}input.txt".format(resource, thisfile)
    with open(dayinputfile, mode='r', encoding='utf-8') as fileio:
        dayinput = fileio.read()
    dayinput = dayinput.strip('\n')
    return dayinput

def sort_by_frequencies(alphas):
    """
    sorts string by frequencies
    """
    items = []
    temp = [alphas[0]]
    for x in range(1, len(alphas)):
        if alphas[x] == alphas[x - 1]:
            temp.append(alphas[x])
        else:
            items.append(''.join(temp))
            temp = [alphas[x]]
    items.append(''.join(temp))
    newa = ''.join([k[0] for k in sorted(items, key=lambda x: -len(x))])
    return newa

def find_repititions(dayinput):
    """
    first half solver:
    get message from repititions
    """
    lines = dayinput.split('\n')
    rotated = []
    rotated[:] = zip(*lines[::-1])
    rotated = [''.join(sorted(list(x))) for x in rotated]
    message = []
    for line in rotated:
        message.append(sort_by_frequencies(line)[0])
    return ''.join(message)

def app():
    """
    runs day application
    """
    print("Day #6:")
    dayinput = readdayinput()
    repitition_message = find_repititions(dayinput)
    print(repitition_message)


if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
