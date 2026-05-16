---
title: Rozporządzenie Ministra Rozwoju i Finansów z dnia 1 czerwca 2017 r. w sprawie systemu teleinformatycznego rejestrującego i archiwizującego dane dotyczące przebiegu gier na automatach do gier w salonach gier na automatach
address: WDU20170001096
eli: DU/2017/1096
publisher: DU
year: 2017
pos: 1096
act_type: Rozporządzenie
status: obowiązujący
domain: null
source: "eli-html"
---

# Rozporządzenie Ministra Rozwoju i Finansówz dnia 1 czerwca 2017 r. w sprawie systemu teleinformatycznego rejestrującego i archiwizującego dane dotyczące przebiegu gier na automatach do gier w salonach gier na automatach

| Pole | Wartość |
|---|---|
| Adres publikacyjny | Dz.U. 2017 poz. 1096 |
| ISAP | WDU20170001096 |
| Typ aktu | Rozporządzenie |
| Status | obowiązujący |
| W mocy | tak |
| Data ogłoszenia | 2017-06-01 |
| Data wydania | 2017-06-07 |
| Ostatnia zmiana | 2024-03-14 |
| Źródło | [ISAP](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20170001096) · [PDF](https://api.sejm.gov.pl/eli/acts/DU/2017/1096/text.pdf) |

Treść rozporządzenia
Na podstawie art. 15ba ust. 7 ustawy z dnia 19 listopada 2009 r. o grach hazardowych (Dz. U. z 2016 r. poz. 471, 1948 i 2260 oraz z 2017 r. poz. 88, 379 i 1089) zarządza się, co następuje:
§ 1.
Rozporządzenie określa szczegółowe warunki prowadzenia i działania systemu teleinformatycznego rejestrującego i archiwizującego, o którym mowa w art. 15ba ust. 1 ustawy z dnia 19 listopada 2009 r. o grach hazardowych, zwanego dalej „systemem”.
§ 2.
1.
System jest prowadzony w warunkach zapewniających bezpieczeństwo, integralność, kompletność, poufność i rozliczalność rejestrowanych danych podczas wszystkich procesów dotyczących tych danych, w tym ich przesyłania, archiwizacji i udostępnienia. Dane należy archiwizować z zapewnieniem warunków umożliwiających określenie jednoznacznej informacji o czasie zdarzenia oraz czasie jego zapisania, z podaniem daty i czasu z dokładnością pozwalającą na określenie kolejności zdarzeń i ich archiwizacji.
2.
Zapisu danych dokonuje się w sposób uniemożliwiający ich zmianę bez wykrycia tego zdarzenia przez oprogramowanie urządzenia archiwizującego.
3.
System zapewnia możliwość odtworzenia zarchiwizowanych danych w razie ich całkowitej lub częściowej utraty, w szczególności przez kopiowanie danych na zewnętrzne nośniki.
4.
System uniemożliwia dokonywanie ingerencji oraz zmian w sposobie jego działania bez zapisania w nim informacji o tym.
§ 3.
1.
System prowadzony jest w sposób umożliwiający:
1)
wyszukiwanie, sortowanie, filtrowanie, przeglądanie i wydruk danych wymienionych w § 5, w szczególności wyszukiwanie i filtrowanie danych w podziale na automaty do gier znajdujące się w poszczególnych województwach, powiatach, gminach, salonach gier na automatach oraz na pojedyncze automaty do gier;
2)
kopiowanie danych z systemu na informatyczne nośniki danych;
3)
zdalny dostęp organów, o których mowa w art. 15ba ust. 5 ustawy z dnia 19 listopada 2009 r. o grach hazardowych, do danych z systemu wymienionych w § 5, i pobieranie tych danych z systemu uporządkowanych z zastosowaniem kryteriów, o których mowa w pkt 1, w sposób pozwalający na ich późniejszą analizę.
2.
W celu realizacji wymogów, o których mowa w § 2 ust. 1, oprogramowanie zapewnia w szczególności:
1)
dla każdego typu rejestrowanych zdarzeń ciągłą, niemodyfikowalną i jednoznacznie identyfikującą każde zdarzenie niepowtarzalną numerację;
2)
obliczanie dla każdego rejestrowanego zdarzenia skrótu kryptograficznego; skrót ten jest obliczany przy wykorzystaniu niesymetrycznego algorytmu SHA2, zgodnego z normą ISO/IEC 10118–3:2004, zwanego dalej „skrótem SHA2”;
3)
systematyczną weryfikację ciągłości numeracji rejestrowanych zdarzeń oraz ich zgodności z odpowiadającymi im skrótami SHA2 obliczonymi zgodnie z ust. 3.
3.
Skrót SHA2 jest obliczany od zawartości cyfrowej reprezentacji tego zdarzenia oraz skrótu SHA2 zdarzenia bezpośrednio poprzedzającego w numeracji, przy czym dla pierwszego zdarzenia w numeracji pomija się skrót SHA2 zdarzenia bezpośrednio poprzedzającego.
§ 4.
System:
1)
jest zabezpieczony przed nieuprawnionym dostępem, w szczególności przez zastosowanie mechanizmów uwierzytelniania i autoryzacji;
2)
zapewnia ciągłość i prawidłowość działania, w tym przez zastosowanie rozwiązań sprzętowych oraz programowych na wypadek zdarzeń, w tym losowych, które mogłyby grozić zmianą lub utratą zarchiwizowanych danych albo brakiem ich archiwizacji.
§ 5.
Wsystemie rejestrowane są, w sposób umożliwiający realizację wymogów, o których mowa w § 3:
1)
dane dotyczące wpłaconych stawek obejmujące:
a)
kwotę wpłaconej stawki,
b)
dokładny czas wpłaty stawki,
c)
formę wpłaty stawki (gotówka, karta lub wpłata zastępcza przez upoważnioną obsługę salonu gier na automatach),
d)
dane automatu do gier, na którym dokonano wpłaty stawki;
2)
dane dotyczące wypłaconych wygranych:
a)
kwotę wypłaconej wygranej,
b)
dokładny czas wypłaty wygranej,
c)
formę wypłaty wygranej (gotówka, karta lub wypłata zastępcza przez upoważnioną obsługę salonu gier na automatach),
d)
dane automatu do gier, z którego dokonano wypłaty stawki;
3)
dane dotyczące wygrywalności w przeliczeniu na zaprogramowane cykle gier;
4)
dane dotyczące przebiegu poszczególnych gier na automatach obejmujące co najmniej:
a)
dokładny czas rozpoczęcia gry,
b)
wartość stawki za grę,
c)
wartość uzyskanej wygranej;
5)
dane zawierające następujące parametry pracy automatu do gier:
a)
czas każdorazowego uruchomienia (włączenia) i unieruchomienia (wyłączenia) automatu do gier,
b)
czas prowadzonych gier na automacie do gier, w podziale na rodzaje gier;
6)
dane dotyczące miejsca lokalizacji automatu do gier oraz zmiany lokalizacji;
7)
dane dotyczące awarii automatu do gier oraz występujących błędów w działaniu i wykonywanych czynności serwisowych, w szczególności czas trwania, rodzaj oraz sposób likwidacji awarii lub błędu;
8)
dane dotyczące ingerencji i zmian dokonywanych w sposobie działania automatu do gier.
§ 6.
System umożliwia odbieranie danych, o których mowa w § 5, w postaci dokumentów elektronicznych, za pośrednictwem sieci Internet.
§ 7.
Rozporządzenie wchodzi w życie z dniem następującym po dniu ogłoszenia.
1) Minister Rozwoju i Finansów kieruje działem administracji rządowej – finanse publiczne, na podstawie § 1 ust. 2 pkt 2 rozporządzenia Prezesa Rady Ministrów z dnia 30 września 2016 r. w sprawie szczegółowego zakresu działania Ministra Rozwoju i Finansów (Dz. U. poz. 1595). 2) Niniejsze rozporządzenie zostało notyfikowane Komisji Europejskiej w dniu 30 grudnia 2016 r. pod numerem 2016/698/PL, zgodnie z § 4 rozporządzenia Rady Ministrów z dnia 23 grudnia 2002 r. w sprawie sposobu funkcjonowania krajowego systemu notyfikacji norm i aktów prawnych (Dz. U. poz. 2039 oraz z 2004 r. poz. 597), które wdraża dyrektywę (UE) 2015/1535 Parlamentu Europejskiego i Rady z dnia 9 września 2015 r. ustanawiającą procedurę udzielania informacji w dziedzinie przepisów technicznych oraz zasad dotyczących usług społeczeństwa informacyjnego (ujednolicenie) (Dz. Urz. UE L 241 z 17.09.2015, str. 1).

