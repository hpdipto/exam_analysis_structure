
from tkinter import *
import data
from tkinter import messagebox
import interface


def get_roll(en, roll=roll):
    r = int(roll_entry.get())
    roll.set(r)

    roll_list = data.roll_list

    if r in roll_list:
        n, sc, wm, vm, vr = data.get_info(r)

        if str(vm) == "nan":
        	vm = ""
        if str(vr) == "nan":
        	vr = ""


        name.config(text=n)
        subject_code.config(text=sc)
        written_marks.config(text=wm)
        viva_entry.config(textvariable=viva_marks.set(vm))

        remark_text.delete("1.0", "end")
        remark_text.insert(INSERT, vr)

    else:
        name.config(text="N/A")
        subject_code.config(text="N/A")
        written_marks.config(text="N/A")
        viva_entry.config(textvariable=viva_marks.set(""))
        remark_text.delete("1.0", "end")

        messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")


def get_roll_button(roll=roll):
    r = int(roll_entry.get())
    roll.set(r)

    roll_list = data.roll_list

    if r in roll_list:
        n, sc, wm, vm, vr = data.get_info(r)

        if str(vm) == "nan":
        	vm = ""
        if str(vr) == "nan":
        	vr = ""


        name.config(text=n)
        subject_code.config(text=sc)
        written_marks.config(text=wm)
        viva_entry.config(textvariable=viva_marks.set(vm))

        remark_text.delete("1.0", "end")
        remark_text.insert(INSERT, vr)
    else:
        name.config(text="N/A")
        subject_code.config(text="N/A")
        written_marks.config(text="N/A")
        viva_entry.config(textvariable=viva_marks.set(""))
        remark_text.delete("1.0", "end")

        messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")



def update_entry(en):

    r = int(roll_entry.get())

    roll_list = data.roll_list

    # viva_remarks = remark_text.get("1.0", "end-1c")

    if r in roll_list:
        vm = viva_entry.get()
        vr = remark_text.get("1.0", "end-1c")

        data.update_info(r, vm, vr)
    else:
        name.config(text="N/A")
        subject_code.config(text="N/A")
        written_marks.config(text="N/A")
        viva_entry.config(textvariable=viva_marks.set(""))
        remark_text.delete("1.0", "end")
        

        messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")



def update_button(roll):

    r = int(roll_entry.get())

    roll_list = data.roll_list

    if r in roll_list:
        vm = viva_entry.get()
        vr = remark_text.get("1.0", "end-1c")

        data.update_info(r, vm, vr)
    else:
        name.config(text="N/A")
        subject_code.config(text="N/A")
        written_marks.config(text="N/A")
        viva_entry.config(textvariable=viva_marks.set(""))
        remark_text.delete("1.0", "end")

        messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")