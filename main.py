import pyexcel as pe
sheet = pe.load("пользователи.csv")
del sheet.row[1]
sheet.save_as("пользователи.csv")
