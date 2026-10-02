from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection

app = Flask(__name__)



@app.route("/")
def main_menu():
    baglanti = get_db_connection()
    kategoriler = baglanti.execute("SELECT * FROM categories").fetchall()
    islemler = baglanti.execute("""
        SELECT transactions.*, categories.name AS category_name 
        FROM transactions 
        JOIN categories ON transactions.category_id = categories.id
        ORDER BY transactions.date DESC
        """).fetchall()

    toplam_gelir = 0.0
    toplam_gider = 0.0
    net_bakiye = 0.0
    tasarruf_orani = 0.0
    
    for islem in islemler:
        if islem["type"] == "income":
            toplam_gelir += islem["amount"]
        elif islem["type"] == "expense":
            toplam_gider += islem["amount"]
    
    net_bakiye = toplam_gelir - toplam_gider

    if net_bakiye > 0:
        tasarruf_orani = (net_bakiye/toplam_gelir)*100
    else:
        tasarruf_orani = 0.0

    baglanti.close()
    return render_template(
        "main_menu.html",
        kategoriler=kategoriler,
        islemler=islemler,
        toplam_gelir=toplam_gelir,
        toplam_gider=toplam_gider,
        net_bakiye=net_bakiye,
        tasarruf_orani=tasarruf_orani
        )

@app.route("/ekle", methods=["POST"])
def ekle():
    islem_tipi = request.form["type"]
    kategori_id = request.form["category_id"]
    miktar = request.form["amount"]
    tarih = request.form["date"]
    aciklama = request.form["description"]
    baglanti = get_db_connection()
    baglanti.execute(
        """
    INSERT INTO transactions (category_id, amount, type, description, date)
    VALUES (?,?,?,?,?)
    """,
    (kategori_id, miktar, islem_tipi, aciklama, tarih)
    )
    baglanti.commit()
    baglanti.close()
    return redirect(url_for("main_menu"))
    

if __name__ == "__main__":
    app.run(debug=True)