from flask import request, jsonify
from database import get_connection
from datetime import date

def register_routes(app):

    # ==========================
    # CADASTRAR USUÁRIO
    # ==========================
    @app.route("/usuarios", methods=["POST"])
    def cadastrar_usuario():
        """
        Cadastrar usuário
        ---
        responses:
            201:
                description: Usuário cadastrado
        """
        
        dados = request.get_json()

        nome = dados.get("nome")
        email = dados.get("email")

        if not nome or not email:
            return jsonify({
                "erro": "Nome e email são obrigatórios."
            }), 400

        conn = get_connection()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO usuarios(nome, email)
                VALUES (?, ?)
            """, (nome, email))

            conn.commit()

            return jsonify({
                "mensagem": "Usuário cadastrado com sucesso!"
            }), 201

        except Exception as e:

            return jsonify({
                "erro": str(e)
            }), 400

        finally:
            conn.close()

    # ==========================
    # LOGIN
    # ==========================
    @app.route("/login", methods=["POST"])
    def login():
        """
        Login do usuário
        ---
        responses:
            200:
                description: Login realizado
        """

        dados = request.get_json()

        email = dados.get("email")

        if not email:
            return jsonify({
                "erro": "Informe um email."
            }), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE email = ?",
            (email,)
        )

        usuario = cursor.fetchone()

        conn.close()

        if usuario:

            return jsonify({
                "id": usuario["id"],
                "nome": usuario["nome"],
                "email": usuario["email"]
            })

        return jsonify({
            "erro": "Usuário não encontrado."
        }), 404
    
    # ==========================
    # CRIAR HÁBITO
    # ==========================
    @app.route("/habitos", methods=["POST"])
    def criar_habito():
        """
        Criar hábito
        ---
        responses:
            201:
                description: Hábito criado
        """

        dados = request.get_json()

        usuario_id = dados.get("usuario_id")
        nome = dados.get("nome")
        meta = dados.get("meta")

        if not usuario_id or not nome or not meta:
            return jsonify({
                "erro": "Todos os campos são obrigatórios."
            }), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO habitos(usuario_id, nome, meta)
            VALUES (?, ?, ?)
        """, (usuario_id, nome, meta))

        conn.commit()

        conn.close()

        return jsonify({
            "mensagem": "Hábito criado com sucesso!"
        }), 201

    # ==========================
    # LISTAR HÁBITOS
    # ==========================
    @app.route("/habitos", methods=["GET"])
    def listar_habitos():
        """
        Listar hábitos
        ---
        responses:
            200:
                description: Lista de hábitos
        """

        usuario_id = request.args.get("usuario_id")

        if not usuario_id:
            return jsonify({
                "erro": "usuario_id é obrigatório."
            }), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM habitos
            WHERE usuario_id = ?
        """, (usuario_id,))

        habitos = cursor.fetchall()

        conn.close()

        lista = []

        for habito in habitos:
            lista.append({
                "id": habito["id"],
                "usuario_id": habito["usuario_id"],
                "nome": habito["nome"],
                "meta": habito["meta"],
                "dias_seguidos": habito["dias_seguidos"],
                "ultima_data": habito["ultima_data"]
            })

        return jsonify(lista)

    # ==========================
    # EDITAR HÁBITO
    # ==========================
    @app.route("/habitos/<int:id>", methods=["PUT"])
    def editar_habito(id):
        """
        Editar hábito
        ---
        responses:
            200:
                description: Hábito atualizado
        """

        dados = request.get_json()

        nome = dados.get("nome")
        meta = dados.get("meta")

        if not nome or not meta:
            return jsonify({
                "erro": "Nome e meta são obrigatórios."
            }), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE habitos
            SET nome = ?, meta = ?
            WHERE id = ?
        """, (nome, meta, id))

        conn.commit()

        conn.close()

        return jsonify({
            "mensagem": "Hábito atualizado com sucesso!"
        })
    
    # ==========================
    # EXCLUIR HÁBITO
    # ==========================
    @app.route("/habitos/<int:id>", methods=["DELETE"])
    def excluir_habito(id):
        """
        Excluir hábito
        ---
        responses:
            200:
                description: Hábito excluído
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM habitos WHERE id = ?",
            (id,)
        )

        conn.commit()

        conn.close()

        return jsonify({
            "mensagem": "Hábito excluído com sucesso!"
        })

    # ==========================
    # MARCAR HÁBITO
    # ==========================
    @app.route("/habitos/<int:id>/marcar", methods=["PATCH"])
    def marcar_habito(id):
        """
        Marcar hábito
        ---
        responses:
            200:
                description: Hábito marcado
        """

        hoje = date.today().isoformat()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE habitos
            SET dias_seguidos = dias_seguidos + 1,
                ultima_data = ?
            WHERE id = ?
        """, (hoje, id))

        conn.commit()

        conn.close()

        return jsonify({
            "mensagem": "Hábito marcado com sucesso!"
        })


