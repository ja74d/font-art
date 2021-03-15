import os
def font():
    string = input(str('enter your string:'))
    from pyfiglet import Figlet
    c_text = Figlet(font=input(str('''enter font name :
for exampel:
3-d | avatar | banner | basic | bell | big | block | bubble | ...
to see all fonts folow this link:http://www.figlet.org/fontdb.cgi
enter font name:''')))
    os.system("clear")
    print(c_text.renderText(string))
font()
