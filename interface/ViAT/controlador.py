# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:36:21 2020

@author: veroh
"""

from vista import ViAT
import sys
from PyQt5.QtWidgets import QApplication,QScrollArea
#%%
class Principal(object):
    def __init__(self):  
#        scroll_area = QScrollArea()
        self.__app=QApplication(sys.argv)
        self.__view=ViAT()
    def main(self):
        self.__view.show()
        sys.exit(self.__app.exec_())
#%%
p=Principal()
p.main()