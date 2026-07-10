---
title: Rozporządzenie Ministra Spraw Wewnętrznych i Administracji z dnia 26 marca 2025 r. w sprawie warunków technicznych przetwarzania danych przez Krajowy System Informatyczny do spraw Systemu Wjazdu/Wyjazdu
address: WDU20250000411
eli: DU/2025/411
publisher: DU
year: 2025
pos: 411
act_type: Rozporządzenie
status: obowiązujący
domain: null
source: pdf
---

# RZECZYPOSPOLITEJ POLSKIEJ Poz. 411 ROZPORZĄDZENIE MINISTRA SPRAW WEWNĘTRZNYCH I ADMINISTRACJI z dnia 26 marca 2025 r.

| Pole | Wartość |
|---|---|
| Adres publikacyjny | Dz.U. 2025 poz. 411 |
| ISAP | WDU20250000411 |
| Typ aktu | Rozporządzenie |
| Status | obowiązujący |
| W mocy | tak |
| Data ogłoszenia | 2025-03-26 |
| Data wydania | 2025-03-28 |
| Ostatnia zmiana | 2025-03-31 |
| Źródło | [ISAP](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250000411) · [PDF](https://api.sejm.gov.pl/eli/acts/DU/2025/411/text.pdf) |

w sprawie warunków technicznych przetwarzania danych przez Krajowy System Informatyczny do spraw Systemu Wjazdu/Wyjazdu Na podstawie art. 13 ustawy z dnia 18 października 2024 r. o udziale Rzeczypospolitej Polskiej w Systemie Wjazdu/ Wyjazdu (Dz. U. poz. 1688) zarządza się, co następuje:
§ 1. Rozporządzenie określa:
1) sposób wykorzystywania Krajowego Systemu Informatycznego do spraw Systemu Wjazdu/Wyjazdu, zwanego dalej „KSI EES”, jako krajowego interfejsu Systemu Wjazdu/Wyjazdu, zwanego dalej „EES”;
2) warunki techniczne przetwarzania danych EES przez KSI EES.
§ 2. Ilekroć w rozporządzeniu jest mowa o:
1) brzegowym urządzeniu sieciowym – należy przez to rozumieć urządzenie typu firewall pełniące funkcję urządzenia dostępowego do KSI EES, terminujące tunel VPN IPsec;
2) certyfikacie – należy przez to rozumieć elektroniczne zaświadczenie, zapewniające poufność przesyłanych danych oraz bezpieczeństwo procesu uwierzytelniania użytkownika instytucjonalnego, będące elementem Infrastruktury Klucza Publicznego (PKI), czyli kryptosystemu, w którego skład wchodzą urzędy certyfikacyjne, urzędy rejestracyjne, użytkownicy certyfikatów (subskrybenci), oprogramowanie i sprzęt, wydane zgodnie z obowiązującą w Straży Granicznej Polityką Certyfikacji;
3) TLS (Transport Layer Security) – należy przez to rozumieć protokół służący do szyfrowania transmisji danych w sieci;
4) VPN (Virtual Private Network) – należy przez to rozumieć wirtualną sieć prywatną jako sieć przekazu danych korzystającą z publicznej infrastruktury telekomunikacyjnej, która dzięki stosowaniu protokołów tunelowania i procedur bezpieczeństwa zachowuje poufność danych;
5) wydzielonej sieci teleinformatycznej – należy przez to rozumieć niepubliczną sieć telekomunikacyjną, która dzięki zastosowaniu rozwiązań sprzętowych lub programowych zapewnia możliwość logicznej separacji od powszechnie dostępnej infrastruktury telekomunikacyjnej;
6) certyfikacie X.509 – należy przez to rozumieć standard opisujący sposób użycia asymetrycznych algorytmów kryptograficznych.
§ 3. KSI EES wykorzystuje się jako krajowy interfejs EES przez zapewnienie połączenia:
1) w przypadku użytkownika indywidualnego – przez aplikację WWW EES lub
2) w przypadku użytkownika końcowego – przez system teleinformatyczny użytkownika instytucjonalnego.
§ 4. Warunki techniczne przetwarzania danych EES obejmują:
1) zapewnienie bezpieczeństwa własnej sieci teleinformatycznej podłączonej do KSI EES;
2) zapewnienie połączenia z KSI EES za pośrednictwem wydzielonej sieci teleinformatycznej z wykorzystaniem protokołu https oraz VPN;
3) wykorzystanie protokołu TLS i certyfikatu X.509 w celu zabezpieczenia dostępu do KSI EES;
4) uzyskanie:
a) certyfikatu dla brzegowego urządzenia sieciowego wydawanego przez Centralny Organ Techniczny KSI EES,
b) parametrów konfiguracji brzegowego urządzenia sieciowego określanych przez Centralny Organ Techniczny KSI EES.
§ 5. Warunki techniczne przetwarzania danych EES przez użytkownika indywidualnego obejmują dodatkowo uwierzytelnienie się w KSI EES spersonalizowanym identyfikatorem użytkownika indywidualnego oraz hasłem, wydanymi zgodnie z art. 17 ust. 5 ustawy z dnia 18 października 2024 r. o udziale Rzeczypospolitej Polskiej w Systemie Wjazdu/ Wyjazdu, zwanej dalej „ustawą”.
§ 6. Warunki techniczne przetwarzania danych EES przez użytkownika instytucjonalnego obejmują dodatkowo:
1) uzyskanie certyfikatu uwierzytelniającego zgodnie z przepisami wydanymi na podstawie art. 17 ust. 18 ustawy;
2) zapewnienie uwierzytelnienia użytkownika końcowego we własnym systemie teleinformatycznym i przetwarzania przez niego danych EES na podstawie przydzielonych uprawnień;
3) zapewnienie odnotowywania przez własny system teleinformatyczny informacji obejmujących:
a) indywidualny identyfikator użytkownika końcowego,
b) datę i godzinę dokonania czynności,
c) dane, których dotyczyła czynność,
d) określenie rodzaju czynności wykonanej za pośrednictwem KSI EES,
e) w przypadku czynności polegającej na dokonaniu wpisu – niepowtarzalny identyfikator wpisu danych EES nadany przez KSI EES.
§ 7. Rozporządzenie wchodzi w życie z dniem określonym w decyzji Komisji Europejskiej, zgodnie z art. 66 ust. 1 rozporządzenia Parlamentu Europejskiego i Rady (UE) 2017/2226 z dnia 30 listopada 2017 r. ustanawiającego system wjazdu/wyjazdu (EES) w celu rejestrowania danych dotyczących wjazdu i wyjazdu obywateli państw trzecich przekraczających granice zewnętrzne państw członkowskich i danych dotyczących odmowy wjazdu w odniesieniu do takich obywateli oraz określającego warunki dostępu do EES na potrzeby ochrony porządku publicznego i zmieniającego konwencję wykonawczą do układu z Schengen i rozporządzenia (WE) nr 767/2008 i (UE) nr 1077/2011 (Dz. Urz. UE L 327 z 09.12.2017, str. 20, z późn. zm. ).
Minister Spraw Wewnętrznych i Administracji: wz. T. Szymański

