from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Önce varsa eski admini silelim ki çakışmasın
    User.query.filter_by(username='admin').delete()
    
    # Hashlenmiş şifre oluştur (Siber güvenlik budur!)
    hashed_pw = generate_password_hash("1234mel123456")
    
    # Veritabanına mühürle
    new_admin = User(username='admin', password=hashed_pw)
    db.session.add(new_admin)
    db.session.commit()
    print("✓ BAŞARILI: Admin kullanıcısı veritabanına eklendi.")