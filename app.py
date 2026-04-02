from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FARLIGHT 84 | دليل مستقبلي شامل</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Orbitron', monospace;
    background: #000;
    color: #00ffff;
    overflow-x: hidden;
    position: relative;
}

body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 80%, rgba(120,119,198,0.3) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255,119,198,0.3) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(120,219,255,0.3) 0%, transparent 50%);
    pointer-events: none;
    z-index: -1;
    animation: bgPulse 20s ease-in-out infinite;
}

@keyframes bgPulse {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 1; }
}

.header {
    background: linear-gradient(45deg, #ff00ff, #00ffff, #00ff00, #ffff00, #ff6600);
    background-size: 400% 400%;
    animation: neonGradient 4s ease infinite;
    padding: 4rem 2rem;
    text-align: center;
    position: relative;
    box-shadow: 0 0 50px #00ffff, inset 0 0 50px rgba(0,255,255,0.3);
}

@keyframes neonGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.header h1 {
    font-size: 5rem;
    font-weight: 900;
    text-shadow: 
        0 0 10px #00ffff,
        0 0 20px #00ffff,
        0 0 30px #00ffff,
        0 0 40px #ff00ff;
    animation: neonFlicker 2s infinite;
    margin-bottom: 1rem;
}

@keyframes neonFlicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.95; }
}

.header p {
    font-size: 1.6rem;
    text-shadow: 0 0 10px #00ffff;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem;
}

.section {
    background: rgba(0,0,0,0.8);
    backdrop-filter: blur(20px);
    border: 2px solid #00ffff;
    border-radius: 25px;
    padding: 3rem;
    margin: 3rem 0;
    position: relative;
    overflow: hidden;
    box-shadow: 
        0 0 30px rgba(0,255,255,0.5),
        inset 0 0 30px rgba(0,255,255,0.1);
    animation: slideInUp 1s ease-out;
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.section::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,255,255,0.4), transparent);
    transition: left 0.7s;
}

.section:hover::before {
    left: 100%;
}

.section h2 {
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 2.5rem;
    background: linear-gradient(45deg, #00ffff, #ff00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 20px #00ffff;
}

.video-section {
    border-color: #ff00ff;
    box-shadow: 
        0 0 40px rgba(255,0,255,0.6),
        inset 0 0 40px rgba(255,0,255,0.2);
}

.video-container {
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 56.25%;
    margin: 2rem 0;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 
        0 0 50px #ff00ff,
        inset 0 0 30px rgba(255,0,255,0.3);
    border: 3px solid #ff00ff;
}

iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.characters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.character-card {
    background: rgba(0,255,255,0.1);
    border: 2px solid #00ffff;
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
}

.character-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #00ffff, #ff00ff, #00ffff);
    background-size: 200% 100%;
    animation: scanLine 2s linear infinite;
}

@keyframes scanLine {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

.character-card:hover {
    transform: translateY(-15px) scale(1.05);
    box-shadow: 0 20px 60px rgba(0,255,255,0.6);
    border-color: #ff00ff;
}

.character-icon {
    font-size: 6rem;
    margin-bottom: 1.5rem;
    display: block;
    filter: drop-shadow(0 0 20px);
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.character-name {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    text-shadow: 0 0 15px #00ffff;
}

.ability {
    background: rgba(255,0,255,0.2);
    padding: 1.5rem;
    margin: 1.2rem 0;
    border-radius: 15px;
    border-left: 5px solid #ff00ff;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(255,0,255,0.3);
}

.features-list {
    list-style: none;
    padding: 0;
    font-size: 1.2rem;
}

.features-list li {
    padding: 1.2rem 0;
    padding-right: 3rem;
    position: relative;
    opacity: 0;
    animation: fadeInUp 0.8s ease forwards;
}

.features-list li:nth-child(1) { animation-delay: 0.1s; }
.features-list li:nth-child(2) { animation-delay: 0.2s; }
.features-list li:nth-child(3) { animation-delay: 0.3s; }
.features-list li:nth-child(4) { animation-delay: 0.4s; }
.features-list li:nth-child(5) { animation-delay: 0.5s; }
.features-list li:nth-child(6) { animation-delay: 0.6s; }
.features-list li:nth-child(7) { animation-delay: 0.7s; }

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.features-list li::before {
    content: '⚡';
    position: absolute;
    right: 0;
    font-size: 1.8rem;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.3); }
    100% { transform: scale(1); }
}

@media (max-width: 768px) {
    .header h1 { font-size: 3rem; }
    .container { padding: 1rem; }
    .section { padding: 2rem 1.5rem; margin: 2rem 0; }
    .characters-grid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>FARLIGHT 84</h1>
<p>نظام قتالي مستقبلي | دليل شامل للشخصيات والتكتيكات والرسوميات</p>
</div>

<div class="video-section section">
<h2>🎥 عرض رسمي للعبة</h2>
<div class="video-container">
<iframe src="https://www.youtube.com/embed/nTczHNUmI4s?autoplay=1&mute=0&loop=1&playlist=nTczHNUmI4s&controls=0&showinfo=0&rel=0&modestbranding=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>
</div>

<div class="section">
<h2>🎭 نظام الشخصيات المتقدم (6 Heroes رئيسية)</h2>
<div class="characters-grid">
<div class="character-card">
<span class="character-icon" style="color:#ff6b6b;">🦾</span>
<div class="character-name">GABRIEL</div>
<div class="ability">
<strong>Heroic Charge:</strong> اندفاع مدمر بسرعة 300% + صدمة جماعية<br>
<strong>Gravity Bomb:</strong> جذب 5 أعداء + انفجار ثقالي 200% ضرر
</div>
</div>

<div class="character-card">
<span class="character-icon" style="color:#4ecdc4;">⚡</span>
<div class="character-name">LENA</div>
<div class="ability">
<strong>Arc Dash:</strong> قفزة كهربائية 25م + صعق 3 ثواني<br>
<strong>Lightning Field:</strong> منطقة 10م تبطئ 70% + ضرر مستمر
</div>
</div>

<div class="character-card">
<span class="character-icon" style="color:#ff9500;">🔥</span>
<div class="character-name">JIN</div>
<div class="ability">
<strong>Fire Dash:</strong> مسار حرق 15م + DoT 5 ثواني<br>
<strong>Flame Wall:</strong> جدار 12م × 3م يمنع الرؤية والحركة
</div>
</div>

<div class="character-card">
<span class="character-icon" style="color:#ff69b4;">🩸</span>
<div class="character-name">FRA</div>
<div class="ability">
<strong>Blood Blade:</strong> ليتش 50% من الضرر + تنقل سريع<br>
<strong>Healing Mist:</strong> +150 HP للحلفاء في 8م
</div>
</div>

<div class="character-card">
<span class="character-icon" style="color:#00d4ff;">🎯</span>
<div class="character-name">YUKI</div>
<div class="ability">
<strong>Hawk Eye:</strong> رؤية 2كم + تتبع تلقائي<br>
<strong>Precision Shot:</strong> اختراق دروع + 250% ضرر
</div>
</div>

<div class="character-card">
<span class="character-icon" style="color:#ffd700;">🛡️</span>
<div class="character-name">MARCUS</div>
<div class="ability">
<strong>Shield Wall:</strong> 500 HP درع لـ 10 ثواني<br>
<strong>Fortify:</strong> +300 درع للحلفاء القريبين
</div>
</div>
</div>
</div>

<div class="section">
<h2>🎮 طريقة اللعب المتقدمة (Battle Royale مستقبلي)</h2>
<ul class="features-list">
<li><strong>الخريطة:</strong> 8 كم² مع 7 مناطق بيئية مختلفة (مدن مستقبلية، صحاري إشعاعية، غابات نيون)</li>
<li><strong>المركبات:</strong> 12 نوع (Hovercars, Jetbikes, Mechs, Flying Drones) مع أسلحة مدمجة</li>
<li><strong>نظام اللووت:</strong> 5 مستويات أسلحة مع 25 ترقية في المعركة (Laser Rifles, Plasma Launchers)</li>
<li><strong>دائرة السلامة:</strong> تتقلص 5 مرات مع عواصف إشعاعية تسبب ضرر</li>
<li><strong>الطاقة:</strong> 100 نقطة للقدرات + نظام Cooldown ذكي</li>
<li><strong>الأوضاع:</strong> Solo, Duo, Squad (4) + Ranked + Custom Matches</li>
<li><strong>النظام الاقتصادي:</strong> عملة FC + نظام Battle Pass مع 100+ مكافآت موسمية</li>
<li><strong>التكتيكات:</strong> هبوط استراتيجي + تدوير المنطقة + استخدام المركبات + تنسيق الفريق</li>
</ul>
</div>

<div class="section">
<h2>🌐 الرسوميات والمحرك الفني (تحليل شامل)</h2>
<ul class="features-list">
<li><strong>اسم المحرك:</strong> Unreal Engine 4.27 مع تعديلات مخصصة للأداء المحمول</li>
<li><strong>الجماليات:</strong> Cyberpunk نيون مع إضاءة Global Illumination + تأثيرات Volumetric Fog + Particle Systems متقدمة</li>
<li><strong>الإيجابيات:</strong><br>
&nbsp;&nbsp;✨ 60 FPS مستقر على 90% من الأجهزة<br>
&nbsp;&nbsp;✨ حجم 1.5 GB فقط مع Quality عالية<br>
&nbsp;&nbsp;✨ تأثيرات بصرية لكل قدرة (120+ Effect)<br>
&nbsp;&nbsp;✨ دعم HDR + 120 FPS على PC/Consoles<br>
&nbsp;&nbsp;✨ تحميل سريع (15 ثانية على WiFi جيد)<br>
&nbsp;&nbsp;✨ Anti-Aliasing مثالي بدون Blur</li>
<li><strong>السلبيات:</strong><br>
&nbsp;&nbsp;⚠️ بعض Textures منخفضة في Low-End devices<br>
&nbsp;&nbsp;⚠️ Pop-in طفيف في المركبات السريعة<br>
&nbsp;&nbsp;⚠️ عدم دعم Ray Tracing كامل (للأداء)</li>
<li><strong>مقارنة:</strong> أفضل من PUBG Mobile في الإضاءة + أخف من COD Mobile</li>
<li><strong>التقييم الفني:</strong> 9.2/10 ⭐ (ممتاز لـ Mobile BR)</li>
</ul>
</div>
</div>

<script>
// الفيديو يشتغل تلقائياً بدون click
document.addEventListener('DOMContentLoaded', function() {
    const iframe = document.querySelector('iframe');
    iframe.src = iframe.src + '&autoplay=1&mute=0';
    
    // إعادة تشغيل كل 4 دقائق
    setInterval(() => {
        iframe.src = iframe.src;
    }, 240000);
});

// إيكتات عند التصفح
window.addEventListener('mousemove', (e) => {
    const cursor = document.createElement('div');
    cursor.style.cssText = `
        position: fixed;
        width: 4px;
        height: 4px;
        background: radial-gradient(circle, #00ffff, transparent);
        border-radius: 50%;
        pointer-events: none;
        left: ${e.clientX}px;
        top: ${e.clientY}px;
        z-index: 9999;
        animation: cursorGlow 0.6s ease-out forwards;
    `;
    document.body.appendChild(cursor);
    
    setTimeout(() => cursor.remove(), 600);
});

const style = document.createElement('style');
style.textContent = `
@keyframes cursorGlow {
    0% { transform: scale(1); opacity: 1; }
    100% { transform: scale(3); opacity: 0; }
}
`;
document.head.appendChild(style);

// إيكت كتابة تظهر تدريجياً
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animationPlayState = 'running';
        }
    });
});

document.querySelectorAll('.features-list li').forEach(li => {
    li.style.animationPlayState = 'paused';
    observer.observe(li);
});
</script>
</body>
</html>
'''

if __name__ == '__main__':
    print("🚀 FARLIGHT 84 - خادم نيون يعمل!")
    print("🌐 http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
