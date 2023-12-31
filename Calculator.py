import math 
def app():
    print("Amalgar mored nazar ra vared konid")
    print("+,-,*,/,sin,cos,sqr,tan,**,")
    print("bad az amalgar adad ra vared konid")
    inp = input()
    if(inp == "+"):
        print((float(input())+float(input())))
        app()
        ###############################
    elif(inp == "-"):
        print((float(input())-float(input())))
        app()
        ###############################
    elif(inp == "*"):
        print((float(input())*float(input())))
        app()
        #############################
    elif(inp == "/"):
        print((float(input())/float(input())))
        app()
        ###################################
    elif(inp == "**"):
        print(math.pow((float(input())),float(input())))
        app()
        ##################
    elif(inp == "tan"):
        print(math.tan(float(input())))
        app()
        ##########################
    elif(inp == "sqr"):
        print(math.sqrt(float(input())))
        app()
        ############################
    elif(inp == "sin"):
        print(math.sin(float(input())))
        app()
        ############################
    elif(inp == "cos"):
        print(math.cos(float(input())))
        app()
    else:
        app()
app()
#پروژه پایانی پایتون ماشین حساب پیشرفته
#محمد حسین رنجبر حسینی