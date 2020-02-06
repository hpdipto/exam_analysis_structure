
from tkinter import *
import data
from tkinter import messagebox
import report_viewer


master = Tk()

master.option_add("*font", 15)

master.title("Viva")

master.geometry("600x600")

# login_frame = Frame(master)
# login_frame.pack(anchor=CENTER, pady=200)

# frame = Frame(master)
# frame.pack(anchor=CENTER, pady=90)


roll = StringVar()
viva_marks = StringVar()
mark_obtained = StringVar()
string_variable = StringVar()


board = IntVar()
group = IntVar()
date = StringVar()

# date_ = group_ = board_ = ""



def get_roll(en, roll=roll):
	if roll_entry.get().isnumeric() == True:
		r = int(roll_entry.get())
		roll.set(r)
	else:
		r = 0

	roll_list = data.roll_list

	if r in roll_list:
		data_list = data.get_info(r, group.get(), date.get())


		for i in range(len(data_list)-4):
			label_list[i].config(text=data_list[i])

		mo = data_list[8]
		if str(mo) == "nan":
			mo = ""
		vm = data_list[9]
		if str(vm) == "nan":
			vm = ""
		tm = data_list[10]
		if str(tm) == "nan":
			tm = "0"
		vr = data_list[11]
		if str(vr) == "nan":
			vr = ""

		label_list[-1].config(text=tm)
		mark_obtained_entry.config(textvariable=mark_obtained.set(mo))
		viva_entry.config(textvariable=viva_marks.set(vm))
		remark_text.delete("1.0", "end")
		remark_text.insert(INSERT, vr)

		mark_obtained_entry.focus()

	else:
		
		for i in range(len(label_list)):
			label_list[i].config(text="N/A")

		mark_obtained_entry.config(textvariable=string_variable.set(""))
		viva_entry.config(textvariable=viva_marks.set(""))
		remark_text.delete("1.0", "end")

		messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")
		roll_entry.focus()


def get_roll_button():
	if roll_entry.get().isnumeric() == True:
		r = int(roll_entry.get())
		roll.set(r)
	else:
		r = 0

	roll_list = data.roll_list

	if r in roll_list:
		data_list = data.get_info(r, group.get(), date.get())


		for i in range(len(data_list)-4):
			label_list[i].config(text=data_list[i])

		mo = data_list[8]
		if str(mo) == "nan":
			mo = ""
		vm = data_list[9]
		if str(vm) == "nan":
			vm = ""
		tm = data_list[10]
		if str(tm) == "nan":
			tm = "0"
		vr = data_list[11]
		if str(vr) == "nan":
			vr = ""

		label_list[-1].config(text=tm)
		mark_obtained_entry.config(textvariable=mark_obtained.set(mo))
		viva_entry.config(textvariable=viva_marks.set(vm))
		remark_text.delete("1.0", "end")
		remark_text.insert(INSERT, vr)

		mark_obtained_entry.focus()

	else:
		
		for i in range(len(label_list)):
			label_list[i].config(text="N/A")

		mark_obtained_entry.config(textvariable=string_variable.set(""))
		viva_entry.config(textvariable=viva_marks.set(""))
		remark_text.delete("1.0", "end")

		messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")
		roll_entry.focus()



def save_entry(en):
	
	if roll_entry.get().isnumeric():
		r = int(roll_entry.get())
	else:
		r = 0

	roll_list = data.roll_list

	if r in roll_list:
		mo = mark_obtained_entry.get()
		vm = viva_entry.get()
		vr = remark_text.get("1.0", "end-1c")
		bd = board.get()
		if (float(mo) >= 0.0 and float(mo) <= 12.0) and (float(vm) >= 0.0 and float(vm) <= 8.0):
			data.save_info(r, mo, vm, vr, bd)

			roll_entry.config(textvariable=roll.set(""))
			for i in range(len(label_list)):
				label_list[i].config(text="N/A")

			mark_obtained_entry.delete(0, 'end')
			viva_entry.delete(0, 'end')
			remark_text.delete("1.0", "end")
		else:
			messagebox.showinfo("Invalid Mark(s)", "Please Enter A Valid Mark!")
			if not (float(mo) >= 0.0 and float(mo) <= 12.0):
				mark_obtained_entry.delete(0, 'end')
			if not (float(vm) >= 0.0 and float(vm) <= 8.0):
				viva_entry.delete(0, 'end')
	else:
		messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")

		roll_entry.config(textvariable=roll.set(""))

		for i in range(len(label_list)):
			label_list[i].config(text="N/A")

		mark_obtained_entry.delete(0, 'end')
		viva_entry.delete(0, 'end')
		remark_text.delete("1.0", "end")




def save_button():
	
	if roll_entry.get().isnumeric():
		r = int(roll_entry.get())
	else:
		r = 0

	roll_list = data.roll_list

	if r in roll_list:
		mo = mark_obtained_entry.get()
		vm = viva_entry.get()
		vr = remark_text.get("1.0", "end-1c")
		bd = board.get()
		if str(mo) == "":
			mo = "0.0"
		if str(vm) == "":
			vm = "0.0"
		if str(vr) == "nan":
			vm = ""

		if (float(mo) >= 0.0 and float(mo) <= 12.0) and (float(vm) >= 0.0 and float(vm) <= 8.0):
			if mo == "0.0":
				mo = ""
			if vm == "0.0":
				vm = ""
			data.save_info(r, mo, vm, vr, bd)

			roll_entry.config(textvariable=roll.set(""))
			for i in range(len(label_list)):
				label_list[i].config(text="N/A")

			mark_obtained_entry.delete(0, 'end')
			viva_entry.delete(0, 'end')
			remark_text.delete("1.0", "end")

			index = roll_list.index(r)
			if index < len(roll_list)-1:
				roll.set(str(roll_list[index+1]))
				get_roll_button()
				mark_obtained_entry.focus()
			else:
				messagebox.showinfo("Viva Completed", "Viva Has Completed for All Roll!")
				roll_entry.focus()
		else:
			messagebox.showinfo("Invalid Mark(s)", "Please Enter A Valid Mark!")
			if not (float(mo) >= 0.0 and float(mo) <= 12.0):
				mark_obtained_entry.delete(0, 'end')
			if not (float(vm) >= 0.0 and float(vm) <= 8.0):
				viva_entry.delete(0, 'end')
	else:
		messagebox.showinfo("Invalid Roll", "Please Enter A Valid Roll!")

		roll_entry.config(textvariable=roll.set(""))

		for i in range(len(label_list)):
			label_list[i].config(text="N/A")

		mark_obtained_entry.delete(0, 'end')
		viva_entry.delete(0, 'end')
		remark_text.delete("1.0", "end")



def login_entry(en):

	if str(board_entry.get()).isnumeric() and str(group_entry.get()).isnumeric():
		board_ = int(board_entry.get())
		group_ = int(group_entry.get())
	else:
		board_ = group_ = 0

	date_ = str(date_entry.get())

	if (board_ >= 1 and board_ <= 9) and (group_ >= 1 and group_ <= 9) and (date_ in data.date_list):

		data.init(board_entry.get(), group_entry.get(), date_entry.get())
		report_viewer.init(board_entry.get(), group_entry.get(), date_entry.get())

		board.set(board_)
		group.set(group_)
		date.set(date_)
		roll.set(data.global_roll)

		group_label.config(text="Group: "+str(group.get()))
		board_label.config(text="Board: "+str(board.get()))
		date_label.config(text=date.get())

		get_roll_button()
		mark_obtained_entry.focus()

		login_frame.grid_forget()
		login_frame.destroy()


		frame.pack(anchor=CENTER, pady=50)

	else:
		board_entry.delete(0, 'end')
		group_entry.delete(0, 'end')
		date_entry.delete(0, 'end')

		messagebox.showinfo("Invalid Input", "Please Enter A Valid Values!")


def login_button():

	if str(board_entry.get()).isnumeric() and str(group_entry.get()).isnumeric():
		board_ = int(board_entry.get())
		group_ = int(group_entry.get())
	else:
		board_ = group_ = 0

	date_ = str(date_entry.get())

	if (board_ >= 1 and board_ <= 9) and (group_ >= 1 and group_ <= 9) and (date_ in data.date_list):

		data.init(board_entry.get(), group_entry.get(), date_entry.get())
		report_viewer.init(board_entry.get(), group_entry.get(), date_entry.get())

		board.set(board_)
		group.set(group_)
		date.set(date_)
		roll.set(data.global_roll)

		group_label.config(text="Group: "+str(group_entry.get()))
		board_label.config(text="Board: "+str(board_entry.get()))
		date_label.config(text=date_entry.get())

		get_roll_button()
		mark_obtained_entry.focus()

		login_frame.grid_forget()
		login_frame.destroy()


		frame.pack(anchor=CENTER, pady=50)

	else:
		board_entry.delete(0, 'end')
		group_entry.delete(0, 'end')
		date_entry.delete(0, 'end')

		messagebox.showinfo("Invalid Input", "Please Enter A Valid Values!")


def new_board_start():
	frame.pack_forget()
	lf, be, ge, de = login_screen()

	global login_frame
	login_frame = lf

	global board_entry
	board_entry = be

	global group_entry
	group_entry = ge

	global date_entry
	date_entry = de







# login screen

def login_screen():

	# frame.pack_forget()

	login_frame = Frame(master)
	login_frame.pack(anchor=CENTER, pady=200)

	board_label = Label(login_frame, text="Board").grid(row=0, column=0, sticky=W)
	board_entry = Entry(login_frame)
	board_entry.grid(row=0, column=1, sticky=E)

	board_entry.focus()

	group_label = Label(login_frame, text="Group").grid(row=1, column=0, sticky=W)
	group_entry = Entry(login_frame)
	group_entry.grid(row=1, column=1, sticky=E)


	date_label = Label(login_frame, text="Date (DD-MM-YYYY)").grid(row=2, column=0, sticky=W)
	date_entry = Entry(login_frame) #, textvariable=date)
	date_entry.grid(row=2, column=1, sticky=E)
	date_entry.bind('<Return>', login_entry)


	login = Button(login_frame, text="Login", command=login_button).grid(row=3, column=1, sticky=N)

	return login_frame, board_entry, group_entry, date_entry




# 201013546 201010334 201011150
# 201015987
# group 3 : 201008040, 201008259


def main_frame(board_entry, group_entry, date_entry):

	# frame = Frame(master)
	# login_frame.pack_forget()

	frame = Frame(master)
	frame.pack(anchor=CENTER, pady=90)

	row_names = ["Name", "Father's Name", "Mother's Name", "Date of Birth(DD-MM-YYYY)", "Subject Code",
				   "Subject Name", "Home District", "Invoice", "Total Marks"]

	label_list = [Label(frame, text="N/A") for i in range(len(row_names))]


	board_label = Label(frame, text="Board:"+str(board.get()))
	board_label.grid(row=0, column=0, sticky=W)

	group_label = Label(frame, text="Group: "+str(group.get()))
	group_label.grid(row=0, column=1, sticky=E)


	date_label = Label(frame, text="Date").grid(row=1, column=0, sticky=W)
	date_label = Label(frame, text=date.get())
	date_label.grid(row=1, column=1, sticky=E)


	roll_label = Label(frame, text="Roll").grid(row=2, column=0, sticky=W)
	roll_entry = Entry(frame, textvariable=roll, width=25)
	roll_entry.grid(row=2, column=1, sticky=E)
	roll_entry.bind('<Return>', get_roll)


	for r in range(len(row_names)):
		label1 = Label(frame, text=row_names[r]).grid(row=r+3, column=0, sticky=W)
		label2 = label_list[r]
		label2.grid(row=r+3, column=1, sticky=E)



	mark_obtained_label = Label(frame, text="Mark Obtained").grid(row=12, column=0, sticky=W)
	mark_obtained_entry = Entry(frame, textvariable=mark_obtained, width=15)
	mark_obtained_entry.grid(row=12, column=1, sticky=E)


	viva_label = Label(frame, text="Viva Mark").grid(row=13, column=0, sticky=W)
	viva_entry = Entry(frame, textvariable=viva_marks, width=15)
	viva_entry.grid(row=13, column=1, sticky=E)


	remark_label = Label(frame, text="Remarks").grid(row=14, column=0, sticky=NW)
	remark_text = Text(frame)
	remark_text.grid(row=14, column=1, sticky=E)
	remark_text.config(width=25, height=2)



	load = Button(frame, text="Load", command=get_roll_button).grid(row=15, column=0, sticky=W)

	save = Button(frame, text="Save", command=save_button).grid(row=15, column=1, sticky=E)

	newline = Label(frame, text="").grid(row=16)
	newline = Label(frame, text="").grid(row=17)

	report = Button(frame, text="Show Report", command=report_viewer.generate_report).grid(row=18, column=0, sticky=W)

	new_board = Button(frame, text="New Board", command=new_board_start).grid(row=18, column=1, sticky=E)


	return frame, board_label, group_label, date_label, roll_entry, label_list, mark_obtained_entry, viva_entry, remark_text




if __name__ == "__main__":

	login_frame, board_entry, group_entry, date_entry = login_screen()
	frame, board_label, group_label, date_label, roll_entry, label_list, mark_obtained_entry, viva_entry, remark_text = main_frame(board_entry, group_entry, date_entry)


	master.mainloop()