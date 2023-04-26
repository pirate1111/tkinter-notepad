# 메모장 만들기

from tkinter import *
from tkinter.filedialog import *

window = Tk()                                       # 창 만듦
window.title("Notepad")                             # 창 이름
window.geometry("400x400")
window.resizable(False, False)

menu = Menu(window)                                 # 메뉴 위젯 만드는 클래스
menu_1 = Menu(menu, tearoff=0)       
menu_1.add_command(label="새파일")                  # 메뉴 항목 생성
menu_1.add_command(label="저장")
menu_1.add_separator()                              # 메뉴 구분선 생성
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)         # 메뉴 펼치는 라벨 추가

menu_2 = Menu(menu, tearoff=0)                      # 메뉴2 생성
menu_2.add_command(label="만든이")
menu.add_cascade(label="만든이", menu=menu_2)       # 하위 메뉴 추가

text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky = N + E + S + W)

window.config(menu=menu)
window.mainloop()
