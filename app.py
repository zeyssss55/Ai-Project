from flask import Flask, render_template, request
from questions import questions
from collections import defaultdict

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    scores = defaultdict(int)

    for q in questions:
        answer = int(request.form.get(q["id"], 0))
        scores[q["category"]] += answer

    # Mapping rekomendasi
    rekomendasi = max(scores, key=scores.get)

    jurusan_map = {
        "teknologi": ("Teknik Informatika", "Cocok untuk kamu yang suka logika, sistem, dan teknologi."),
        "psikologi": ("Psikologi", "Cocok untuk kamu yang suka memahami manusia dan perilaku."),
        "manajemen": ("Manajemen", "Cocok untuk kamu yang suka organisasi dan memimpin."),
        "desain": ("Desain Komunikasi Visual", "Cocok untuk kamu yang kreatif dan suka seni."),
        "statistik": ("Statistika", "Cocok untuk kamu yang suka angka dan analisis data."),
        "kesehatan": ("Kedokteran atau Keperawatan", "Cocok untuk kamu yang ingin menolong orang dan memahami tubuh.")
    }

    jurusan, deskripsi = jurusan_map.get(rekomendasi, ("Jurusan Tidak Dikenali", "Silakan coba lagi."))

    return render_template("result.html", scores=dict(scores), jurusan=jurusan, deskripsi=deskripsi)

if __name__ == "__main__":
    app.run(debug=True)
