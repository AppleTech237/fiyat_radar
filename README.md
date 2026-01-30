# FİYAT RADAR

**Grup Adı:** Fiyat Radar<br>
**Teknolojiler:** Python 3.x, Django 4.x, Bootstrap 5, SQLite



## Grup Üyeleri ve Görev Dağılımı

Bu proje, ekip çalışması ile modüler bir yapıda geliştirilmiştir. Her üye belirli uygulamaların (Apps) ve sayfaların geliştirilmesinden sorumludur.

| Öğrenci Adı Soyadı | Sorumluluk Alanları (Apps & Dosyalar) |
| :--- | :--- |
| **Gaius Joresse Azangue Tengam** | **Products & Alerts (Ürünler ve Uyarılar)**<br>• `products/` (Tüm yapı)<br>• `templates/products/` (all_products, product_detail)<br>• `alerts_form.html`, `alerts_confirm_delete.html`<br>• Fiyat Karşılaştırma ve Arama Mantığı<br>• Kullanıcı Deneyimi (UX) İyileştirmeleri |
| **Jean Innocent Manta Nsangou** | **Accounts & Stores (Hesaplar ve Mağazalar)**<br>• `accounts/` (views.py, forms.py, urls.py)<br>• `login.html`, `register.html`, `user_profile.html`<br>• `stores/` (models.py, views.py, urls.py)<br>• Mağaza veritabanı yapısı |
| **Matias Fernando Ndong Owono** <br> **Mario Enrique Motede Dasilva** | **Pages & Static Content (Statik Sayfalar)**<br>• `pages/` (urls.py, views.py)<br>• `home.html` (Ana Sayfa)<br>• `about.html` (Hakkımızda)<br>• `contact.html` (İletişim)<br>• `store_list.html` (Mağaza Listesi Arayüzü) |



## Projenin Amacı ve Kapsamı (Ön Fizibilite)

**Fiyat Radar**, Django framework’ü temel alınarak geliştirilen bir web tabanlı uygulamadır. Bu uygulama, kullanıcıların çeşitli marketlerde satışa sunulan ürünlerin fiyatlarını karşılaştırmalarını sağlayarak daha rasyonel ve ekonomik alışveriş kararları almalarına yardımcı olmayı amaçlamaktadır.

### Temel Hedefler:
1. **Fiyat Karşılaştırma:** Farklı satıcılardaki fiyatları tek ekranda sunarak süreci hızlandırmak.
2. **Ekonomik Alışveriş:** Kullanıcının en uygun fiyatı bulmasına yardımcı olmak.
3. **Kullanıcı Dostu Arayüz:** Sade, modern ve responsive (mobil uyumlu) bir tasarım sunmak.
4. **Teknik Gelişim:** Django tabanlı web uygulaması geliştirme becerilerini (CRUD, Auth, MVT) pekiştirmek.



## SWOT Analizi

| **Güçlü Yönler (Strengths)** | **Zayıf Yönler (Weaknesses)** |
| :--- | :--- |
|  **Tam Modüler Yapı:** Proje, görev dağılımına uygun olarak `products`, `accounts`, `stores` app'lerine ayrılmıştır.<br> **CRUD Özellikleri:** Ürün ve Alarm ekleme/silme/düzenleme fonksiyonları aktiftir.<br> **Güvenlik:** Django Auth sistemi ile güvenli oturum yönetimi.<br> **Responsive Tasarım:** Bootstrap ile tüm cihazlarda düzgün görüntüleme. |  **Otomasyon Eksikliği:** Fiyatlar şu an için manuel girilmektedir (Web scraping entegrasyonu sonraki aşamadır).<br> **Veri Girişi:** Ürün veritabanının elle doldurulması zaman almaktadır. |

| **Fırsatlar (Opportunities)** | **Tehditler (Threats)** |
| :--- | :--- |
| **Enflasyon:** Fiyat dalgalanmaları nedeniyle bu tür uygulamalara olan ihtiyaç artmaktadır.<br> **Mobil Entegrasyon:** API desteği ile mobil uygulamaya dönüştürülebilir. |  **Rakipler:** Akakçe, Cimri gibi büyük pazar liderleri.<br>⚔️ **Sunucu Maliyetleri:** Veri tabanı büyüdükçe barındırma maliyeti artabilir. |



## Proje Dosya Yapısı

```text
fiyat_radar/
│
├── accounts/      → Kullanıcı yönetimi (login, register, user_profile)        
├── pages/         → Statik sayfalar (Home, About, Contact)      
├── products/      → Ürünler, Fiyat Karşılaştırma ve Alarmlar (CRUD)    
├── stores/        → Market listesi ve market detayları          
├── templates/     → Global şablonlar (base.html, navbar.html, footer.html)                                  
├── static/        → CSS, JS ve görseller (style.css)                        
├── media/         → Yüklenen ürün görselleri                    
├── manage.py      → Django proje giriş noktası
└── README.md      → Proje Dokümantasyonu
