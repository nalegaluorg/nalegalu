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
source: "isap-pdf"
---

# sprawie warunków technicznych dokonywania wpisów SIS aktualizowania, usuwania wyszukiwania SIS poprzez Krajowy System Informatyczny (KSI) Na podstawie art. 21 ust. ustawy dnia 24 sierpnia 2007 r. o udziale Rzeczypospolitej Polskiej Systemie Informacyjnym Schengen Wizowym Systemie Informacyjnym (Dz. U. 2021 r. poz. 1041 2022 r. poz. 2642) zarządza się, co następuje:

*ROZPORZĄDZENIE MINISTRA SPRAW WEWNĘTRZNYCH I ADMINISTRACJI dnia 6 marca 2023 r.*

| Pole | Wartość |
|---|---|
| Adres publikacyjny | Dz.U. 2023 poz. 428 |
| ISAP | WDU20230000428 |
| Typ aktu | Rozporządzenie |
| Status | obowiązujący |
| W mocy | tak |
| Data ogłoszenia | 2023-03-06 |
| Data wydania | 2023-03-06 |
| Ostatnia zmiana | 2024-03-14 |
| Źródło | [ISAP](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20230000428) · [PDF](https://api.sejm.gov.pl/eli/acts/DU/2023/428/text.pdf) |

1. Rozporządzenie określa:
1) warunki techniczne, sposób tryb dokonywania wpisów SIS tworzenia odsyłaczy pomiędzy wpisami SIS;
sposób tryb aktualizowania, usuwania wyszukiwania SIS poprzez Krajowy System Informatyczny (KSI), zwany dalej „KSI”.
2. Ilekroć rozporządzeniu jest mowa o:
1) brzegowym urządzeniu sieciowym należy przez to rozumieć urządzenie typu firewall pełniące funkcję urządzenia dostępowego KSI, terminujące tunel VPN IPsec;
CWPK SIS (Centralnym Węźle Polskiego Komponentu SIS) należy przez to rozumieć podsystem informacyjny stanowiący część infrastruktury technicznej organizacyjnej KSI, mający na celu zapewnienie przepływu informacji między centralnym systemem SIS a systemami teleinformatycznymi użytkowników instytucjonalnych aplikacją WWW SIS;
3) certyfikacie należy przez to rozumieć elektroniczne zaświadczenie będące elementem PKI, wydane zgodnie obowiązującą Polityką certyfikacji, zapewniające poufność przesyłanych bezpieczeństwo procesu uwierzytelniania użytkownika instytucjonalnego użytkownika indywidualnego;
7) PKI (Public Key Infrastructure) należy przez to rozumieć Infrastrukturę Klucza Publicznego będącego kryptosystemem, którego skład wchodzą urzędy certyfikacyjne, urzędy rejestracyjne, użytkownicy certyfikatów (subskrybenci), oprogramowanie sprzęt;
8) podręczniku SIRENE należy przez to rozumieć podręcznik, o którym mowa art. 8 ust. 4 2018/1861 art. 8 ust. 4 2018/1862;
9) Polityce certyfikacji należy przez to rozumieć dokument określający techniczne organizacyjne warunki zakres tworzenia stosowania certyfikatów standardzie X.509 wykorzystywanych przez użytkowników SIS;
10) rozporządzeniu 2018/1861 należy przez to rozumieć rozporządzenie Parlamentu Europejskiego Rady (UE) 2018/1861 dnia 28 listopada 2018 r. sprawie utworzenia, funkcjonowania użytkowania Systemu Informacyjnego Schengen (SIS) dziedzinie odpraw granicznych, zmiany konwencji wykonawczej układu Schengen zmiany uchylenia (WE) nr 1987/2006 (Dz. 312 07.12.2018, 14, późn. zm. );
11) rozporządzeniu 2018/1862 należy przez to rozumieć rozporządzenie Parlamentu Europejskiego Rady (UE) 2018/1862 dnia 28 listopada 2018 r. sprawie utworzenia, funkcjonowania użytkowania Systemu Informacyjnego Schengen (SIS) dziedzinie współpracy policyjnej współpracy wymiarów sprawiedliwości sprawach karnych, zmiany uchylenia decyzji Rady 2007/533/WSiSW uchylenia Parlamentu Europejskiego Rady (WE) nr 1986/2006 decyzji Komisji 2010/261/UE (Dz. 312 07.12.2018, 56, późn. zm. );
12) TLS (Transport Layer Security) należy przez to rozumieć protokół służący szyfrowania transmisji sieci;
13) transliteracji transkrypcji należy przez to rozumieć zapisywanie liter jednego alfabetu (transliteracja) lub głosek (transkrypcja) za pomocą odpowiadających im ściśle określonych zestawów znaków drugiego alfabetu, które dla danych SIS zostały określone decyzjach wykonawczych Komisji Europejskiej 2018/1861 2018/1862 dokumencie kontroli interfejsu SIS szczegółowych specyfikacjach technicznych;
14) ustawie należy przez to rozumieć ustawę dnia 24 sierpnia 2007 r. o udziale Rzeczypospolitej Polskiej Systemie Informacyjnym Schengen Wizowym Systemie Informacyjnym;
15) VPN (Virtual Private Network) należy przez to rozumieć wirtualną sieć prywatną jako sieć przekazu korzystającą publicznej infrastruktury telekomunikacyjnej, która dzięki stosowaniu protokołów tunelowania procedur bezpieczeństwa zachowuje poufność danych;
16) wartościach katalogowych należy przez to rozumieć kodowany słownik będący zbiorem określonych dopuszczalnych wartości lub terminów wykorzystywanych przez interfejs CWPK SIS;
17) wydzielonej sieci teleinformatycznej należy przez to rozumieć niepubliczną sieć telekomunikacyjną, która dzięki zastosowaniu rozwiązań sprzętowych lub programowych zapewnia możliwość logicznej separacji od powszechnie dostępnej infrastruktury telekomunikacyjnej;
18) X.509 należy przez to rozumieć standard opisujący sposób użycia asymetrycznych algorytmów kryptograficznych.
3. Dokonywanie wpisów SIS tworzenie odsyłaczy następuje odpowiednio za pomocą:
1) aplikacji WWW SIS przypadku użytkownika indywidualnego;
systemu teleinformatycznego użytkownika instytucjonalnego przypadku użytkownika końcowego.
1) wydanie certyfikatów dla brzegowego urządzenia sieciowego określenie przekazanie parametrów konfiguracji brzegowego urządzenia sieciowego dla użytkownika indywidualnego, które umożliwia bezpieczne nawiązanie połączenia KSI;
przekazywanie Polityki certyfikacji Kodeksu postępowania certyfikacyjnego;
3) przekazanie dokumentacji zawierającej specyfikację interfejsu CWPK SIS;
4) założenie kont dostępowych przydzielenie uprawnień SIS użytkownikom indywidualnym;
5) wydanie certyfikatów cyfrowych na potrzeby uwierzytelniania się użytkowników indywidualnych KSI.
6. Podczas dokonywania wpisów SIS tworzenia odsyłaczy uprawniony organ zapewnia:
1) przestrzeganie zasad obowiązujących Polityce certyfikacji Kodeksie postępowania certyfikacyjnego zasad obowiązujących specyfikacji interfejsu CWPK SIS;
bezpieczeństwo własnej sieci teleinformatycznej podłączonej CWPK SIS;
3) stosowanie specyfikacji interfejsu CWPK SIS, tym zasad transliteracji transkrypcji, wartości katalogowych podręcznika użytkownika aplikacji WWW SIS;
4) poprzedzającą dokonanie wpisu SIS weryfikację istnienia wpisu dotyczącego osoby lub przedmiotu przypadku pozytywnego wyniku tej weryfikacji przeprowadzenie konsultacji celu zapobieżenia powstaniu niezgodności wpisów wielokrotnych, bezpośrednio organem wymienionym art. 3 ustawy, który dokonał wpisu, albo za pośrednictwem biura SIRENE zgodnie zasadami określonymi podręczniku SIRENE;
5) przedłużenie okresu utrzymywania wpisu SIS nie później niż 48 godzin przed upływem terminu wygaśnięcia obowiązywania wpisu;
6) dokonywanie wpisów SIS przez użytkowników indywidualnych użytkowników końcowych sposób zapewniający legalność poufność tych wpisów;
7) zachowywanie bezpieczeństwa procesu uwierzytelniania przez użytkowników indywidualnych użytkowników końcowych;
8) odbieranie przez użytkowników indywidualnych użytkowników końcowych komunikatów ostrzegawczych komunikatów dotyczących błędów niezwłoczne dokonywanie aktualizacji lub usunięcia wpisów SIS.
7. Podczas dokonywania wpisów SIS tworzenia odsyłaczy uprawniony organ może:
1) utworzyć odsyłacz pomiędzy co najmniej dwoma dokonanymi przez siebie wpisami SIS albo pomiędzy dokonanym przez siebie wpisem lub wpisami SIS a wpisem lub wpisami SIS dokonanymi przez inny organ usunąć utworzony odsyłacz;
dodać kolejny wpis SIS utworzonego odsyłacza usunąć odsyłacza dodany wpis;
3) dokonać wglądu odsyłacza zgodnie przydzielonymi uprawnieniami.
8. 1. W celu dokonania wpisu SIS lub utworzenia odsyłacza użytkownik indywidualny:
1) dokonuje uwierzytelnienia na podstawie otrzymanego certyfikatu cyfrowego przechowywanego na karcie mikroprocesorowej zabezpieczonej PIN-em;
dokonuje wpisu SIS lub tworzy odsyłacz zgodnie przydzielonymi uprawnieniami;
2. W celu dokonania wpisu SIS lub utworzenia odsyłacza użytkownik instytucjonalny:
1) uwierzytelnia użytkownika końcowego we własnym systemie teleinformatycznym na podstawie przydzielonych uprawnień;
dokonuje wpisu SIS lub tworzy odsyłacz za pośrednictwem użytkownika końcowego, zgodnie przydzielonymi uprawnieniami;
3) automatycznie przekazuje informacje uzupełniające biura SIRENE;
4) prowadzi elektroniczny rejestr, którym automatycznie odnotowuje informacje dotyczące:
a) użytkownika końcowego ze wskazaniem numeru identyfikatora kadrowego lub innego numeru identyfikującego użytkownika końcowego,
b) daty godziny dokonania wpisu SIS,
c) SIS, których dotyczył wpis,
d) niepowtarzalnego identyfikatora wpisu SIS nadanego przez KSI,
e) rodzaju czynności wykonanej za pośrednictwem KSI.
9. W przypadku braku KSI, o którym mowa art. 3 ust. 2 ustawy, organ występuje centralnego organu technicznego KSI z:
1) pisemnym wnioskiem o dokonanie wpisu SIS wraz informacją o wystąpieniu przesłanek uzasadniających dokonanie wpisu za pośrednictwem centralnego organu technicznego KSI;
wypełnioną kartą wpisu SIS, której wzór jest określony przepisach wykonawczych wydanych na podstawie art. 22 ust. 3 ustawy.
10. 1. Aktualizowanie, usuwanie wyszukiwanie SIS poprzez KSI odbywa się wykorzystaniem:
1) aplikacji WWW SIS przez:
a) użytkownika indywidualnego,
b) centralny organ techniczny KSI przypadku określonym art. 22 ust. 2 ustawy;
systemu teleinformatycznego użytkownika instytucjonalnego.
2. Do aktualizowania, usuwania wyszukiwania SIS poprzez KSI stosuje się odpowiednio 8.
3. W przypadku wyszukiwania SIS rejestrze, o którym mowa 8 ust. 2 4, odnotowuje się również informacje dotyczące:
1) kryteriów wyszukiwania;
listy wyników wyszukiwania, których użytkownik końcowy uzyskał dostęp.
4. Uprawniony organ, zakresie dokonywania weryfikacji, przedłużania usuwania wpisów SIS zapewnia rejestrowanie oceny, o której mowa art. 39 ust. 4 2018/1861 art. 53 ust. 6 2018/1862.
11. Rozporządzenie wchodzi życie dniem 7 marca 2023 r.
Minister Spraw Wewnętrznych Administracji: M. Kamiński

