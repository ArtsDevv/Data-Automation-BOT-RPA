# 🤖 Automação de Cadastro de Produtos (Bot RPA)

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Tech](https://img.shields.io/badge/Tech-Python%20%7C%20PyAutoGUI%20%7C%20Pandas-blue)

## 📖 Sobre o Projeto

Este projeto foi desenvolvido para resolver um problema comum e custoso no ambiente corporativo: a entrada manual de dados (Data Entry). Utilizando Python, criei um script que atua como um bot de RPA (Robotic Process Automation), capaz de ler uma base de dados de produtos em um arquivo `.csv` e realizar o cadastro automático e sequencial desses itens no sistema da empresa.

O foco principal desta aplicação é **economizar horas de trabalho** manuais, eliminando erros de digitação e aumentando a produtividade da equipe através da **automação de tarefas** repetitivas.

## 🚀 Funcionalidades

* **Acesso Automatizado:** Abertura do navegador, navegação até a URL do sistema e preenchimento automático das credenciais de login.
* **Leitura de Dados em Massa:** Processamento eficiente de uma base de produtos utilizando a biblioteca `pandas` para extração dos dados do arquivo `.csv`.
* **Cadastro em Lote (Loop de Preenchimento):** Iteração sobre cada linha da tabela de produtos, preenchendo campo a campo do formulário web e enviando o registro para o sistema.

## 🧠 Conceitos e Habilidades Aplicadas

Este projeto coloca em prática os fundamentos fundamentais da trilha "Python Power Up":
* Automação de Tarefas
* Criação de Bots
* Economizar horas de trabalho
* RPA e Web-Scraping

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python 3**
* **PyAutoGUI:** Utilizado para o mapeamento de tela, automação dos cliques do mouse e inserção de comandos via teclado.
* **Pandas:** Utilizado para a leitura, estruturação e manipulação do arquivo `.csv`.
* **Time:** Implementado para controle de pausas (`sleep`), garantindo a sincronia entre a execução do código e o tempo de carregamento das páginas web.
