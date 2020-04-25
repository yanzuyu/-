import os,sys
from tkinter import*
from tkinter.ttk import*
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
# from tkinter import message
from tkinter.scrolledtext import ScrolledText
import webbrowser;from tkinter import*;from tkinter import messagebox;from tkinter.ttk import*

def new():
    
    text.delete("1.0",END)
    root.title("未命名")
def saveFile():
    global filename
    filename="page.html"
    z="<p>"+text.get("1.0",END).replace("\n","\n<br/>")+"</p>"
    with open(filename,"w",encoding="utf-8") as f:
        k="""<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>{{title}}</title>
		<style>
			:root{background-color: azure;
				;
			}
		</style>
		<style>
			footer{background-color: #323232;
			color: #c8d4d4;}
			h1{text-shadow:0px 0px 20px #6d7373;
			text-align: center;
			font-family: "黑体";
			color: black;
			font-size: 50px;
			}
			
			#wen{width:800px;background-color: #c2f4ca}
			
			p{font-family: "幼圆";font-size: 20px;text-align: left;}
			
			a{text-decoration:none;color: white;font-size: 15px}
			
			.tuchu{font-family: "楷体";font-size: 23px}
			
			.xie{font-style: italic}
			.red{color: red}
			.blue{color: cyan}
			.text{text-align: left;}
		</style>
	</head>
	<body>


		<div align="center">
		<div id="wen" >
			<h1>{{title}}</h1>
			{{wen}}
		</div>
		</div>
		<br\>&nbsp; <br\> &nbsp;
	</body>
	
        <footer>
		<div align="center">
			<br/>子昱|2020 All Rights Reserved.
			<br/><a href="https://www.wenjuan.com/s/3Unqem9/">放话</a>
			&nbsp;<a href="../jiao.html">python教程</a><br/><a href="../index.html">个人主页</a><br/>QQ:2292068915  
			<br/> 微信：eazy252625  
			<br/> 邮箱：yanziyu252625@qq.com
			<br/>  &nbsp;
		</div>
	
		
		
	</footer>
</html>

        """
        k=k.replace("{{title}}",Enter.get())
        nice="<p>"+text.get("1.0",END).replace("\n","&nbsp;<br/>\n")+"</p>"
        nice=nice.replace("chu{",'<p class="tuchu">').replace("end}","</p>")
        
        k=k.replace("{{wen}}",nice)
        f.write(k)
        get=text.get("1.0",END)
        
        root.title(filename)
def find(a,b):
    text.tag_remove(b,"1.0",END)
    start="1.0"
    key=a
    if len(k)==0:
        return
    pos=text.search(key,start,END)
    while pos!="":
        text.tag_add(b,pos,"%s+%dc"%(pos,len(word)))
        start="%s+%dc"%(pos,len(word))
        pos=text.search(key,start,END)
def finds(z,tag):
    for x in z:
        find(z,tag)

def keyword():
    finds(key,"key")
filename="未命名"

root=Tk()
root.title(filename)
root.geometry("680x770")
Enter=Entry(root)
Enter.insert(END,"标题")

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=False)

menubar.add_cascade(label="文件",menu=filemenu)
filemenu.add_command(label="新文件",command=new)
filemenu.add_command(label="保存文件",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="退出",command=root.destroy)
root.config(menu=menubar)
Enter.pack(fill=X)
text=ScrolledText(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.tag_configure("key",foreground="blue")

root.mainloop()








