import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from tkinter.constants import BOTH, UNDERLINE
app=tk.Tk()
app.title("CodePad")
app.geometry("450x300+450+200")
# ---------------text_area----------------
default_bg="#1f1f1f"
default_fg="#ffffff"
app.config(bg=default_bg)
text_area=tk.Text(app,bg=default_bg,fg=default_fg,font=("Courier",14))
text_area.pack(fill="both",expand=1)
text_area.focus_force()
 # -------------main_menu------------
main_menu=tk.Menu(app)
app.config(menu=main_menu)
# ------------menu_function----------
#------------open_file---------------
url=''
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(('Text File','*.txt'),("All Files","*.*")))
    try:
        with open(url,"r") as f:
            text_area.delete(1.0,tk.END)
            text_area.insert(1.0,f.read())
        app.title(os.path.basename(url))
    except FileNotFoundError:
        pass
    except:
        messagebox.showerror("Oops!!","Something went wrong")
#------------new_file---------------
def new_file(event=None):
    global url
    if (len(text_area.get(1.0,tk.END))>1):
        save=messagebox.askokcancel("Confirm","Do you want to save this file?")
        if save:
            try:
                if url:
                    with open(url,"w") as fw:
                        content=str(text_area.get(1.0,tk.END))
                        fw.write(content)
                else:
                    url=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save File",defaultextension="*.txt")
                    with open(url,"w") as nfw:
                        content_to_save=str(text_area.get(1.0,tk.END))
                        nfw.write(content_to_save)
            except FileNotFoundError:
                 messagebox.showerror("File not saved","File has not been saved")
            except:
                messagebox.showerror("Oops!!","Something went wrong")
        else:
            messagebox.showinfo("File not saved","File has not been saved")
        url=''
        app.title("CodePad")
        text_area.delete(1.0,tk.END)      
#------------save_file---------------
def save_file(event=None):
    global url
    try:
        if url:
            with open(url,"w") as fw:
                content=str(text_area.get(1.0,tk.END))
                fw.write(content)
            app.title(os.path.basename(url))
        else:
            url=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save File",defaultextension="*.txt")
            with open(url,"w") as nfw:
                content2=str(text_area.get(1.0,tk.END))
                nfw.write(content2)
            app.title(os.path.basename(url))
    except FileNotFoundError:
        messagebox.showerror("File not saved","File has not been saved")
    except:
        messagebox.showerror("Oops!!","Something went wrong")
#------------save_as_file---------------
def save_as_file(event=None):
    url=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save File",defaultextension="*.txt")
    try:
        with open(url,"w") as nfw:
            content3=str(text_area.get(1.0,tk.END))
            nfw.write(content3)
        app.title(os.path.basename(url))
    except  FileNotFoundError:  
        messagebox.showerror("File not saved",'File has not been saved')
#------------close_file---------------
def close_file(event=None):
    url=''
    app.title("CodePad")
    text_area.delete(1.0,tk.END)
#------------run_file-----------------
def run_file(event=None):
    if (os.path.splitext(os.path.basename(url))[1]==".py"):
        os.system(f"python {url}")
    elif(os.path.splitext(os.path.basename(url))[1]==".html" or os.path.splitext(os.path.basename(url))[1]==".htm"):
        os.startfile(url)
    else:
        messagebox.showerror("Oops!","File should be a HTML or a Python file")
 
# -----file_menu------
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="Open",command=open_file,accelerator="Ctrl+O")
file_menu.add_command(label="New File",command=new_file,accelerator="Ctrl+N")
file_menu.add_command(label="Save",command=save_file,accelerator="Ctrl+S")
file_menu.add_command(label="Save As",command=save_as_file,accelerator="Ctrl+Shift+S")
file_menu.add_command(label="Close File",command=close_file,accelerator="Ctrl+W")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=lambda:app.quit(),accelerator="Alt+F4")
# ------------view_menu------------
view_menu=tk.Menu(main_menu,tearoff=0)
#-------themes_menu-------------
theme_menu=tk.Menu(view_menu,tearoff=0)
theme_menu.add_command(label="Default",command=lambda:text_area.config(bg="#1f1f1f",fg="#ffffff"))
theme_menu.add_command(label="Light Blue",command=lambda:text_area.config(bg="#5652ff",fg="#000000"))
theme_menu.add_command(label="Light Green",command=lambda:text_area.config(bg="#56ff52",fg="#000000"))
theme_menu.add_command(label="Dark",command=lambda:text_area.config(bg="#0f0f0f",fg="#f0f0f0"))
theme_menu.add_command(label="Grey",command=lambda:text_area.config(bg="#0f0f0f",fg="#f0f0f0"))
#--------------run_menu-----------------
run_menu=tk.Menu(main_menu,tearoff=0)
run_menu.add_command(label="Run",command=run_file)
#------------menu_cascading------------
main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="View",menu=view_menu)
view_menu.add_cascade(label="Themes",menu=theme_menu)
main_menu.add_cascade(label="Run",menu=run_menu)
# -----------------shortcut_bindings------------------
app.bind("<Control-o>",open_file)
app.bind("<Control-n>",new_file)
app.bind("<Control-s>",save_file)
app.bind("<Control-Shift-S>",save_as_file)
app.bind("<Control-w>",close_file)
app.bind("<Control-r>",run_file)
app.mainloop()
