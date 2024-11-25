from paciente import Paciente
from enfermeiro import Enfermeiro
import tkinter as tk
from tkinter import ttk, messagebox

# Listas para armazenar pacientes e enfermeiros
pacientes = []
enfermeiros = []

# Funções
def cadastrarPaciente():
    nome = entryNomePaciente.get()
    idade = entryIdadePaciente.get()
    enfermidade = entryEnfermidade.get()
    status = varStatus.get()
    enfermeiro_idx = comboEnfermeiros.current()

    if not nome or not idade.isdigit() or not enfermidade:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente!")
        return

    enfermeiro_responsavel = enfermeiros[enfermeiro_idx] if enfermeiro_idx >= 0 else None
    paciente = Paciente(nome, idade, enfermidade, status, enfermeiro_responsavel)
    pacientes.append(paciente)

    messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
    limparCamposPaciente()

def cadastrarEnfermeiro():
    nome = entryNomeEnfermeiro.get()
    idade = entryIdadeEnfermeiro.get()
    coren = entryCoren.get()
    setor = entrySetor.get()

    if not nome or not idade.isdigit() or not coren or not setor:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente!")
        return

    enfermeiro = Enfermeiro(nome, idade, coren, setor)
    enfermeiros.append(enfermeiro)

    messagebox.showinfo("Sucesso", "Enfermeiro cadastrado com sucesso!")
    atualizarComboEnfermeiros()
    limparCamposEnfermeiro()

def limparCamposPaciente():
    entryNomePaciente.delete(0, tk.END)
    entryIdadePaciente.delete(0, tk.END)
    entryEnfermidade.delete(0, tk.END)
    varStatus.set("Internado")

def limparCamposEnfermeiro():
    entryNomeEnfermeiro.delete(0, tk.END)
    entryIdadeEnfermeiro.delete(0, tk.END)
    entryCoren.delete(0, tk.END)
    entrySetor.delete(0, tk.END)

def atualizarComboEnfermeiros():
    comboEnfermeiros["values"] = [e.getNome() for e in enfermeiros]

def atualizarLista():
    treeview.delete(*treeview.get_children())
    for paciente in pacientes:
        enfermeiro = paciente.getEnfermeiroResponsavel()
        treeview.insert("", "end", values=(
            paciente.getNome(),
            paciente.getIdade(),
            paciente.getEnfermidade(),
            paciente.getStatus(),
            enfermeiro.getNome() if enfermeiro else "N/A"
        ))

# Interface Gráfica
janela = tk.Tk()
janela.title("Sistema de Gerenciamento Hospitalar")
janela.geometry("800x600")
janela.config(bg="#f4f4f9")

tabs = ttk.Notebook(janela)
tabs.pack(expand=1, fill="both", padx=10, pady=10)

# Aba Paciente
tabPaciente = ttk.Frame(tabs)
tabs.add(tabPaciente, text="Pacientes")

tk.Label(tabPaciente, text="Nome", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=0, column=0, pady=5, sticky="w")
entryNomePaciente = tk.Entry(tabPaciente, font=("Arial", 10), width=30, bd=2)
entryNomePaciente.grid(row=0, column=1, pady=5)

tk.Label(tabPaciente, text="Idade", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=1, column=0, pady=5, sticky="w")
entryIdadePaciente = tk.Entry(tabPaciente, font=("Arial", 10), width=30, bd=2)
entryIdadePaciente.grid(row=1, column=1, pady=5)

tk.Label(tabPaciente, text="Enfermidade", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=2, column=0, pady=5, sticky="w")
entryEnfermidade = tk.Entry(tabPaciente, font=("Arial", 10), width=30, bd=2)
entryEnfermidade.grid(row=2, column=1, pady=5)

tk.Label(tabPaciente, text="Status", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=3, column=0, pady=5, sticky="w")
varStatus = tk.StringVar(value="Internado")
tk.Radiobutton(tabPaciente, text="Internado", variable=varStatus, value="Internado", font=("Arial", 10)).grid(row=3, column=1, padx=5)
tk.Radiobutton(tabPaciente, text="Alta", variable=varStatus, value="Alta", font=("Arial", 10)).grid(row=3, column=2, padx=5)

tk.Label(tabPaciente, text="Enfermeiro Responsável", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=4, column=0, pady=5, sticky="w")
comboEnfermeiros = ttk.Combobox(tabPaciente, state="readonly", font=("Arial", 10), width=28)
comboEnfermeiros.grid(row=4, column=1, pady=5)

tk.Button(tabPaciente, text="Cadastrar Paciente", font=("Arial", 10, "bold"), command=cadastrarPaciente, bg="#4CAF50", fg="white", width=20).grid(row=5, column=0, columnspan=3, pady=10)

# Aba Enfermeiro
tabEnfermeiro = ttk.Frame(tabs)
tabs.add(tabEnfermeiro, text="Enfermeiros")

tk.Label(tabEnfermeiro, text="Nome", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=0, column=0, pady=5, sticky="w")
entryNomeEnfermeiro = tk.Entry(tabEnfermeiro, font=("Arial", 10), width=30, bd=2)
entryNomeEnfermeiro.grid(row=0, column=1, pady=5)

tk.Label(tabEnfermeiro, text="Idade", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=1, column=0, pady=5, sticky="w")
entryIdadeEnfermeiro = tk.Entry(tabEnfermeiro, font=("Arial", 10), width=30, bd=2)
entryIdadeEnfermeiro.grid(row=1, column=1, pady=5)

tk.Label(tabEnfermeiro, text="COREN", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=2, column=0, pady=5, sticky="w")
entryCoren = tk.Entry(tabEnfermeiro, font=("Arial", 10), width=30, bd=2)
entryCoren.grid(row=2, column=1, pady=5)

tk.Label(tabEnfermeiro, text="Setor", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=3, column=0, pady=5, sticky="w")
entrySetor = tk.Entry(tabEnfermeiro, font=("Arial", 10), width=30, bd=2)
entrySetor.grid(row=3, column=1, pady=5)

tk.Button(tabEnfermeiro, text="Cadastrar Enfermeiro", font=("Arial", 10, "bold"), command=cadastrarEnfermeiro, bg="#4CAF50", fg="white", width=20).grid(row=4, column=0, columnspan=3, pady=10)

# Aba Lista
tabLista = ttk.Frame(tabs)
tabs.add(tabLista, text="Lista Geral")

treeview = ttk.Treeview(tabLista, columns=("Nome", "Idade", "Detalhe1", "Detalhe2", "Detalhe3"), show="headings", height=10)
treeview.heading("Nome", text="Nome")
treeview.heading("Idade", text="Idade")
treeview.heading("Detalhe1", text="Enfermidade/COREN")
treeview.heading("Detalhe2", text="Status/Setor")
treeview.heading("Detalhe3", text="Responsável")
treeview.column("Nome", width=150)
treeview.column("Idade", width=80)
treeview.column("Detalhe1", width=150)
treeview.column("Detalhe2", width=150)
treeview.column("Detalhe3", width=150)
treeview.pack(fill="both", expand=1, pady=10)

tk.Button(tabLista, text="Atualizar Lista", font=("Arial", 10, "bold"), command=atualizarLista, bg="#4CAF50", fg="white").pack(pady=10)

janela.mainloop()
