# 📊 Bütçe Takip ve Analiz Uygulaması

Bu proje; kişisel gelir ve giderlerinizi kategorize ederek takip etmenizi, net bakiyenizi ve tasarruf oranınızı anlık olarak hesaplamanızı sağlayan **Python**, **Flask** ve **SQLite** tabanlı bir web uygulamasıdır.

---

## 🚀 Özellikler

- 💳 **Gelir & Gider Yönetimi:** Farklı kategorilerde harcama ve gelir kaydı oluşturma.
- 📈 **Canlı Finansal Özet:** 
  - Toplam Gelir ve Toplam Gider takibi.
  - Anlık Net Bakiye hesaplama.
  - Gelir/Gider dengesine göre dinamik Tasarruf Oranı (%) gösterimi.
- 📁 **Dinamik Kategori Sistemi:** Veritabanından çekilen dinamik kategoriler (Market, Fatura, Kira, Maaş vb.).
- 📜 **İşlem Geçmişi Tablosu:** Kaydedilen tüm işlemlerin tarih sırasına göre kategori detaylarıyla (`JOIN` yapısı) listelenmesi.
- 🎨 **Modern Arayüz:** Kullanıcı dostu ve duyarlı (responsive) CSS tasarımı.

---

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python 3, Flask
- **Veritabanı:** SQLite3
- **Şablon Motoru:** Jinja2
- **Frontend:** HTML5, CSS3

---

## 📁 Proje Yapısı

```text
├── src/
│   ├── app.py              # Flask sunucu logic'i ve rotaları (routes)
│   ├── database.py         # Veritabanı bağlantısı ve tablo oluşturma (schema)
│   ├── templates/
│   │   └── main_menu.html  # Ana sayfa HTML şablonu
│   └── static/
│       └── style.css       # Arayüz tasarım stilleri
├── README.md               # Proje dokümantasyonu
