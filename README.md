# Sistema de Gerenciamento Hospitalar

## Descrição
O **Sistema de Gerenciamento Hospitalar** é uma aplicação desenvolvida em Python que tem como objetivo gerenciar as informações de pacientes e enfermeiros em um hospital. O sistema permite realizar o cadastro de pacientes e enfermeiros, além de exibir suas informações em uma interface gráfica simples. Ele proporciona uma gestão eficiente e organizada, facilitando o acompanhamento dos pacientes e a alocação de enfermeiros responsáveis.

## Funcionalidades
- **Cadastro de Pacientes**: Permite cadastrar pacientes, registrando informações como nome, idade, enfermidade, status (internado ou alta) e o enfermeiro responsável.
- **Cadastro de Enfermeiros**: Permite cadastrar enfermeiros, incluindo nome, idade, COREN e setor de atuação.
- **Listagem de Pacientes e Enfermeiros**: Exibe uma lista com todos os pacientes e enfermeiros cadastrados, com suas respectivas informações detalhadas.
- **Interface Gráfica**: A interface foi desenvolvida utilizando a biblioteca Tkinter para facilitar a interação do usuário com o sistema.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.x
- **Biblioteca Gráfica**: Tkinter (para a interface gráfica)
- **Estrutura de Dados**: Listas para armazenar informações de pacientes e enfermeiros
- **Objetos e Classes**: Programação orientada a objetos para gerenciar as entidades Paciente e Enfermeiro.

## Cronograma de Desenvolvimento
Semana 1: Estruturação inicial do projeto e criação das classes Paciente e Enfermeiro.
Semana 2: Implementação da interface gráfica com o Tkinter, incluindo as abas de cadastro e visualização.
Semana 3: Ajustes finais, como validações de entrada e organização do código.
Semana 4: Testes e documentação do sistema.

## Como Executar o Projeto

### Requisitos
- **Python 3.x** instalado no seu computador.
- Biblioteca Tkinter (geralmente já vem com o Python, mas caso contrário, instale com `pip install tk`).

### Instruções para Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/emanuelykock/Sistema-Gerenciamento-Hospitalar.git

Desafios Enfrentados
Durante o desenvolvimento, um dos principais desafios foi integrar a lógica de cadastro e a alocação de enfermeiros aos pacientes de forma dinâmica e eficiente. Além disso, o gerenciamento da interface gráfica utilizando Tkinter exigiu um controle cuidadoso da estrutura de layout para garantir uma boa experiência de usuário. A utilização do Git foi crucial para manter o controle das alterações e facilitar a colaboração.