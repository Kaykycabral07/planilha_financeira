from windows.gui import MainWindow
from database.functions import create_db

if __name__ == "__main__":
    create_db()
    app = MainWindow()
    app.show_main_frame()
    app.mainloop()