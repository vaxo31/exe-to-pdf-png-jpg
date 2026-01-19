🛠️ Dankek-Softwares | RTLO & Icon Spoofer
Bu araç, pentest çalışmalarında .exe dosyalarının uzantılarını ve ikonlarını manipüle ederek kullanıcı farkındalık testleri yapmanıza olanak tanır. Dankek-Softwares çatısı altında geliştirilen bu proje, RTLO (Right-to-Left Override) tekniğini kullanarak dosyaları görsel olarak farklı formatlarda (.pdf, .png, .jpg) gösterir.

✨ Özellikler
Dinamik İsimlendirme: Seçilen EXE'nin orijinal adını korur ve manipülasyonu bu isim üzerine uygular.

İkon Gömme: İstenilen .ico dosyasını otomatik olarak EXE içerisine entegre eder.

Gelişmiş RTLO: Unicode karakterleri kullanarak sistemde sahte uzantı görünümü sağlar.

Dosya Kilitleme: Oluşturulan dosyayı "Salt Okunur" yaparak üzerine yazılmasını engeller.

Modern GUI: Dankek-Softwares imzalı, karanlık mod destekli şık arayüz.

🚀 Kurulum
Projeyi çalıştırmak veya derlemek için gerekli kütüphaneleri kurun:

Bash
pip install Pillow pyinstaller
💻 Kullanım
main.py dosyasını çalıştırın.

Hedef EXE dosyasını seçin.

(Opsiyonel) Görünmesini istediğiniz bir İkon (.ico) dosyası seçin.

Hedef formatı (PDF, PNG, JPG) belirleyin.

GENERATE & LOCK butonuna basın.

🛠️ EXE Haline Getirme
Aracı tek bir yürütülebilir dosya yapmak için:

Bash
pyinstaller --onefile --noconsole --name "DankekSpoofer" main.py
⚠️ Yasal Uyarı
Bu araç Mert tarafından yalnızca eğitim ve pentest (sızma testi) amaçlı geliştirilmiştir. Kötü niyetli kullanımlardan geliştirici sorumlu tutulamaz.
