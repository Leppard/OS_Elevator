#!/usr/bin/python
#coding=utf-8  

import wx
floor_list_4 = []
floor_list_5 = []
current_floor_1 = 1
import time
import threading

floor_list_1 = []
floor_list_2 = []
floor_list_3 = []
current_floor_2 = 1
current_floor_3 = 1
current_floor_4 = 1
current_floor_5 = 1
Ele_1 = []
Ele_2 = []
Ele_3 = []
Ele_4 = []
Ele_5 = []


class NewFrame(wx.Frame):
    def __init__(self, parent, title):
    
        wx.Frame.__init__(self,parent, title=title, size=(1200,700))

        for i in range(20,0,-1):
            count_floor="%d"%i
            Str = count_floor+" "+"Floor"
            wx.StaticText(self,-1,Str,(1,(21-i)*25))        
        self.Centre()
        self.Show()

        btn_1 = []
        btn_2 = []
        btn_3 = []
        btn_4 = []
        btn_5 = []
        for i in range(1,6):
            Str = "%s"%i
            btn_1.append(wx.Button(self,-1,Str,pos=(100,i*20+550),size=(30,20)))
            btn_2.append(wx.Button(self,-1,Str,pos=(300,i*20+550),size=(30,20)))
            btn_3.append(wx.Button(self,-1,Str,pos=(500,i*20+550),size=(30,20)))
            btn_4.append(wx.Button(self,-1,Str,pos=(700,i*20+550),size=(30,20)))
            btn_5.append(wx.Button(self,-1,Str,pos=(900,i*20+550),size=(30,20)))
        for i in range(6,11):
            Str = "%s"%i
            btn_1.append(wx.Button(self,-1,Str,pos=(130,(i-5)*20+550),size=(30,20)))
            btn_2.append(wx.Button(self,-1,Str,pos=(330,(i-5)*20+550),size=(30,20)))
            btn_3.append(wx.Button(self,-1,Str,pos=(530,(i-5)*20+550),size=(30,20)))
            btn_4.append(wx.Button(self,-1,Str,pos=(730,(i-5)*20+550),size=(30,20)))
            btn_5.append(wx.Button(self,-1,Str,pos=(930,(i-5)*20+550),size=(30,20)))
        for i in range(11,16):
            Str = "%s"%i
            btn_1.append(wx.Button(self,-1,Str,pos=(160,(i-10)*20+550),size=(30,20)))
            btn_2.append(wx.Button(self,-1,Str,pos=(360,(i-10)*20+550),size=(30,20)))
            btn_3.append(wx.Button(self,-1,Str,pos=(560,(i-10)*20+550),size=(30,20)))
            btn_4.append(wx.Button(self,-1,Str,pos=(760,(i-10)*20+550),size=(30,20)))
            btn_5.append(wx.Button(self,-1,Str,pos=(960,(i-10)*20+550),size=(30,20)))
        for i in range(16,21):
            Str = "%s"%i
            btn_1.append(wx.Button(self,-1,Str,pos=(190,(i-15)*20+550),size=(30,20)))
            btn_2.append(wx.Button(self,-1,Str,pos=(390,(i-15)*20+550),size=(30,20)))
            btn_3.append(wx.Button(self,-1,Str,pos=(590,(i-15)*20+550),size=(30,20)))
            btn_4.append(wx.Button(self,-1,Str,pos=(790,(i-15)*20+550),size=(30,20)))
            btn_5.append(wx.Button(self,-1,Str,pos=(990,(i-15)*20+550),size=(30,20)))

        self.Bind(wx.EVT_BUTTON, self.OnClick_1_1,btn_1[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_2,btn_1[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_3,btn_1[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_4,btn_1[3])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_5,btn_1[4])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_6,btn_1[5])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_7,btn_1[6])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_8,btn_1[7])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_9,btn_1[8])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_10,btn_1[9])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_11,btn_1[10])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_12,btn_1[11])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_13,btn_1[12])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_14,btn_1[13])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_15,btn_1[14])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_16,btn_1[15])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_17,btn_1[16])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_18,btn_1[17])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_19,btn_1[18])
        self.Bind(wx.EVT_BUTTON, self.OnClick_1_20,btn_1[19])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_1,btn_2[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_2,btn_2[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_3,btn_2[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_4,btn_2[3])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_5,btn_2[4])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_6,btn_2[5])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_7,btn_2[6])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_8,btn_2[7])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_9,btn_2[8])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_10,btn_2[9])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_11,btn_2[10])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_12,btn_2[11])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_13,btn_2[12])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_14,btn_2[13])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_15,btn_2[14])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_16,btn_2[15])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_17,btn_2[16])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_18,btn_2[17])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_19,btn_2[18])
        self.Bind(wx.EVT_BUTTON, self.OnClick_2_20,btn_2[19])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_1,btn_3[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_2,btn_3[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_3,btn_3[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_4,btn_3[3])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_5,btn_3[4])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_6,btn_3[5])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_7,btn_3[6])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_8,btn_3[7])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_9,btn_3[8])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_10,btn_3[9])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_11,btn_3[10])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_12,btn_3[11])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_13,btn_3[12])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_14,btn_3[13])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_15,btn_3[14])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_16,btn_3[15])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_17,btn_3[16])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_18,btn_3[17])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_19,btn_3[18])
        self.Bind(wx.EVT_BUTTON, self.OnClick_3_20,btn_3[19])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_1,btn_4[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_2,btn_4[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_3,btn_4[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_4,btn_4[3])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_5,btn_4[4])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_6,btn_4[5])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_7,btn_4[6])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_8,btn_4[7])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_9,btn_4[8])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_10,btn_4[9])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_11,btn_4[10])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_12,btn_4[11])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_13,btn_4[12])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_14,btn_4[13])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_15,btn_4[14])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_16,btn_4[15])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_17,btn_4[16])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_18,btn_4[17])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_19,btn_4[18])
        self.Bind(wx.EVT_BUTTON, self.OnClick_4_20,btn_4[19])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_1,btn_5[0])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_2,btn_5[1])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_3,btn_5[2])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_4,btn_5[3])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_5,btn_5[4])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_6,btn_5[5])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_7,btn_5[6])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_8,btn_5[7])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_9,btn_5[8])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_10,btn_5[9])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_11,btn_5[10])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_12,btn_5[11])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_13,btn_5[12])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_14,btn_5[13])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_15,btn_5[14])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_16,btn_5[15])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_17,btn_5[16])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_18,btn_5[17])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_19,btn_5[18])
        self.Bind(wx.EVT_BUTTON, self.OnClick_5_20,btn_5[19])

    def OnClick_1_1(self,event):
        floor_list_1.append(1)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_2(self,event):
        floor_list_1.append(2)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_3(self,event):
        floor_list_1.append(3)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_4(self,event):
        floor_list_1.append(4)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_5(self,event):
        floor_list_1.append(5)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_6(self,event):
        floor_list_1.append(6)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_7(self,event):
        floor_list_1.append(7)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_8(self,event):
        floor_list_1.append(8)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_9(self,event):
        floor_list_1.append(9)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_10(self,event):
        floor_list_1.append(10)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_11(self,event):
        floor_list_1.append(11)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_12(self,event):
        floor_list_1.append(12)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_13(self,event):
        floor_list_1.append(13)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_14(self,event):
        floor_list_1.append(14)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_15(self,event):
        floor_list_1.append(15)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_16(self,event):
        floor_list_1.append(16)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_17(self,event):
        floor_list_1.append(17)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_18(self,event):
        floor_list_1.append(18)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_19(self,event):
        floor_list_1.append(19)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])
    def OnClick_1_20(self,event):
        floor_list_1.append(20)
        floor_list_1.sort()
        self.move_to_1(floor_list_1[0])

    def OnClick_2_1(self,event):
        floor_list_2.append(1)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_2(self,event):
        floor_list_2.append(2)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_3(self,event):
        floor_list_2.append(3)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_4(self,event):
        floor_list_2.append(4)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_5(self,event):
        floor_list_2.append(5)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_6(self,event):
        floor_list_2.append(6)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_7(self,event):
        floor_list_2.append(7)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_8(self,event):
        floor_list_2.append(8)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_9(self,event):
        floor_list_2.append(9)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_10(self,event):
        floor_list_2.append(10)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_11(self,event):
        floor_list_2.append(11)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_12(self,event):
        floor_list_2.append(12)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_13(self,event):
        floor_list_2.append(13)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_14(self,event):
        floor_list_2.append(14)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_15(self,event):
        floor_list_2.append(15)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_16(self,event):
        floor_list_2.append(16)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_17(self,event):
        floor_list_2.append(17)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_18(self,event):
        floor_list_2.append(18)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_19(self,event):
        floor_list_2.append(19)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])
    def OnClick_2_20(self,event):
        floor_list_2.append(20)
        floor_list_2.sort()
        self.move_to_2(floor_list_2[0])

    def OnClick_3_1(self,event):
        floor_list_3.append(1)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_2(self,event):
        floor_list_3.append(2)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_3(self,event):
        floor_list_3.append(3)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_4(self,event):
        floor_list_3.append(4)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_5(self,event):
        floor_list_3.append(5)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_6(self,event):
        floor_list_3.append(6)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_7(self,event):
        floor_list_3.append(7)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_8(self,event):
        floor_list_3.append(8)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_9(self,event):
        floor_list_3.append(9)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_10(self,event):
        floor_list_3.append(10)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_11(self,event):
        floor_list_3.append(11)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_12(self,event):
        floor_list_3.append(12)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_13(self,event):
        floor_list_3.append(13)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_14(self,event):
        floor_list_3.append(14)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_15(self,event):
        floor_list_3.append(15)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_16(self,event):
        floor_list_3.append(16)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_17(self,event):
        floor_list_3.append(17)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_18(self,event):
        floor_list_3.append(18)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_19(self,event):
        floor_list_3.append(19)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])
    def OnClick_3_20(self,event):
        floor_list_3.append(20)
        floor_list_3.sort()
        self.move_to_3(floor_list_3[0])

    def OnClick_4_1(self,event):
        floor_list_4.append(1)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_2(self,event):
        floor_list_4.append(2)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_3(self,event):
        floor_list_4.append(3)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_4(self,event):
        floor_list_4.append(4)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_5(self,event):
        floor_list_4.append(5)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_6(self,event):
        floor_list_4.append(6)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_7(self,event):
        floor_list_4.append(7)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_8(self,event):
        floor_list_4.append(8)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_9(self,event):
        floor_list_4.append(9)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_10(self,event):
        floor_list_4.append(10)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_11(self,event):
        floor_list_4.append(11)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_12(self,event):
        floor_list_4.append(12)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_13(self,event):
        floor_list_4.append(13)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_14(self,event):
        floor_list_4.append(14)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_15(self,event):
        floor_list_4.append(15)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_16(self,event):
        floor_list_4.append(16)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_17(self,event):
        floor_list_4.append(17)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_18(self,event):
        floor_list_4.append(18)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_19(self,event):
        floor_list_4.append(19)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])
    def OnClick_4_20(self,event):
        floor_list_4.append(20)
        floor_list_4.sort()
        self.move_to_4(floor_list_4[0])

    def OnClick_5_1(self,event):
        floor_list_5.append(1)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_2(self,event):
        floor_list_5.append(2)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_3(self,event):
        floor_list_5.append(3)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_4(self,event):
        floor_list_5.append(4)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_5(self,event):
        floor_list_5.append(5)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_6(self,event):
        floor_list_5.append(6)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_7(self,event):
        floor_list_5.append(7)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_8(self,event):
        floor_list_5.append(8)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_9(self,event):
        floor_list_5.append(9)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_10(self,event):
        floor_list_5.append(10)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_11(self,event):
        floor_list_5.append(11)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_12(self,event):
        floor_list_5.append(12)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_13(self,event):
        floor_list_5.append(13)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_14(self,event):
        floor_list_5.append(14)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_15(self,event):
        floor_list_5.append(15)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_16(self,event):
        floor_list_5.append(16)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_17(self,event):
        floor_list_5.append(17)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_18(self,event):
        floor_list_5.append(18)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_19(self,event):
        floor_list_5.append(19)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])
    def OnClick_5_20(self,event):
        floor_list_5.append(20)
        floor_list_5.sort()
        self.move_to_5(floor_list_5[0])

    def Repaint(self,Ele_,Elevator_,pos):
        Ele_[0].e1.Destroy()
        del Ele_[0]
        Ele_.append(Elevator_(NewFrame,pos))
        

    def move_to_1(self,aim_floor):
        if (aim_floor > current_floor_1):
            del floor_list_1[0]
            print current_floor_1,aim_floor
            for s in range((21-current_floor_1)*25,(21-aim_floor)*25-1,-1):
                timer=threading.Timer(1.0,self.Repaint(Ele_1,Elevator_1,s))
                timer.start()
#        current_floor_1 = aim_floor
        if (aim_floor < current_floor_1):
            self.move_down(aim_floor)
        if (aim_floor == current_floor_1):
            print "OK"

    def move_to_2(self,aim_floor):
        if (aim_floor > current_floor_2):
            del floor_list_2[0]
            print current_floor_2,aim_floor
            for s in range((21-current_floor_2)*25,(21-aim_floor)*25-1,-1):
                timer=threading.Timer(1.0,self.Repaint(Ele_2,Elevator_2,s))
                timer.start()
        if (aim_floor < current_floor_2):
            self.move_down(aim_floor)
        if (aim_floor == current_floor_2):
            print "OK"

    def move_to_3(self,aim_floor):
        if (aim_floor > current_floor_3):
            del floor_list_3[0]
            print current_floor_3,aim_floor
            for s in range((21-current_floor_3)*25,(21-aim_floor)*25-1,-1):
                timer=threading.Timer(1.0,self.Repaint(Ele_3,Elevator_3,s))
                timer.start()
        if (aim_floor < current_floor_3):
            self.move_down(aim_floor)
        if (aim_floor == current_floor_3):
            print "OK"

    def move_to_4(self,aim_floor):
        if (aim_floor > current_floor_4):
            del floor_list_4[0]
            print current_floor_4,aim_floor
            for s in range((21-current_floor_4)*25,(21-aim_floor)*25-1,-1):
                timer=threading.Timer(1.0,self.Repaint(Ele_4,Elevator_4,s))
                timer.start()
        if (aim_floor < current_floor_4):
            self.move_down(aim_floor)
        if (aim_floor == current_floor_4):
            print "OK"

    def move_to_5(self,aim_floor):
        if (aim_floor > current_floor_5):
            del floor_list_5[0]
            print current_floor_5,aim_floor
            for s in range((21-current_floor_5)*25,(21-aim_floor)*25-1,-1):
                timer=threading.Timer(1.0,self.Repaint(Ele_5,Elevator_5,s))
                timer.start()
        if (aim_floor < current_floor_5):
            self.move_down(aim_floor)
        if (aim_floor == current_floor_5):
            print "OK"


    def move_down(self,aim_floor):
        print "success"

class Elevator_1:
    def __init__(self,nframe,pos_floor):
        
        self.e1 = wx.Button(nframe,-1,' ',pos=(150,pos_floor),size=(20,25))
class Elevator_2:
    def __init__(self,nframe,pos_floor):
        
        self.e1 = wx.Button(nframe,-1,' ',pos=(350,pos_floor),size=(20,25))
class Elevator_3:
    def __init__(self,nframe,pos_floor):
        
        self.e1 = wx.Button(nframe,-1,' ',pos=(550,pos_floor),size=(20,25))
class Elevator_4:
    def __init__(self,nframe,pos_floor):
        
        self.e1 = wx.Button(nframe,-1,' ',pos=(750,pos_floor),size=(20,25))
class Elevator_5:
    def __init__(self,nframe,pos_floor):
        
        self.e1 = wx.Button(nframe,-1,' ',pos=(950,pos_floor),size=(20,25))



app = wx.App()
NewFrame = NewFrame(None,"电梯调度")
Ele_1.append(Elevator_1(NewFrame,500))
Ele_2.append(Elevator_2(NewFrame,500))
Ele_3.append(Elevator_3(NewFrame,500))
Ele_4.append(Elevator_4(NewFrame,500))
Ele_5.append(Elevator_5(NewFrame,500))
app.MainLoop()
