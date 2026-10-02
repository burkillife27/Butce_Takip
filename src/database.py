import sqlite3
from pathlib import Path

def get_db_connection():
    # 1. Kodun yolunu al
    kod_yolu = Path(__file__).resolve()
    # 2. İki kez üste çık(Ana klasöre).
    proje_ana_dizini = kod_yolu.parent.parent
    # 3. DB yolunu oluştur.
    db_yolu = proje_ana_dizini / "data" / "Bütçe planlama ve takip.db"
    # 4. data kalsörünü oluştur.
    db_yolu.parent.mkdir(parents=True, exist_ok=True)
    # 5. Bağlantıyı kur.
    baglanti = sqlite3.connect(db_yolu)
    # Verileri isimleriyle okuyabilmek için ayar.
    baglanti.row_factory = sqlite3.Row
    # Bağlantıyı teslim et.
    return baglanti


def init_db():
    baglanti = get_db_connection()
    imlec = baglanti.cursor()

    imlec.execute("""
        CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL CHECK(type IN('expense', 'income'))
        )
    """)
    #Kategori tablosu oluşturma

    imlec.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        type TEXT CHECK (type IN ('income', 'expense')) NOT NULL,
        description TEXT,
        date DATE NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """)
    #İşlemler tablosu oluşturma

    imlec.execute("""
        CREATE TABLE IF NOT EXISTS monthly_budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year_month TEXT UNIQUE NOT NULL,
        target_amount REAL NOT NULL
        )
    """)
    #Aylık bütçe hedefi tablosu

    imlec.execute("""
    INSERT INTO categories (name, type)
    VALUES 
        ('Market', 'expense'),
        ('Fatura', 'expense'),
        ('Kira', 'expense'),
        ('Maaş', 'income'),
        ('Diğer Gelir', 'income')
    """)
    #Kategori tablosuna varsayılan öğeleri yükler.
    
    baglanti.commit()
    baglanti.close()

if __name__ == "__main__":
    init_db()