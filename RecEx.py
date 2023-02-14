from openpyxl import Workbook
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import *

def path_window_xlsx():
	root = Tk()
	root.withdraw()
	PathSave = askdirectory()
	root.destroy()
	return PathSave

def write_book(Dimensions, Path):
	wb = Workbook()
	ws = wb.active
	ws.append(['№', 'Name size', 'Nominal size', 'Max size', 'Min size'])
	for Dimension in Dimensions:
		ws.append(Dimension)
	wb.save(Path + "/BookDimensions.xlsx")



