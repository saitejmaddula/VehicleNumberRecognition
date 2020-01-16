
from PIL import Image
import cv2
import pytesseract
from tkinter import *
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['openlab']
collection = db['details']
top = Tk()
def sendmail(a):
    import smtplib
    global s
    fromaddr = 'trafficinvoice04@gmail.com'
    toaddrs  = s['Email']
    print("here",toaddrs)
    msg =a
    username = 'trafficinvoice04@gmail.com'
    password = 'traffic04'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    print("mail sent")
def cur(text):
    ans=""
    for i in text:
      #  print(i)
        if i>='A' and i<='Z':
            ans+=i
        elif i>='0' and i<='9':
            ans+=i
    return ans
def hello():
    sendmail(" This is to inform that You have been overspeeding you need to pay Rs.1500 as fine")
def bye():
    sendmail("This is to inform that You have going in Wrong route pay Rs.1000 as fine ")
def hi():
    sendmail("This is to inform that You have jumped the signal pay Rs.500 as fine")     

def click():
    entered_text = entry.get()
def enter():
    global text
    global variable,s
    v=variable.get()
    from PIL import Image
    if v=="1":
        img="C:/Users/Chimata/Desktop/openlab pics/18.jpg"
    elif v=="2":
        img="C:/Users/Chimata/Desktop/openlab pics/9b.png"
    elif v=="3":
        img="C:/Users/Chimata/Desktop/openlab pics/15.jpg"
    elif v=="4":
        img="C:/Users/Chimata/Desktop/openlab pics/7a.jpg"
    else :
        img="C:/Users/Chimata/Desktop/openlab pics/1.png"

    image=cv2.imread(img,0)
   # cv2.imshow("Original",image)
    blurred=cv2.blur(image,(3,3))   
  #  cv2.imshow("Blurred_image",blurred)
    img=Image.fromarray(blurred)
    
    text=pytesseract.image_to_string(img,lang='eng')
    text=cur(text)
    print(text)
    T.configure(state='normal')
    T.delete(1.0,END)
    T.insert(INSERT,text)
    T.configure(state='disabled')
    answer=collection.find({"Number Plate":text})
    s=answer.next()
    print(s['Name'])
    print(s['Email'])
s=""
variable = StringVar(top)
variable.set("Select Photo") 
label = OptionMenu(top, variable, "1", "2", "3","4","5")
w = Button ( top,text="OverSpeeding",command=hello )    
y = Button ( top,text="Singal Jump",command=hi )
z = Button ( top,text="Wrong Route",command=bye )
T = Text(top, height=1, width=30)
label.pack()
#k.pack()
k = Button ( top,text="OK",command=enter)    

T.pack()
k.pack()
w.pack()
y.pack()
z.pack()

text=""

print("here",text)
top.mainloop()


cv2.waitKey(0)
