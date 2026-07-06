# 💜 RoutineX-Back-end

## 📖 Descrição

A API do RoutineX foi desenvolvida utilizando Python e Flask para fornecer os serviços responsáveis pelo gerenciamento de hábitos.

Ela é responsável pelo cadastro de usuários, autenticação, gerenciamento dos hábitos e persistência dos dados utilizando SQLite.

Além disso, a API possui documentação utilizando Swagger (OpenAPI).

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Flask
- Flask-CORS
- Flasgger (Swagger)
- SQLite

---

## 📂 Estrutura do Projeto

```
RoutineX-Back-end/
│
├── app.py
├── database.db
├── database.py
├── requirements.txt
├── routes.py
├── swagger.py
└── .gitignore
```

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/rRafaelGomes/RoutineX-Back-end.git
```

### 2. Acesse a pasta

```bash
cd RoutineX-Back-end
```

### 3. Crie um ambiente virtual

Windows

```bash
python -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a API

```bash
python app.py
```

A API será iniciada em:

```
http://127.0.0.1:5000
```

---

## 📖 Documentação da API

Após iniciar o servidor, a documentação pode ser acessada em:

```
http://127.0.0.1:5000/apidocs
```

---

## 📌 Rotas Disponíveis

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| POST | `/usuarios` | Cadastro de usuário |
| POST | `/login` | Login do usuário |
| GET | `/habitos` | Listar hábitos |
| POST | `/habitos` | Criar hábito |
| PUT | `/habitos/{id}` | Editar hábito |
| DELETE | `/habitos/{id}` | Excluir hábito |
| PATCH | `/habitos/{id}/marcar` | Marcar hábito como realizado |

---

## 🗄️ Banco de Dados

O projeto utiliza o banco de dados **SQLite**, contendo tabelas para usuários e hábitos.

---

## ✨ Funcionalidades

- Cadastro de usuários
- Login
- Cadastro de hábitos
- Listagem de hábitos
- Atualização de hábitos
- Exclusão de hábitos
- Controle de dias consecutivos
- Documentação da API com Swagger

---

## 👨‍💻 Autor

Desenvolvido por Rafael Gomes de Almeida como projeto da disciplina de Desenvolvimento Full Stack da Pos Graduação de Engenharia de Software.
