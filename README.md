Pythonlog
Pythonlog Monitor, bilgisayarınızın sistem durumunu kapsamlı bir şekilde izleyen ve anlık olarak loglayan güçlü bir yazılımdır. Bu program, dosya sistemi değişikliklerini, çalışan süreçleri, ağ trafiğini, CPU ve bellek kullanımını, kullanıcı aktivitelerini ve anlık olarak açık olan uygulamaları takip edebilir. Ayrıca, bu bilgileri kullanıcıya grafiksel gösterimlerle sunar.

Özellikler
Dosya Sistemi İzleme: Program, dosya sisteminde meydana gelen her türlü değişikliği (oluşturma, silme, taşıma, değiştirme) anlık olarak takip eder ve loglar.
Süreç İzleme: Bilgisayarınızda çalışan süreçleri izler, CPU ve bellek kullanım oranlarını takip eder ve loglar.
Ağ Trafiği İzleme: Canlı ağ trafiğini izler, paketlerin kaynak ve hedef IP adreslerini, kullanılan protokolleri loglar.
Sistem Performansı İzleme: CPU, bellek ve disk kullanımını grafiksel olarak gösterir ve bu bilgileri loglar.
Kullanıcı Etkinlikleri: Klavye ve fare aktivitelerini izler ve loglar.
Açık Uygulamalar Takibi: Anlık olarak bilgisayarınızda açık olan uygulamaları ayrı bir pencerede gösterir.
Grafiksel Gösterim: CPU ve bellek kullanımını gerçek zamanlı grafiklerle izleyebilirsiniz.
Kullanıcı Dostu Arayüz: Kullanıcıya loglama işlemlerini kolayca başlatma, durdurma ve logları kaydetme imkanı sunan basit ve etkili bir arayüz.
Gereksinimler
Bu programı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

psutil: Sistem süreçleri, CPU, bellek ve disk kullanımı gibi bilgileri izlemek için kullanılır.
pyshark: Ağ trafiğini izlemek için kullanılır.
watchdog: Dosya sistemi olaylarını izlemek için kullanılır.
tkinter: Kullanıcı arayüzü oluşturmak için kullanılır (Python ile birlikte gelir, ayrıca yüklenmesine gerek yoktur).
matplotlib: Grafiksel gösterimler (örneğin CPU ve bellek kullanım grafikleri) oluşturmak için kullanılır.
pynput: Klavye ve fare olaylarını izlemek için kullanılır.
Gerekli kütüphaneleri kurmak için, proje dizininde aşağıdaki komutu çalıştırabilirsiniz:

bash
Kodu kopyala
pip install -r requirements.txt
Kurulum ve Kullanım
Adım 1: Proje dosyalarını bilgisayarınıza indirin veya kopyalayın.
Adım 2: Gerekli kütüphaneleri yüklemek için yukarıda belirtilen komutu çalıştırın.
Adım 3: Python dosyasını çalıştırarak programı başlatın:
bash
Kodu kopyala
python ultimate_system_monitor.py
Adım 4: Program açıldığında, "Start Logging" butonuna tıklayarak sistem izlemeyi başlatın. Program, belirlediğiniz özellikleri anlık olarak izleyip loglayacak ve sonuçları kullanıcı arayüzünde gösterecektir.
Adım 5: İstediğiniz zaman "Stop Logging" butonuna tıklayarak izleme işlemini durdurabilirsiniz.
Adım 6: "Save Log" butonuna tıklayarak logları bir dosyaya kaydedebilirsiniz.
Adım 7: "Plot CPU Usage" ve "Plot Memory Usage" butonlarını kullanarak CPU ve bellek kullanımını grafiksel olarak izleyebilirsiniz.
Adım 8: "Show Open Applications" butonuna tıklayarak anlık olarak açık olan uygulamaları ayrı bir pencerede görebilirsiniz.
