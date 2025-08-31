from windows.gui import MainWindow
from database.create_db import create_db

if __name__ == "__main__":
    create_db()
    app = MainWindow()
    app.show_main_frame()
    app.mainloop()