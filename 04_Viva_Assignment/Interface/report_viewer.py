
import tkinter as tk
import pandas as pd
import data

from tkinter import ttk
import tkinter.ttk as ttk


file_name = "12-11-2019_Group 3.csv"

board = 1
group = 3
date = "12-11-2019"

def init(bd, gp, dt):
	global board
	board = bd
	global group
	group = gp
	global date
	date = dt

	global file_name
	file_name = "Data/"+str(date)+"_Group "+str(group)+".csv"



def generate_report():
	df = data.report(file_name)

	column_names = ["Serial", "Name", "Roll", "Subject Code", "Subject Name", "Marks Obtained", "Viva Marks", "Total Marks", "Remarks"]
	df_column_names = ["Serial", "Applicants_Name", "Roll", "Subject_Code", "subject_name", "Mark_Obtained", "Viva_Marks", "Total_Marks", "Viva_Remarks"]

	rows = len(df)
	columns = len(column_names)



	def set_abset_status(tple):
		lst = list(tple)

		if (str(tple[4]) == "0.0" or str(tple[4]) == "nan") and (str(tple[5]) == "0.0" or str(tple[5]) == "nan"):
			lst[4] = "Absent"
			lst[5] = "Absent"
			lst[6] = "Absent"
			lst[7] = "Absent"

		for i in range(len(tple)):
			if str(lst[i]) == "nan":
				lst[i] = ""

		return tuple(lst)


	def is_absent(tple):
		if str(tple[5]) == "Absent":
			return True
		else:
			return False






	master = tk.Tk()

	master.option_add("*font", 15)
	master.title(file_name[5:-4])
	master.geometry("700x500")


	style = ttk.Style(master)
	style.configure("Treeview.Heading", font=(None, 12))

	info_frame = tk.Frame(master)
	info_frame.pack(side=tk.TOP)


	bd = tk.Label(info_frame, text="Board").grid(row=0, column=0, sticky=tk.W)
	bd = tk.Label(info_frame, text=str(board)).grid(row=0, column=1, sticky=tk.E)

	gp = tk.Label(info_frame, text="Group").grid(row=1, column=0, sticky=tk.W)
	gp = tk.Label(info_frame, text=str(group)).grid(row=1, column=1, sticky=tk.E)

	dt = tk.Label(info_frame, text="Date").grid(row=2, column=0, sticky=tk.W)
	dt = tk.Label(info_frame, text="   "+str(date)).grid(row=2, column=1, sticky=tk.E)



	table_margin = tk.Frame(master, height=500, width=700)
	table_margin.pack(side=tk.TOP)

	scrollbarx = tk.Scrollbar(table_margin, orient=tk.HORIZONTAL)
	scrollbary = tk.Scrollbar(table_margin, orient=tk.VERTICAL)

	table = tk.ttk.Treeview(table_margin, height=500, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

	scrollbary.config(command=table.yview)
	scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
	scrollbarx.config(command=table.xview)
	scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)


	table["columns"] = tuple(column_names)

	for i in range(len(column_names)):
		table.heading(column_names[i], text=column_names[i], anchor=tk.W)



	# customize width of various columns (hard code)
	table.column('#0', stretch=tk.NO, minwidth=0, width=0)
	table.column('#1', stretch=tk.NO, minwidth=0, width=70)
	table.column('#2', stretch=tk.NO, minwidth=0, width=300)
	table.column('#3', stretch=tk.NO, minwidth=0, width=100)
	table.column('#4', stretch=tk.NO, minwidth=0, width=120)
	table.column('#5', stretch=tk.NO, minwidth=0, width=280)
	table.column('#6', stretch=tk.NO, minwidth=0, width=150)
	table.column('#7', stretch=tk.NO, minwidth=0, width=110)
	table.column('#8', stretch=tk.NO, minwidth=0, width=110)
	table.column('#9', stretch=tk.NO, minwidth=0, width=500)



	data_tuple = [tuple(df.iloc[i]) for i in range(rows)]



	count_absent = 0
	for i in range(len(data_tuple)):
		tple = (i+1,) + set_abset_status(data_tuple[i])
		absent = is_absent(tple)
		if absent:
			table.insert("", i, i, values=tple, tags=('absent_tag'))
			count_absent += 1
		else:
			table.insert("", i, i, values=tple, tags=('present_tag'))

	table.tag_configure('absent_tag', font=(None, 12), background='#ED4D21')
	table.tag_configure('present_tag', font=(None, 12),  background='#FAFAFA')


	label = tk.Label(info_frame, text="   Present")
	label.grid(row=0, column=3, sticky=tk.W)
	label = tk.Label(info_frame, text=str(rows-count_absent))
	label.grid(row=0, column=4, sticky=tk.E)

	label = tk.Label(info_frame, text="   Absent")
	label.grid(row=1, column=3, sticky=tk.W)
	label = tk.Label(info_frame, text=str(count_absent))
	label.grid(row=1, column=4, sticky=tk.E)

	label = tk.Label(info_frame, text="   Total")
	label.grid(row=2, column=3, sticky=tk.W)
	label = tk.Label(info_frame, text=str(rows))
	label.grid(row=2, column=4, sticky=tk.E)


	table.pack(side=tk.TOP)


	master.mainloop()


# generate_report()