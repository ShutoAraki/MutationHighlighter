#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:52:34 2017

@author: Shuto Araki
"""

def highlightMutation(filename, protein_num, hbond, namesel):
    import csv

    # read a csv file
    f = open(filename, 'rU')
    data = csv.reader(f)

    # List: (list(pdbId), list(residue #), list(label) (the value)
    pdbIdL = []
    residueL = []
    labelL = []

    # add elements to the lists and the set
    for row in data:
        pdbIdL.append(row[2])
        residueL.append(row[7])
        labelL.append(row[4])

    # Set: pick all the unique values
    pdbIds = sorted(set(pdbIdL), key=pdbIdL.index)

    # clean up the data
    pdbIds.remove('PDB ID')
    pdbIdL.remove('PDB ID')
    residueL.remove('PDB seq number')
    labelL.remove('mutation')


    dataSet = [pdbIdL, residueL, labelL]

    f.close()

    numbers = []

    for i in range(len(list(dataSet))):
        numbers.append(0)
        for item in dataSet[0]:
            if item == list(pdbIds)[i]: numbers[i] += 1


    # execute chimera commands
    from chimera import runCommand as rc

    rc('close all')
    # openc = 'open biounitID:' + list(pdbIds)[protein_num] + ".1"
    openc = "open " + list(pdbIds)[protein_num]
    rc(openc)
    rc('~display; ribbon; background solid black; color #c71caaaa84bd,r')

    colorc = []
    labelc = []
    nameselc = []
    selectString = "sel:"

    #labelc2 = []

    # which index to start slicing from?
    def start(p):
        start = 0
        for i in range(p):
            start += numbers[i]
        return start

    begin = start(protein_num)
    end = begin + numbers[protein_num]

    for i in range(begin, end):
        resNum = dataSet[1][i]
        label = dataSet[2][i]

        # label2 = ""
        # for c in label:
        #     from Ilabel import *
        #     letter = Character(letter, c, fontName='Sans Serif', size=50)
        #     label2.append(letter)
        # labelc2.append(('setattr r label "' + label2 + '" :' + resNum)

        colorc.append('color red :' + resNum)
        labelc.append('setattr r label "' + label + '" :' + resNum)
        nameselc.append('sel: ' + resNum + '; namesel ' + label)
        if i == end-1:
            selectString += resNum
        else:
            selectString += resNum + ","

    # clear all the named selections
    for i in range(len(dataSet[2])):
        try:
            rc("~namesel " + dataSet[2][i])
        except:
            pass


    # execution of the commands
    for i in range(len(colorc)):
        rc(colorc[i])
        rc(labelc[i])
        if namesel == 1:
            rc(nameselc[i])

    # show any H-bonds to mutant positions
    rc(selectString)
    if hbond == 1:
        rc('hbond selRestrict any reveal true')
    rc('color byelement')
    rc('focus')
    rc('~sel')
