---
title: Rozporządzenie Ministra Administracji i Cyfryzacji z dnia 12 grudnia 2014 r. w sprawie szczegółowych wymagań dotyczących zasad adresowania dla właściwego kierowania połączeń
address: WDU20150000012
eli: DU/2015/12
publisher: DU
year: 2015
pos: 12
act_type: Rozporządzenie
status: obowiązujący
domain: null
source: "isap-pdf"
---

# RZECZYPOSPOLITEJ POLSKIEJ Warszawa, dnia 5 stycznia 2015 r.

| Pole | Wartość |
|---|---|
| Adres publikacyjny | Dz.U. 2015 poz. 12 |
| ISAP | WDU20150000012 |
| Typ aktu | Rozporządzenie |
| Status | obowiązujący |
| W mocy | tak |
| Data ogłoszenia | 2014-12-12 |
| Data wydania | 2015-01-05 |
| Ostatnia zmiana | 2024-08-14 |
| Źródło | [ISAP](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20150000012) · [PDF](https://api.sejm.gov.pl/eli/acts/DU/2015/12/text.pdf) |

ROZPORZĄDZENIE MINISTRA ADMINISTRACJI I CYFRYZACJI dnia grudnia 2014 r.
sprawie szczegółowych wymagań dotyczących zasad adresowania dla właściwego kierowania połączeń Na podstawie art. 126 ust. 13 ustawy dnia 16 lipca 2004 r. Prawo telekomunikacyjne (Dz. U. 2014 r. poz. 243, 827 i 1198) zarządza się, co następuje: § 1. Rozporządzenie określa szczegółowe wymagania dotyczące zasad adresowania dla właściwego kierowania połączeń, stanowiące załącznik do rozporządzenia.
§ 2. Rozporządzenie wchodzi życie po upływie 14 dni od dnia ogłoszenia.
Minister Administracji i Cyfryzacji: A. Halicki SZCZEGÓŁOWE WYMAGANIA DOTYCZĄCE ZASAD ADRESOWANIA DLA WŁAŚCIWEGO KIEROWANIA POŁĄCZEŃ § 1. Informacja adresowa o numerze abonenta wywołującego powinna być niezmienna na całej drodze połączeniowej, zastrzeżeniem § 2.
§ 2. Numer zastępujący numer abonenta (numer techniczny) powinien być wykorzystywany przy:
1) realizowaniu połączenia na numery alarmowe telekomunikacyjnego urządzenia końcowego bez użycia przez abonenta wielofunkcyjnej, inteligentnej karty identyfikacyjnej (Subscriber Identity Module), zwanej dalej „kartą SIM”, lub
2) używaniu przez abonenta, przypadku braku zasięgu, połączeniu na numery alarmowe, karty SIM zalogowanej sieci innej niż sieć wykorzystywana przez dostawcę usług, którym abonent wywołujący zawarł umowę o świadczenie usług telekomunikacyjnych.
§ 3. Dla numeracji służącej realizacji uprawnień abonentów do przenoszenia przydzielonego numeru pomiędzy dostawcami usług, dla przypadków, gdy występuje zmiana sieci, ustala się:
1) następujące zasady adresowania dla właściwego kierowania połączeń zakresie numeracji służącej realizacji uprawnień abonenta do przenoszenia przydzielonego numeru pomiędzy dostawcami usług:
a) numer rutingowy (NR NP) zamieszcza się parametrze Called Party Number wiadomości IAM (Initial Address Message) przed numerem abonenta B (tryb połączony „concatenated”),
b) parametr NoA (Nature of Address) przyjmuje wartość 3,
c) adresowanie metodą „en-bloc” ,
d) numer rutingowy (NR NP) dołącza się po odpytaniu bazy dla numerów przeniesionych; dopuszcza się dołączenie numeru rutingowego (NR NP) po odpytaniu bazy dla numerów nieprzeniesionych;
2) następujący format numeru rutingowego (NR NP): NR NP (5 cyfr) = „C hex” + XYZT, gdzie:
a) dla numerów geograficznych: XY = AB = wskaźnik strefy numeracyjnej SN (X=1–9), ZT = numer HOST (HOST ID) danej SN (dla danego AB),
b) dla numerów niegeograficznych: XYZT numer sieci (X = 0).
§ 4. Dla numeracji służącej realizacji wywołań do trzycyfrowych numerów AUS i numeru alarmowego 112 ustala się:
1) następujące zasady kierowania ruchu:
a) połączenia do trzycyfrowych numerów AUS oraz numeru alarmowego 112 mogą być realizowane po odebraniu numeru tylko formatach: XYZ (3 cyfry) łącza abonenckiego, WSNd (2 cyfry) + „C hex” + IDL (3 cyfry) + XYZ (3 cyfry) łącza międzycentralowego, tym łącza międzyoperatorskiego,
b) numer kierowania alarmowego (NKA), związany położeniem abonenta obszarze gminy, jest wprowadzany
d) NKA powinien być niezmienny na całej drodze połączeniowej,
e) zamiana NKA na numer krajowy KNA (numer podkładowy) następuje centrali bezpośrednio obsługującej jednostkę, do której kierowane jest wywołanie alarmowe na trzycyfrowy numer AUS lub numer alarmowy 112;
2) następujący format NKA: NKA = WSNd (2 cyfry) + „C hex” + IDL (3 cyfry) + XYZ (3 cyfry), gdzie: WSNd (Wskaźnik Strefy Numeracyjnej docelowej) oznacza strefę numeracyjną, jakiej znajduje się jednostka, do której kierowane jest wywołanie alarmowe, IDL (Identyfikator Docelowej Lokalizacji) wskazuje jednostkę, do której kierowane jest wywołanie alarmowe, występującą danej lokalizacji danej strefie numeracyjnej, XYZ oznacza wybrany trzycyfrowy numer AUS i numer alarmowy 112.

