from Tkinter import *
from controle import Controle

class Crud_Funcionario:

    def __init__(self, master):
        self.frame= Frame(master, height=600, width=500)
        self.frame.pack()
        self.labelname= Label(self.frame, text='Nome')
        self.labelname.place(x=0,y=30)
        self.name_str= StringVar()
        self.entryname= Entry(self.frame, textvariable= self.name_str, width=22)
        self.entryname.place(x=50,y=30)

        self.labelcpf= Label(self.frame, text='Cpf')
        self.labelcpf.place(x=0,y=60)
        self.cpf_str= StringVar()
        self.entrycpf= Entry(self.frame, textvariable= self.cpf_str, width=22)
        self.entrycpf.place(x=50,y=60)

        self.labelendereco= Label(self.frame, text='Endereco')
        self.labelendereco.place(x=0,y=90)
        self.endereco_str= StringVar()
        self.entryendereco= Entry(self.frame, textvariable= self.endereco_str, width=22)
        self.entryendereco.place(x=50,y=90)

        self.labeltelefone= Label(self.frame, text='Telefone')
        self.labeltelefone.place(x=0,y=120)
        self.telefone_str= StringVar()
        self.entrytelefone= Entry(self.frame, textvariable= self.telefone_str, width=22)
        self.entrytelefone.place(x=50,y=120)

        self.labeldt_nasc= Label(self.frame, text='dt_nasc')
        self.labeldt_nasc.place(x=0,y=150)
        self.dt_nasc_str= StringVar()
        self.entrydt_nasc= Entry(self.frame, textvariable= self.dt_nasc_str, width=22)
        self.entrydt_nasc.place(x=50,y=150)

        self.labelsalario= Label(self.frame, text='salario')
        self.labelsalario.place(x=0,y=180)
        self.salario_str= StringVar()
        self.entrysalario= Entry(self.frame, textvariable= self.salario_str, width=22)
        self.entrysalario.place(x=50,y=180)

        self.labelcargo= Label(self.frame, text='cargo')
        self.labelcargo.place(x=0,y=210)
        self.cargo_str= StringVar()
        self.entrycargo= Entry(self.frame, textvariable= self.cargo_str, width=22)
        self.entrycargo.place(x=50,y=210)

        self.labelemail= Label(self.frame, text='e-mail')
        self.labelemail.place(x=0,y=250)
        self.email_str= StringVar()
        self.entryemail= Entry(self.frame, textvariable= self.email_str, width=22)
        self.entryemail.place(x=50,y=250)
        
        self.button1 = Button(self.frame, text='Salvar', height=1, width=25,command=self.salvar)
        self.button1.place(x=5,y=280)
        self.label_str= StringVar()
        self.labelanswer= Label(self.frame, textvariable= self.label_str)
        self.labelanswer.place(x=40,y=350)

    def salvar(self):
        nome = self.name_str.get();
        cpf = self.cpf_str.get();
        end = self.endereco_str.get();
        tel = self.telefone_str.get();
        dt_nasc = self.dt_nasc_str.get();
        email = self.email_str.get();
        cargo = self.cargo_str.get();
        salario = self.salario_str.get();

        controle = Controle()
        controle.cadastrar_funcionario(nome, cpf, end, tel, dt_nasc, email, cargo, salario)
        
    
root= Tk()
p = Crud_Funcionario(root)
root.mainloop()
