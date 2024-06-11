from prettytable import PrettyTable



table = PrettyTable()

table.add_column("big",column = ["input",'',''])
table.border = True
table.add_column("small", column = ['x','u',345])

print(table)