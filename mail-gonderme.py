import smtplib
from email.mime.text import MIMEText

"""
 ----- YAHOO -----
  server = smtplib.SMTP("smtp.mail.yahoo.com",587)
    server.login(username,password)
    server.sendmail(fromMy, to,msg)

"""


smtp_adresi = "smtp-mail.outlook.com"  #outlok bilgilerini girdik
smtp_port = 587
kullanici_adi = "E-Posta giriniz"
sifre = "Sifreniz"





gonderilecek_adresler = ["Gonderilecek mail adresleri"]
konu = "KONU"
icerik = "İCERİK ÖRNEK:<h1>dsadsa</h1>"

mail = MIMEText(icerik,"html","utf-8") #mail içeriğini html biçiminde ve utf-8 karakter kodlaması ile gönderilecek şekilde ayarladık.



mail["from"] = kullanici_adi
mail["Subject"] = konu
mail["To"] = ",".join(gonderilecek_adresler) #mailin gideceği adresler her mail arasına virgül koyulmalı
mail = mail.as_string() #mail bilgilerini derledik

s = smtplib.SMTP(smtp_adresi,smtp_port)
s.starttls() #TLS bağlantısı şifreli bağlantıdır
s.login(kullanici_adi,sifre) #SMTP sunucusuna giriş yapıyoruz
s.sendmail(kullanici_adi,gonderilecek_adresler,mail)   #GÖNDER
