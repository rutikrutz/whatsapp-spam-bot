from rich.console import Console
import pyautogui as pygui
import time

con = Console()
MSG = pygui.confirm("TOOL MADE BY RUTIK")

con.print("            _   _ _   ",style="bold cyan")
con.print("_ __ _   _| |_(_) | __",style="bold cyan")
con.print(" '__| | | | __| | |/ /",style="bold cyan")
con.print("| |  | |_| | |_| |   <",style="bold cyan")
con.print("|_|   \__,_|\__|_|_|\_",style="bold cyan")

con.print("")
con.print("tool made by Rutik.......!",style="bold green")
con.print("version 1.0.1 :heart:",style="bold cyan")
con.print(" ")
con.print("! enter the msg you want to send and hit enter then go to messanger and click on type text :heart: !",style="bold green")
con.print("")
input =input("msg:")


while True:
    pygui.typewrite(input)
    pygui.press("enter")
    time.sleep(0.01)