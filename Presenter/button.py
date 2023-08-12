import View.userMenuConsole as view
import Presenter.command as com


def start():
    while True:
        view.menu_console()
        user_input = input()
        match user_input:
            case '1':
                com.show("all")
            case '2':
                com.show("ID")
            case '3':
                com.show("date")
            case '4':
                com.show("all")
                com.change_note()
            case '5':
                com.add_note()
            case '6':
                com.show("all")
                com.del_notes()
            case _:
                break
