// frontend/static/script.js
const canvas = document.getElementById('matrix-canvas');
const ctx = canvas.getContext('2d');

// Canvas boyutunu ayarla
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Akan karakterler (siberci sitesi için 0101 yapalım)
const characters = '01';
const columns = canvas.width / 20; // 20px genişliğinde sütunlar

// Sütunların yüksekliklerini tutan dizi
const drops = [];
for (let i = 0; i < columns; i++) {
    drops[i] = 1;
}

// Matrix yağmurunu çizme fonksiyonu
function drawMatrix() {
    // Hafif şeffaf siyah bir katman çizerek eski karakterlerin silinmesini sağla (kuyruk efekti)
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Karakterlerin rengi (Matrix yeşili)
    ctx.fillStyle = '#00ff41';
    ctx.font = '20px monospace';

    // Her sütun için karakter çiz
    for (let i = 0; i < drops.length; i++) {
        // Rastgele bir karakter seç
        const text = characters[Math.floor(Math.random() * characters.length)];
        
        // Karakteri çiz
        ctx.fillText(text, i * 20, drops[i] * 20);

        // Sütunun sonuna gelindiyse veya rastgele bir şekilde başa dön
        if (drops[i] * 20 > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }

        // Sütun yüksekliğini artır
        drops[i]++;
    }
}

// Animasyonu başlat (hızı ayarlamak için interval kullanalım, 50ms)
setInterval(drawMatrix, 50);

// Pencere boyutu değiştiğinde canvas'ı yeniden boyutlandır
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});