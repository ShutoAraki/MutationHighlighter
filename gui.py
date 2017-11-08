#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:59:02 2017

@author: Shuto Araki
"""

import os
from Tkinter import *
import chimera
from chimera.baseDialog import ModelessDialog
import MutationHighlighter as mh

#filename = os.path.abspath(os.path.join('/MutationHighlighter/', 'csvSample.csv'))
filename = os.path.dirname(__file__) + "/csvSample.csv"

def extractProteinNames():
    import csv
    f = open(filename, 'rU')
    data = csv.reader(f)

    proteins = []
    for row in data:
        proteins.append(row[0])
    proteins.remove('Gene ID')

    proteinNames = sorted(set(proteins), key = proteins.index)

    return proteinNames


proteinNames = extractProteinNames()
proteinMap = {}

for i in range(len(proteinNames)):
    proteinMap.update({proteinNames[i]:i})


class MutationDialog(ModelessDialog):

    name = "Rare Genetic Disease Mutation Highlighter"

    def fillInUI(self, parent):

        topText = Label(parent, text = "    Select Gene    ",
                        font = ("Helvetica", 13, "normal"))

        global hbond
        hbond = IntVar()
        cbA = Checkbutton(parent, text="detect H-bonds", variable=hbond)

        global namesel
        namesel = IntVar()
        cbB = Checkbutton(parent, text="create named selections", variable=namesel)

        global var
        var = StringVar(parent)
        var.set(proteinNames[0])
        options = OptionMenu(parent, var, *proteinNames)

        # Layouts
        topText.grid(row=0, column=0)
        options.grid(row=0, column=1)
        cbA.grid(row=1, column=0)
        cbB.grid(row=1, column=1)

    def Apply(self):
        protein_num = proteinMap[var.get()]
        mh.highlightMutation(filename, protein_num, hbond.get(), namesel.get())


chimera.dialogs.register(MutationDialog.name, MutationDialog)

dir, file = os.path.split(__file__)
icon = os.path.join(dir, 'ExtensionUI.tiff')
chimera.tkgui.app.toolbar.add(icon, lambda d=chimera.dialogs.display,
n=MutationDialog.name: d(n), MutationDialog.name, None)
