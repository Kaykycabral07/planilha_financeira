from customtkinter import * #type:ignore

class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplicação para banco de dados")
        self.geometry("550x550")

        self.main_frame = CTkFrame(self)
        self.login_frame = CTkFrame(self)
        self.register_frame = CTkFrame(self)

        # Elementos da janela principal
        CTkLabel(self.main_frame,text="BEM VINDO À MINHA APLICAÇÂO"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10,
            padx=15,
            sticky="n")
        CTkLabel(self.main_frame,
        text="Logar na minha conta:").grid(row=1,column=0,columnspan=2, pady=5, padx=10)
        
        CTkButton(self.main_frame,text="login",
            command=self.show_login_frame
            ).grid(
                row=2,
                column=0,
                columnspan=2,
                pady=5,
                padx=10
            )

        CTkLabel(self.main_frame,
        text="Registrar:").grid(row=3,column=0,columnspan=2, pady=5, padx=10)
        
        CTkButton(self.main_frame,text="login",
            command=self.show_register_frame
            ).grid(
                row=4,
                column=0,
                columnspan=2,
                pady=5,
                padx=10
            )

        # Elementos da tela de login
        CTkLabel(self.login_frame,text="TELA DE LOGIN"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20,
            )
        
        CTkLabel(self.login_frame, text="Insira seu email:").grid(row=1,column=0,pady=5, padx=10, sticky="e")
        email_entry = CTkEntry(self.login_frame)
        email_entry.grid(pady=5, padx=10, row=1, column=1)

        CTkLabel(self.login_frame, text="Insira sua senha:").grid(row=2,column=0,pady=5, padx=10, sticky="e")
        password_entry = CTkEntry(self.login_frame)
        password_entry.grid(pady=5, padx=10, row=2, column=1 )

        CTkButton(self.login_frame, text="Fazer login", command= lambda:[print("button clicked!")]).grid(row=3,columnspan=2, pady=10, padx=5 )

        CTkButton(self.login_frame, text="Voltar", command= self.show_main_frame).grid(row=4,columnspan=2, pady=5, padx=5 )

        # Elementos da tela de registro
        CTkLabel(self.login_frame,text="TELA DE REGISTRO"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20,
            )
        
        CTkLabel(self.login_frame, text="Insira seu nome:").grid(row=1,column=0,pady=5, padx=10, sticky="e")
        name_entry = CTkEntry(self.register_frame)
        name_entry.grid(pady=5, padx=10, row=1, column=1)

    def show_main_frame(self):
        self.main_frame.pack()
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()

    def show_login_frame(self):
        self.login_frame.pack()
        self.main_frame.pack_forget()
        self.register_frame.pack_forget()

    def show_register_frame(self):
        self.register_frame.pack()
        self.main_frame.pack_forget()
        self.login_frame.pack_forget()

if __name__ == "__main__":
    app = MainWindow()
    app.show_main_frame()
    app.mainloop()