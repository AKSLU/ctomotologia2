from flask import Flask, request, render_template
from models import Client, Note
from database import Session
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/add_user", methods=["POST"])
def add_user():
    try:
        data = request.form
        session = Session()
        new_client = Client(
            name=data["name"],
            healing_price=int(data["healing_price"]),
            status=int(data["status"])
        )
        session.add(new_client)
        session.commit()
        return "Пользователь добавлен"
    except Exception as e:
        return f"Ошибка при добавлении пользователя: {e}"


@app.route("/api/add_note", methods=["POST"])
def add_note():
    try:
        data = request.form
        session = Session()
        new_note = Note(
            title=data["title"],
            description=data["description"],
            date=datetime.date.today(),
            client_id=int(data["client_id"])
        )
        session.add(new_note)
        session.commit()
        return "Заметка добавлена"
    except Exception as e:
        return f"Ошибка при добавлении заметки: {e}"


@app.route("/api/remove_user", methods=["POST"])
def remove_user():
    try:
        data = request.form
        session = Session()
        client = session.query(Client).get(int(data["id"]))
        if client:
            session.delete(client)
            session.commit()
            return "Пользователь удалён"
        return "Пользователь не найден"
    except Exception as e:
        return f"Ошибка при удалении пользователя: {e}"


@app.route("/api/remove_note", methods=["POST"])
def remove_note():
    try:
        data = request.form
        session = Session()
        note = session.query(Note).get(int(data["id"]))
        if note:
            session.delete(note)
            session.commit()
            return "Заметка удалена"
        return "Заметка не найдена"
    except Exception as e:
        return f"Ошибка при удалении заметки: {e}"


@app.route("/api/get_stats", methods=["GET"])
def get_stats():
    try:
        session = Session()
        clients = session.query(Client).all()
        result = ""
        for c in clients:
            result += f"{c.id} | {c.name} | {c.healing_price} | {c.status}\n"
        return result
    except Exception as e:
        return f"Ошибка при получении данных: {e}"


@app.route("/api/get_notes", methods=["GET"])
def get_notes():
    try:
        session = Session()
        notes = session.query(Note).all()
        result = ""
        for note in notes:
            result += f"{note.id} | {note.title} | {note.description} | {note.date} | client_id: {note.client_id}\n"
        return result
    except Exception as e:
        return f"Ошибка при получении заметок: {e}"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
