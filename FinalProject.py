# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:59:19 2021

@author: Emilee
"""
############################## import ##########################################
import tkinter as tk


root = tk.Tk()

############################## size of window ##################################
canvas = tk.Canvas(root, width=700, height=400, bg="#4682B4")
canvas.grid(columnspan=3,rowspan=6)

########################## math ################################################################

def payment(event, loan, payment, interest, lblPayment):
    if loan.get() and interest.get() and period.get():
        #convert Entry Boxes to numbers
        years = int(period.get())
        months = years * 12
        rate = float(interest.get())
        loan = int(loan.get())
        # Calculate The Loan
        # Monthly Interest Rate
        monthly_rate = rate / 100 / 12 
        # Get  Payment
        payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
        # Format Payment
        payment = f"{payment:,.2f}"
        # Output Payment to the screen
        lblPayment["text"] = "Monthly Payment: $(¥)" + str(payment)
    else:
        lblPayment["text"] = "You forgot to enter some information (你忘记输入信息)..."


############################## English Window ######################################################

def openEn():
    pageEn = tk.Toplevel(canvas,bg="#4682B4")
    btnexit = tk.Button(pageEn, text="Exit",font="Stencil", bg="#98FB98", fg="#000000" ,command=pageEn.destroy)
    btnexit.grid(column=1,row=1)
    enpage = tk.Canvas(pageEn,width=700, height=400,bg="#4682B4")
    enpage.grid(columnspan=7,rowspan=10)
    
    ########## entry boxes english window #####################
   
    global loan
    loan = tk.Entry(pageEn)
    loan.grid(column=1,row=3)
    global interest
    interest = tk.Entry(pageEn)
    interest.grid(column=1,row=4)
    global period
    period = tk.Entry(pageEn)
    period.grid(column=1,row=5)
    
    ########## labels english window ##################
    
    
    lblloan = tk.Label(pageEn, text="Enter the amount of your loan:")
    lblloan.grid(column=0,row=3)
    lblinterest = tk.Label(pageEn, text="Enter your interest rate % :")
    lblinterest.grid(column=0,row=4)
    lblperiod = tk.Label(pageEn, text="Enter the period of your loan (in years):")
    lblperiod.grid(column=0,row=5)
    lblPayment = tk.Label(pageEn, text="Your monthly payment is:")
    lblPayment.grid(column=1, row=7)
    
    
    ################################# buttons English window #####################################################   
    btnEnter = tk.Button(pageEn, text="Enter", font="Stencil", bg="#98FB98", fg="#000000")
    btnEnter.bind("<Button-1>", lambda event: payment(event, loan, payment, interest, lblPayment))
    btnEnter.grid(column=1,row=9)
	
	
 
 

        
 
    
    
 
######################################### Chinese Window ###################################################    


def openCh():
    pageCh = tk.Toplevel(canvas,bg="#4682B4")
    btnleave = tk.Button(pageCh, text="退出窗口",font="Stencil", bg="#98FB98", fg="#000000" ,command=pageCh.destroy)
    btnleave.grid(column=1,row=1)
    chpage = tk.Canvas(pageCh,width=700, height=400,bg="#4682B4")
    chpage.grid(columnspan=7,rowspan=10)

    ################################## entry boxes chinese window #####################################################

   
    global loan
    loan = tk.Entry(pageCh)
    loan.grid(column=1,row=3)
    global interest
    interest = tk.Entry(pageCh)
    interest.grid(column=1,row=4)
    global period
    period = tk.Entry(pageCh)
    period.grid(column=1,row=5)

    ################################# labels chinese window ########################################################
  
   
    lblloan = tk.Label(pageCh, text="输入您的贷款金额:")
    lblloan.grid(column=0,row=3)
    lblinterest = tk.Label(pageCh, text="输入您的利率 % :")
    lblinterest.grid(column=0,row=4)
    lblperiod = tk.Label(pageCh, text="输入您的贷款期限（年）:")
    lblperiod.grid(column=0,row=5)
    lblPayment = tk.Label(pageCh, text="你的每月付款是:")
    lblPayment.grid(column=1, row=7)
    

    ############################## buttons chinese page ################################################

    btnEnter = tk.Button(pageCh, text="输入按钮", font="Stencil", bg="#98FB98", fg="#000000" )
    btnEnter.bind("<Button-1>", lambda event: payment(event, loan, payment, interest, lblPayment))
    btnEnter.grid(column=1,row=9)

  




############################## front page greeting  ##################################

greeting = tk.Label(root, text="Please choose your language (选择你的语言)", font="Impact",bg="#4682B4",fg="#000000")
greeting.grid(columnspan=7,column=0,row=0)


############################## front page language button ##############################################

btnChinese = tk.Button(root, text="汉语 (Chinese)", font="Stencil", bg="#98FB98", fg="#000000", command=openCh)
btnChinese.grid(column=1,row=1)
btnEnglish = tk.Button(root, text="English (英语)", font="Stencil", bg="#98FB98", fg="#000000",command=openEn)
btnEnglish.grid(column=1,row=2)




root.mainloop()