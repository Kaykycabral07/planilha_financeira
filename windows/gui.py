from customtkinter import * #type:ignore
from tkinter import messagebox
from utils import verify_email, verify_password, encrypt_password, check_password
from database.create_db import register_user_in_db, session, User

class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplicação para banco de dados")
        self.geometry("550x550")

        self.initial_frame = CTkFrame(self)
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
        
        CTkButton(self.main_frame,text="registrar",
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
        self.email_entry = CTkEntry(self.login_frame)
        self.email_entry.grid(pady=5, padx=10, row=1, column=1)

        CTkLabel(self.login_frame, text="Insira sua senha:").grid(row=2,column=0,pady=5, padx=10, sticky="e")
        self.password_entry = CTkEntry(self.login_frame)
        self.password_entry.grid(pady=5, padx=10, row=2, column=1 )

        CTkButton(self.login_frame, text="Fazer login", command=self.login_user).grid(row=3,columnspan=2, pady=10, padx=5 )

        CTkButton(self.login_frame, text="Voltar", command= self.show_initial_frame).grid(row=4,columnspan=2, pady=5, padx=5 )

        # Elementos da tela de registro
        CTkLabel(self.register_frame,text="TELA DE REGISTRO"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20,
            )
        
        CTkLabel(self.register_frame, text="Insira seu nome:").grid(row=1,column=0,pady=5, padx=10, sticky="e")
        self.name_entry = CTkEntry(self.register_frame)
        self.name_entry.grid(pady=5, padx=10, row=1, column=1)        
        
        CTkLabel(self.register_frame, text="Insira seu email:").grid(row=2,column=0,pady=5, padx=10, sticky="e")
        self.email_register_entry = CTkEntry(self.register_frame)
        self.email_register_entry.grid(pady=5, padx=10, row=2, column=1)
        
        CTkLabel(self.register_frame, text="Insira sua senha:").grid(row=3,column=0,pady=5, padx=10, sticky="e")
        self.password_register_entry = CTkEntry(self.register_frame)
        self.password_register_entry.grid(pady=5, padx=10, row=3, column=1 )
        
        CTkLabel(self.register_frame, text="Confirme sua senha:").grid(row=4,column=0,pady=5, padx=10, sticky="e")
        self.confirm_password_entry = CTkEntry(self.register_frame)
        self.confirm_password_entry.grid(pady=5, padx=10, row=4, column=1 )
        
        CTkButton(self.register_frame, text="Registrar", command= self.register_user).grid(row=5,columnspan=2, pady=10, padx=5 )

        CTkButton(self.register_frame, text="Voltar", command= self.show_initial_frame).grid(row=6,columnspan=2, pady=5, padx=5 )
        
        
    def register_user(self):
        name = self.name_entry.get()
        email = self.email_register_entry.get()
        password = self.password_register_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if not all([name, email, password, confirm_password]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!.")
            return
        
        elif verify_email(email) is False:
            messagebox.showerror("Erro", "Insira um email valido")
            return
        
        elif verify_password(password, confirm_password) is False:
            messagebox.showerror("Erro", "A senha tem que ser igual nos dois campos!.")
            return
        
        hashed = encrypt_password(password)
        register_user_in_db(name,email,password= hashed.decode("utf-8"))
        
        self.name_entry.delete("0", "end")
        self.email_register_entry.delete("0","end")
        self.password_register_entry.delete("0","end")
        self.confirm_password_entry.delete("0", "end")
        
        self.show_initial_frame() 
        
    def login_user(self):
        email = self.email_entry.get()
        typed_password = self.password_entry.get()
        
        if not email and typed_password:
            messagebox.showerror("Erro", "Primeiro insira os dados!.")
            return
        user = session.query(User).filter_by(email=email).first()
        if not user:
            messagebox.showerror("Erro", "Não existe usuario com esse email!.")
            return        
        
        if check_password(stored_password= user.password, typed_password=typed_password):
            self.email_entry.delete("0","end")
            self.password_entry.delete("0", "end")
            self.show_main_frame()
        
    def show_initial_frame(self):
        self.initial_frame.pack()
        self.main_frame.pack_forget()
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()

    def show_login_frame(self):
        self.login_frame.pack()
        self.main_frame.pack_forget()
        self.register_frame.pack_forget()
        self.initial_frame.pack_forget()
    
    def show_register_frame(self):
        self.register_frame.pack()
        self.main_frame.pack_forget()
        self.login_frame.pack_forget()
        self.initial_frame.pack_forget()
    
    def show_main_frame(self):
        self.main_frame.pack()
        self.login_frame.pack_forget()
        self.initial_frame.pack_forget()
        self.register_frame.pack_forget()