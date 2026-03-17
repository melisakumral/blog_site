# 🛡️Siber Günlük

Bu proje, modern web teknolojileri ve siber güvenlik prensipleri birleştirilerek geliştirilmiş, güvenli bir **İstihbarat ve Analiz Paylaşım Platformu**dur. Bir bilgisayar mühendisi vizyonuyla, güvenli oturum yönetimi ve dinamik içerik kontrolü odaklı inşa edilmiştir.

## 🛠️ Teknik Altyapı
- **Backend:** Python & Flask (Restful Mimari)
- **Veritabanı:** SQLite & SQLAlchemy ORM
- **Güvenlik:** Werkzeug (Password Hashing - scrypt), Session Management, .env Configuration
- **Frontend:** HTML5, CSS3 (Neon-Cyberpunk UI), JavaScript (Matrix Matrix Effect)

## 🔐 Güvenlik Özellikleri
- **Password Hashing:** Şifreler veritabanında asla düz metin olarak tutulmaz; `scrypt` algoritması ile tuzlanarak hashlenir.
- **Session Control:** Admin paneli ve silme işlemleri, sadece yetkilendirilmiş oturumlar tarafından gerçekleştirilebilir.
- **Environment Variables:** Kritik anahtarlar ve veritabanı yolları `.env` dosyası ile koddan izole edilmiştir.
- **Information Exposure Prevention:** Hatalı girişlerde saldırganlara ipucu vermeyen genel hata mesajları kullanılır.

## 🚀 Kurulum ve Çalıştırma

1. Projeyi klonlayın: `git clone https://github.com/kullaniciadi/barslab.git`
2. Sanal ortamı oluşturun: `python -m venv venv`
3. Bağımlılıkları yükleyin: `pip install -r requirements.txt`
4. Admin kullanıcısını oluşturun: `python create_admin.py`
5. Uygulamayı başlatın: `python app.py`

---
**Melisa Kumral** 
