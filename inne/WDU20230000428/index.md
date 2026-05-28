---
title: "Rozporządzenie Ministra Spraw Wewnętrznych i Administracji z dnia 6 marca 2023 r. w sprawie warunków technicznych dokonywania wpisów danych SIS oraz aktualizowania, usuwania i wyszukiwania danych SIS poprzez Krajowy System Informatyczny (KSI)"
address: WDU20230000428
eli: DU/2023/428
publisher: DU
year: 2023
pos: 428
act_type: Rozporządzenie
status: obowiązujący
domain: null
source: "eli-html"
---

# Rozporządzenie Ministra Spraw Wewnętrznych i Administracjiz dnia 6 marca 2023 r. w sprawie warunków technicznych dokonywania wpisów danych SIS oraz aktualizowania, usuwania i wyszukiwania danych SIS poprzez Krajowy System Informatyczny (KSI)

| Pole | Wartość |
|---|---|
| Adres publikacyjny | Dz.U. 2023 poz. 428 |
| ISAP | WDU20230000428 |
| Typ aktu | Rozporządzenie |
| Status | obowiązujący |
| W mocy | tak |
| Data ogłoszenia | 2023-03-06 |
| Data wydania | 2023-03-06 |
| Wejście w życie | 2023-03-07 |
| Ostatnia zmiana | 2024-03-14 |
| Źródło | [ISAP](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20230000428) · [PDF](https://api.sejm.gov.pl/eli/acts/DU/2023/428/text.pdf) |

Treść rozporządzenia
Na podstawie art. 21 ust. 1 ustawy z dnia 24 sierpnia 2007 r. o udziale Rzeczypospolitej Polskiej w Systemie Informacyjnym Schengen oraz Wizowym Systemie Informacyjnym (Dz. U. z 2021 r. poz. 1041 oraz z 2022 r. poz. 2642) zarządza się, co następuje:
§ 1.
Rozporządzenie określa:
1)
warunki techniczne, sposób i tryb dokonywania wpisów danych SIS oraz tworzenia odsyłaczy pomiędzy wpisami w SIS;
2)
sposób i tryb aktualizowania, usuwania i wyszukiwania danych SIS poprzez Krajowy System Informatyczny (KSI), zwany dalej „KSI”.
§ 2.
Ilekroć w rozporządzeniu jest mowa o:
1)
brzegowym urządzeniu sieciowym – należy przez to rozumieć urządzenie typu firewall pełniące funkcję urządzenia dostępowego do KSI, terminujące tunel VPN IPsec;
2)
CWPK SIS (Centralnym Węźle Polskiego Komponentu SIS) – należy przez to rozumieć podsystem informacyjny stanowiący część infrastruktury technicznej i organizacyjnej KSI, mający na celu zapewnienie przepływu informacji między centralnym systemem SIS a systemami teleinformatycznymi użytkowników instytucjonalnych oraz aplikacją WWW SIS;
3)
certyfikacie – należy przez to rozumieć elektroniczne zaświadczenie będące elementem PKI, wydane zgodnie z obowiązującą Polityką certyfikacji, zapewniające poufność przesyłanych danych oraz bezpieczeństwo procesu uwierzytelniania użytkownika instytucjonalnego i użytkownika indywidualnego;
4)
dopasowaniu – należy przez to rozumieć dopasowanie, o którym mowa w art. 3 pkt 7 rozporządzenia 2018/1861 oraz w art. 3 pkt 6 rozporządzenia 2018/1862;
5)
Kodeksie postępowania certyfikacyjnego – należy przez to rozumieć dokument uszczegółowiający ogólne zasady postępowania certyfikacyjnego opisane w Polityce certyfikacji;
6)
uprawnionym organie – należy przez to rozumieć organ lub służbę uprawnioną do dostępu do Krajowego Systemu Informatycznego (KSI) oraz przetwarzania danych poprzez Krajowy System Informatyczny (KSI), o których mowa w art. 3 ust. 1 ustawy;
7)
PKI (Public Key Infrastructure) – należy przez to rozumieć Infrastrukturę Klucza Publicznego będącego kryptosystemem, w którego skład wchodzą urzędy certyfikacyjne, urzędy rejestracyjne, użytkownicy certyfikatów (subskrybenci), oprogramowanie i sprzęt;
8)
podręczniku SIRENE – należy przez to rozumieć podręcznik, o którym mowa w art. 8 ust. 4 rozporządzenia 2018/1861 oraz w art. 8 ust. 4 rozporządzenia 2018/1862;
9)
Polityce certyfikacji – należy przez to rozumieć dokument określający techniczne i organizacyjne warunki oraz zakres tworzenia i stosowania certyfikatów w standardzie X.509 wykorzystywanych przez użytkowników SIS;
10)
rozporządzeniu 2018/1861 – należy przez to rozumieć rozporządzenie Parlamentu Europejskiego i Rady (UE) 2018/1861 z dnia 28 listopada 2018 r. w sprawie utworzenia, funkcjonowania i użytkowania Systemu Informacyjnego Schengen (SIS) w dziedzinie odpraw granicznych, zmiany konwencji wykonawczej do układu z Schengen oraz zmiany i uchylenia rozporządzenia (WE) nr 1987/2006 (Dz. Urz. UE L 312 z 07.12.2018, str. 14, z późn. zm.);
11)
rozporządzeniu 2018/1862 – należy przez to rozumieć rozporządzenie Parlamentu Europejskiego i Rady (UE) 2018/1862 z dnia 28 listopada 2018 r. w sprawie utworzenia, funkcjonowania i użytkowania Systemu Informacyjnego Schengen (SIS) w dziedzinie współpracy policyjnej i współpracy wymiarów sprawiedliwości w sprawach karnych, zmiany i uchylenia decyzji Rady 2007/533/WSiSW oraz uchylenia rozporządzenia Parlamentu Europejskiego i Rady (WE) nr 1986/2006 i decyzji Komisji 2010/261/UE (Dz. Urz. UE L 312 z 07.12.2018, str. 56, z późn. zm.);
12)
TLS (Transport Layer Security) – należy przez to rozumieć protokół służący do szyfrowania transmisji danych w sieci;
13)
transliteracji i transkrypcji – należy przez to rozumieć zapisywanie liter jednego alfabetu (transliteracja) lub głosek (transkrypcja) za pomocą odpowiadających im ściśle określonych zestawów znaków drugiego alfabetu, które dla danych SIS zostały określone w decyzjach wykonawczych Komisji Europejskiej do rozporządzenia 2018/1861 i do rozporządzenia 2018/1862 oraz w dokumencie kontroli interfejsu SIS i szczegółowych specyfikacjach technicznych;
14)
ustawie – należy przez to rozumieć ustawę z dnia 24 sierpnia 2007 r. o udziale Rzeczypospolitej Polskiej w Systemie Informacyjnym Schengen oraz Wizowym Systemie Informacyjnym;
15)
VPN (Virtual Private Network) – należy przez to rozumieć wirtualną sieć prywatną jako sieć przekazu danych korzystającą z publicznej infrastruktury telekomunikacyjnej, która dzięki stosowaniu protokołów tunelowania i procedur bezpieczeństwa zachowuje poufność danych;
16)
wartościach katalogowych – należy przez to rozumieć kodowany słownik danych będący zbiorem określonych dopuszczalnych wartości lub terminów wykorzystywanych przez interfejs CWPK SIS;
17)
wydzielonej sieci teleinformatycznej – należy przez to rozumieć niepubliczną sieć telekomunikacyjną, która dzięki zastosowaniu rozwiązań sprzętowych lub programowych zapewnia możliwość logicznej separacji od powszechnie dostępnej infrastruktury telekomunikacyjnej;
18)
X.509 – należy przez to rozumieć standard opisujący sposób użycia asymetrycznych algorytmów kryptograficznych.
§ 3.
Dokonywanie wpisów danych SIS oraz tworzenie odsyłaczy następuje odpowiednio za pomocą:
1)
aplikacji WWW SIS – w przypadku użytkownika indywidualnego;
2)
systemu teleinformatycznego użytkownika instytucjonalnego – w przypadku użytkownika końcowego.
§ 4.
Warunki techniczne dokonywania wpisów danych SIS oraz tworzenia odsyłaczy pomiędzy wpisami w SIS obejmują:
1)
zapewnienie połączenia z KSI za pośrednictwem wydzielonej sieci teleinformatycznej z wykorzystaniem protokołu https oraz VPN;
2)
wykorzystanie protokołu TLS i certyfikatu X.509 w celu zabezpieczenia dostępu do CWPK SIS.
§ 5.
W celu dokonywania wpisów danych SIS oraz tworzenia odsyłaczy uprawniony organ występuje do centralnego organu technicznego KSI o:
1)
wydanie certyfikatów dla brzegowego urządzenia sieciowego oraz określenie i przekazanie parametrów konfiguracji brzegowego urządzenia sieciowego dla użytkownika indywidualnego, które umożliwia bezpieczne nawiązanie połączenia z KSI;
2)
przekazywanie Polityki certyfikacji i Kodeksu postępowania certyfikacyjnego;
3)
przekazanie dokumentacji zawierającej specyfikację interfejsu CWPK SIS;
4)
założenie kont dostępowych i przydzielenie uprawnień w SIS użytkownikom indywidualnym;
5)
wydanie certyfikatów cyfrowych na potrzeby uwierzytelniania się użytkowników indywidualnych w KSI.
§ 6.
Podczas dokonywania wpisów danych SIS oraz tworzenia odsyłaczy uprawniony organ zapewnia:
1)
przestrzeganie zasad obowiązujących w Polityce certyfikacji i Kodeksie postępowania certyfikacyjnego oraz zasad obowiązujących w specyfikacji interfejsu CWPK SIS;
2)
bezpieczeństwo własnej sieci teleinformatycznej podłączonej do CWPK SIS;
3)
stosowanie specyfikacji interfejsu CWPK SIS, w tym zasad transliteracji i transkrypcji, wartości katalogowych i podręcznika użytkownika aplikacji WWW SIS;
4)
poprzedzającą dokonanie wpisu danych SIS weryfikację istnienia wpisu dotyczącego osoby lub przedmiotu oraz – w przypadku pozytywnego wyniku tej weryfikacji – przeprowadzenie konsultacji w celu zapobieżenia powstaniu niezgodności wpisów wielokrotnych, bezpośrednio z organem wymienionym w art. 3 ustawy, który dokonał wpisu, albo za pośrednictwem biura SIRENE zgodnie z zasadami określonymi w podręczniku SIRENE;
5)
przedłużenie okresu utrzymywania wpisu danych SIS nie później niż 48 godzin przed upływem terminu wygaśnięcia obowiązywania wpisu;
6)
dokonywanie wpisów danych SIS przez użytkowników indywidualnych i użytkowników końcowych w sposób zapewniający legalność i poufność tych wpisów;
7)
zachowywanie bezpieczeństwa procesu uwierzytelniania przez użytkowników indywidualnych i użytkowników końcowych;
8)
odbieranie przez użytkowników indywidualnych i użytkowników końcowych komunikatów ostrzegawczych i komunikatów dotyczących błędów oraz niezwłoczne dokonywanie aktualizacji lub usunięcia wpisów danych SIS.
§ 7.
Podczas dokonywania wpisów danych SIS oraz tworzenia odsyłaczy uprawniony organ może:
1)
utworzyć odsyłacz pomiędzy co najmniej dwoma dokonanymi przez siebie wpisami danych SIS albo pomiędzy dokonanym przez siebie wpisem lub wpisami danych SIS a wpisem lub wpisami danych SIS dokonanymi przez inny organ oraz usunąć utworzony odsyłacz;
2)
dodać kolejny wpis danych SIS do utworzonego odsyłacza oraz usunąć z odsyłacza dodany wpis;
3)
dokonać wglądu do danych odsyłacza zgodnie z przydzielonymi uprawnieniami.
§ 8.
1.
W celu dokonania wpisu danych SIS lub utworzenia odsyłacza użytkownik indywidualny:
1)
dokonuje uwierzytelnienia na podstawie otrzymanego certyfikatu cyfrowego przechowywanego na karcie mikroprocesorowej zabezpieczonej PIN-em;
2)
dokonuje wpisu danych SIS lub tworzy odsyłacz zgodnie z przydzielonymi uprawnieniami;
3)
przekazuje do biura SIRENE informacje niezbędne do celów wymiany informacji uzupełniających z organami, o których mowa w art. 3 ust. 1:
a)
pkt 1, 2, 7–10 i pkt 11 lit. b ustawy,
b)
pkt 6 ustawy, jeżeli wpis dotyczy osób, które dla ich własnej ochrony lub w celu zapobieżenia stwarzanemu przez nie zagrożeniu dla porządku publicznego lub dla bezpieczeństwa publicznego powinny zostać umieszczone we właściwej placówce opiekuńczej lub leczniczej, w szczególności w wyniku decyzji o przymusowym umieszczeniu w takiej placówce,
c)
pkt 11 lit. a ustawy, jeżeli we wnioskowanych we wpisie działaniach zastrzeżono „niezwłoczne działanie”;
4)
w przypadku dodania do wpisu danych SIS danych biometrycznych i otrzymania, po dokonaniu tego wpisu, informacji o dopasowaniu przeprowadza działania wynikające z procedury weryfikacji danych biometrycznych na etapie wprowadzania wpisów danych SIS.
2.
W celu dokonania wpisu danych SIS lub utworzenia odsyłacza użytkownik instytucjonalny:
1)
uwierzytelnia użytkownika końcowego we własnym systemie teleinformatycznym na podstawie przydzielonych uprawnień;
2)
dokonuje wpisu danych SIS lub tworzy odsyłacz za pośrednictwem użytkownika końcowego, zgodnie z przydzielonymi uprawnieniami;
3)
automatycznie przekazuje informacje uzupełniające do biura SIRENE;
4)
prowadzi elektroniczny rejestr, w którym automatycznie odnotowuje informacje dotyczące:
a)
użytkownika końcowego – ze wskazaniem numeru identyfikatora kadrowego lub innego numeru identyfikującego użytkownika końcowego,
b)
daty i godziny dokonania wpisu danych SIS,
c)
danych SIS, których dotyczył wpis,
d)
niepowtarzalnego identyfikatora wpisu danych SIS nadanego przez KSI,
e)
rodzaju czynności wykonanej za pośrednictwem KSI.
§ 9.
W przypadku braku dostępu do KSI, o którym mowa w art. 3 ust. 2 ustawy, organ występuje do centralnego organu technicznego KSI z:
1)
pisemnym wnioskiem o dokonanie wpisu danych SIS wraz z informacją o wystąpieniu przesłanek uzasadniających dokonanie wpisu za pośrednictwem centralnego organu technicznego KSI;
2)
wypełnioną kartą wpisu danych SIS, której wzór jest określony w przepisach wykonawczych wydanych na podstawie art. 22 ust. 3 ustawy.
§ 10.
1.
Aktualizowanie, usuwanie i wyszukiwanie danych SIS poprzez KSI odbywa się z wykorzystaniem:
1)
aplikacji WWW SIS przez:
a)
użytkownika indywidualnego,
b)
centralny organ techniczny KSI – w przypadku określonym w art. 22 ust. 2 ustawy;
2)
systemu teleinformatycznego użytkownika instytucjonalnego.
2.
Do aktualizowania, usuwania i wyszukiwania danych SIS poprzez KSI stosuje się odpowiednio § 8.
3.
W przypadku wyszukiwania danych SIS w rejestrze, o którym mowa w § 8 ust. 2 pkt 4, odnotowuje się również informacje dotyczące:
1)
kryteriów wyszukiwania;
2)
listy wyników wyszukiwania, do których użytkownik końcowy uzyskał dostęp.
4.
Uprawniony organ, w zakresie dokonywania weryfikacji, przedłużania i usuwania wpisów danych SIS zapewnia rejestrowanie oceny, o której mowa w art. 39 ust. 4 rozporządzenia 2018/1861 oraz w art. 53 ust. 6 rozporządzenia 2018/1862.
§ 11.
Rozporządzenie wchodzi w życie z dniem 7 marca 2023 r.
1) Minister Spraw Wewnętrznych i Administracji kieruje działem administracji rządowej – sprawy wewnętrzne, na podstawie § 1 ust. 2 pkt 2 rozporządzenia Prezesa Rady Ministrów z dnia 18 listopada 2019 r. w sprawie szczegółowego zakresu działania Ministra Spraw Wewnętrznych i Administracji (Dz. U. poz. 2264). 2) Niniejsze rozporządzenie służy stosowaniu: 1) rozporządzenia Parlamentu Europejskiego i Rady (UE) 2018/1860 z dnia 28 listopada 2018 r. w sprawie użytkowania Systemu Informacyjnego Schengen do celów powrotu nielegalnie przebywających obywateli państw trzecich (Dz. Urz. UE L 312 z 07.12.2018, str. 1, Dz. Urz. UE L 248 z 13.07.2021, str. 11 oraz Dz. Urz. UE L 249 z 14.07.2021, str. 15); 2) rozporządzenia Parlamentu Europejskiego i Rady (UE) 2018/1861 z dnia 28 listopada 2018 r. w sprawie utworzenia, funkcjonowania i użytkowania Systemu Informacyjnego Schengen (SIS) w dziedzinie odpraw granicznych, zmiany konwencji wykonawczej do układu z Schengen oraz zmiany i uchylenia rozporządzenia (WE) nr 1987/2006 (Dz. Urz. UE L 312 z 07.12.2018, str. 14, Dz. Urz. UE L 135 z 22.05.2019, str. 27, Dz. Urz. UE L 248 z 13.07.2021, str. 11 oraz Dz. Urz. UE L 249 z 14.07.2021, str. 15); 3) rozporządzenia Parlamentu Europejskiego i Rady (UE) 2018/1862 z dnia 28 listopada 2018 r. w sprawie utworzenia, funkcjonowania i użytkowania Systemu Informacyjnego Schengen (SIS) w dziedzinie współpracy policyjnej i współpracy wymiarów sprawiedliwości w sprawach karnych, zmiany i uchylenia decyzji Rady 2007/533/WSiSW oraz uchylenia rozporządzenia Parlamentu Europejskiego i Rady (WE) nr 1986/2006 i decyzji Komisji 2010/261/UE (Dz. Urz. UE L 312 z 07.12.2018, str. 56, Dz. Urz. UE L 135 z 22.05.2019, str. 85, Dz. Urz. UE L 316I z 06.12.2019, str. 4, Dz. Urz. UE L 248 z 13.07.2021, str. 1, Dz. Urz. UE L 249 z 14.07.2021, str. 1 oraz Dz. Urz. UE L 185 z 12.07.2022, str. 1). 3) Zmiany wymienionego rozporządzenia zostały ogłoszone w Dz. Urz. UE L 135 z 22.05.2019, str. 27, Dz. Urz. UE L 248 z 13.07.2021, str. 11 oraz Dz. Urz. UE L 249 z 14.07.2021, str. 15. 4) Zmiany wymienionego rozporządzenia zostały ogłoszone w Dz. Urz. UE L 135 z 22.05.2019, str. 85, Dz. Urz. UE L 316I z 06.12.2019, str. 4, Dz. Urz. UE L 248 z 13.07.2021, str. 1, Dz. Urz. UE L 249 z 14.07.2021, str. 1 oraz Dz. Urz. UE L 185 z 12.07.2022, str. 1. 5) Niniejsze rozporządzenie było poprzedzone rozporządzeniem Ministra Spraw Wewnętrznych z dnia 3 kwietnia 2013 r. w sprawie dokonywania wpisów danych SIS oraz aktualizowania, usuwania i wyszukiwania danych SIS poprzez Krajowy System Informatyczny (KSI) (Dz. U. z 2020 r. poz. 1126), które traci moc z dniem wejścia w życie niniejszego rozporządzenia zgodnie z art. 8 ust. 1 ustawy z dnia 1 grudnia 2022 r. o zmianie ustawy o udziale Rzeczypospolitej Polskiej w Systemie Informacyjnym Schengen oraz Wizowym Systemie Informacyjnym oraz niektórych innych ustaw (Dz. U. poz. 2642).

