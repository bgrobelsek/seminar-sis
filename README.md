# Prikupljanje podataka o sustavu za upravljanje sadržajem (CMS) sa određenih web stranica 

## Kratki opis rada
Korištenjem besplatnog CMS alata CMSeeK iz prethodno upisanih web stranica koje se nalaze u url.txt datoteci dohvaćaju se informacije o svakoj stranici iz datoteke. Nakon toga se zapišu u json datoteku koja nosi isti naziv stranice. Informacije su raznolikog karaktera poput url-a, cms_id-a, wordpress licence itd. 

* **json_csv_sorting.py** json datoteke se pretvaraju u CSV datoteke i sortiraju po CMS-u u nove foldere čiji root folder je /cms_csv/. Nakon što je završen proces otvara se taj folder.

* **ip_dns.py** čita zapise u /cms_csv/, izvlači URL adrese, pronalazi IP adresu i NS zapise i to zapisuje u mapu /IP-DNS/. Nakon što je proces završen otvara se taj folder.

* **encrypto.py** se koristi kako bi odabrali folder, sve .csv datoteke unutar foldera se eknriptiraju koristeći Fernet ključ - preko tog istog ključa se navedene datoteke i dekriptiraju

Navedene .py datoteke, uključujući i CMSeeK se pokreću preko jednostavnog TKinter sučelja. 

### Rad se sastoji od dvije glavne komponente:
* CMS alata [CMSeeK](https://github.com/Tuhinshubhra/CMSeeK#requirements-and-compatibility)
* Projekta koji sadrži ostale komponente i datoteke na kojima su radili studenti

## Zahtjevi i kompatibilnost:
CMSeeK i ovaj projekt su napravljeni koristeći python3 koji će vam trebati za pokretanje ovog alata i kompatibilan je sa sustavima temeljenim na unixu. CMSeeK se oslanja na git za automatsko ažuriranje pa provjerite je li git instaliran na vašem računalu.

## Instalacija i uporaba:
CMSeeK
* git clone https://github.com/bgrobelsek/seminar-sis.git
* cd CMSeek
* ip/pip3 install -r requirements.txt
  
Dodatni python3 moduli za instalaciju:
* fernet 
* cryptography.fernet
* dns.resolver 
* PIL

  
### Uporaba:
Nakon instaliranih modula pozicionirajte se unutar root foldera projekta i otvorite iz njega terminal.
> python3 run.py

Koristeći ScriptMe sučelje krenite s aktivacijom svakog progama tipku po tipku.

CMSeeK će prikazati svoj rad i završetak istog kroz terminal.

JSON/SORT i IP_DNS kada se završe otvoriti će foldere u kojima su prebacili .csv datoteke.

Kada pokrenete Encyrpto - preko **Browse** tipke nađite i odaberite folder 'Projekt' i stisnite **Encrypt**. 

Vaše .csv datoteke su enkriptirane!

p.s. nemojte zaboraviti obrisati trag koristeći **DELETE EVERYTHING** tipku ;)

![TKinter](Projekt/Screenshots/scriptme.png)

![Encrypto](Projekt/Screenshots/encrypto.png)


## Zaključak:

Koristeći se CMSeeK-om uspješno su prikupljeni podaci sa odabranih mrežnih stranica te su sortirani u datoteke po vrsti CMS-a koju koriste, a prikupljeni su i još neki dodatni podaci ovisno o kojem se CMS-u radi. Prikupljeni podaci potom su, pomoću drugog programa, uspješno kriptirani i dekriptirani čime je simulirana transakcija sa zainteresiranim strankama, ali i čuvanje od pokušaja krađe. Kombinacijom rješenja ukazalo se na problem lakoće pristupa nekim podacima, podacima koji mogu znatno olakšati pripremu napada na stranicu. Na primjer, saznavanjem korisničkog imena administratora olakšan je bruteforce napad što je znatno brže nego kada se bruteforce napad koristi za probijanje/saznavanje oba podatka. Na temelju izvedenih pokušaja i dobivenih rezultata programsko rješenje se pokazalo dobrim za ispunjenje cilja ovog projekta te postoji prostor za daljnje unaprjeđivanje i doradu istog. 
 
Simulacija ujedno ukazuje na ranjivost i nedovoljnu zaštitu osnovnih postavki većine CMS sustava. Wordpress, kao najzastupljeniji CMS, je ujedno i najkritičniji po pitanju sigurnosti. Model  i podaci u ovoj simulaciji mogu pružiti informacije o određenoj verziji Wordpress-a kao i o verzijama dodataka (eng. plug-in) koji se koriste te je moguće definirati kritičnu skupinu za eventualni napad odabirom određene verzije za koju je poznato da ima sigurnosnu ranjivost. 
 
Uz destruktivan primjer obrađene podatke moguće je koristiti i na pozitivan način u marketinške svrhe nudeći bolje i kvalitetnije usluge hostinga u odnosu na one koje pruža trenutni pružatelj usluga.

## Prikupljanje podataka o sustavu za upravljanje sadržajem (CMS) sa određenih web stranica 

**Smjer i vrsta studija:** 
Održavanje računalnih sustava, izvanredni 

**Predmetni nastavnik:** 
Antun Matija Filipović, v. pred., mag.

**Studenti:** 
* Gabud Mario
* Grobelšek Bruno
* Babuder Ivan
* Blažić Marin
* Hodak Filip
* Javor Luka
* Joskić Ivan
* Jurić Matej
* Pernjek Anto
* Sabol Luka
* Mezga Alen
* Žanić Ivan
* Borozan Vedran
* Ivošević-Podjed Kristijan
   
