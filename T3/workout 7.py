def counter(Num1,Num2): # ساختن تابع با دو ارگومان با نام های دلخواه
    
    if(Num1 == 0):# در این خط شرط چک میکند که عدد موجود در ارگوامان اول با صفر برار است یا خیر
        print("STOP") #اگر عدد ارگومان اول با صفر برار بود شرط صحیح و متوقف میشود و عبارت در پرینت را چاپ میکند
        
    else:#اگر شرط صحیح نبود
        
        print(Num1-Num2)#عدد در ارگومان اول و عدد ارگوامان دوم را از هم کم و چاپ کرده
        counter(Num1-Num2,Num2)#عدد ارگومان اول و دوم را از هم کم میکند و به همراه ارگومان دوم به تابع بر میگرداند
counter(80,10) #تابع را فراخانی و ارگومان های ورودی را به تابع میدهیم