---
title: Rozporządzenie Ministra Spraw Wewnętrznych i Administracji z dnia 11 czerwca 2026 r. w sprawie trybu oraz warunków technicznych dokonywania wpisów danych i występowania z wnioskami o porównanie danych z danymi Eurodac oraz wymogów technicznych dla systemów teleinformatycznych organów uprawnionych do dokonywania wpisów danych lub do występowania z wnioskami o porównanie danych z danymi Eurodac
address: WDU20260000765
eli: DU/2026/765
publisher: DU
year: 2026
pos: 765
act_type: Rozporządzenie
status: obowiązujący
domain: null
source: pdf
---

# RZECZYPOSPOLITEJ POLSKIEJ Poz. 765 ROZPORZĄDZENIE MINISTRA SPRAW WEWNĘTRZNYCH I ADMINISTRACJI z dnia 11 czerwca 2026 r.

| Pole | Wartość |
|---|---|
| Adres publikacyjny | Dz.U. 2026 poz. 765 |
| ISAP | WDU20260000765 |
| Typ aktu | Rozporządzenie |
| Status | obowiązujący |
| W mocy | tak |
| Data ogłoszenia | 2026-06-11 |
| Data wydania | 2026-06-12 |
| Wejście w życie | 2026-06-12 |
| Ostatnia zmiana | 2026-06-15 |
| Źródło | [ISAP](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000765) · [PDF](https://api.sejm.gov.pl/eli/acts/DU/2026/765/text.pdf) |

w sprawie trybu oraz warunków technicznych dokonywania wpisów danych i występowania z wnioskami o porównanie danych z danymi Eurodac oraz wymogów technicznych dla systemów teleinformatycznych organów uprawnionych do dokonywania wpisów danych lub do występowania z wnioskami o porównanie danych z danymi Eurodac Na podstawie art. 8 ust. 5 ustawy z dnia 15 maja 2026 r. o udziale Rzeczypospolitej Polskiej w systemie Eurodac (Dz. U. poz. 760) zarządza się, co następuje:

**§ 1.** Rozporządzenie określa:

- **1)** tryb oraz warunki techniczne dokonywania wpisów przez organy, o których mowa w art. 4 ust. 1 ustawy z dnia 15 maja 2026 r. o udziale Rzeczypospolitej Polskiej w systemie Eurodac, zwanej dalej „ustawą”;
- **2)** warunki techniczne występowania z wnioskami, o których mowa w art. 5 ustawy;
- **3)** wymogi techniczne dla systemów teleinformatycznych.

**§ 2.** Ilekroć w rozporządzeniu jest mowa o:

- **1)** brzegowym urządzeniu sieciowym – należy przez to rozumieć urządzenie typu firewall pełniące funkcję urządzenia dostępowego oraz terminujące tunel VPN IPsec;
- **2)** dostępie bezpośrednim – należy przez to rozumieć dostęp bezpośredni, o którym mowa w art. 2 pkt 6 ustawy;
- **3)** krajowym punkcie dostępu – należy przez to rozumieć system, o którym mowa w art. 2 ust. 1 lit. k rozporządzenia Parlamentu Europejskiego i Rady (UE) 2024/1358 z dnia 14 maja 2024 r. w sprawie ustanowienia systemu Eurodac do porównywania danych biometrycznych w celu skutecznego stosowania rozporządzeń Parlamentu Europejskiego i Rady (UE) 2024/1351 i (UE) 2024/1350 i dyrektywy Rady 2001/55/WE oraz w celu identyfikowania nielegalnie przebywających obywateli państw trzecich oraz bezpaństwowców, w sprawie występowania z wnioskami o porównanie z danymi Eurodac przez organy ścigania państw członkowskich i Europol na potrzeby ochrony porządku publicznego, w sprawie zmiany rozporządzeń Parlamentu Europejskiego i Rady (UE) 2018/1240 i (UE) 2019/818 oraz w sprawie uchylenia rozporządzenia Parlamentu Europejskiego i Rady (UE) nr 603/2013 (Dz. Urz. UE L 2024/1358 z 22.05.2024, z późn. zm.), zwanego dalej „rozporządzeniem 2024/1358”;
- **4)** TLS – należy przez to rozumieć protokół służący do szyfrowania transmisji danych w sieci (Transport Layer Security);
- **5)** użytkowniku indywidualnym – należy przez to rozumieć użytkownika indywidualnego, o którym mowa w art. 2 pkt 13 ustawy;
- **6)** użytkowniku instytucjonalnym – należy przez to rozumieć organ uprawniony do dostępu bezpośredniego;
- **7)** użytkowniku końcowym – należy przez to rozumieć użytkownika końcowego, o którym mowa w art. 2 pkt 14 ustawy;
- **8)** VPN – należy przez to rozumieć wirtualną sieć prywatną jako sieć przekazu danych korzystającą z publicznej infrastruktury telekomunikacyjnej, która dzięki stosowaniu protokołów tunelowania i procedur bezpieczeństwa zachowuje poufność danych (Virtual Private Network);
- **9)** wpisie – należy przez to rozumieć wpis, o którym mowa w art. 2 pkt 15 ustawy;
- **10)** WUI – należy przez to rozumieć interfejs użytkownika, o którym mowa w art. 2 pkt 16 ustawy;
- **11)** wydzielonej sieci teleinformatycznej – należy przez to rozumieć niepubliczną sieć telekomunikacyjną, która dzięki zastosowaniu rozwiązań sprzętowych lub programowych zapewnia możliwość logicznej separacji od powszechnie dostępnej infrastruktury telekomunikacyjnej.

**§ 3.** Warunkami technicznymi dokonywania wpisów danych przez organy, o których mowa w art. 4 ust. 1 ustawy, są:

- **1)** zapewnienie połączenia z krajowym punktem dostępu lub z WUI za pośrednictwem wydzielonej sieci teleinformatycznej z wykorzystaniem protokołu HTTPS oraz VPN;
- **2)** wykorzystanie protokołu TLS.

**§ 4.** Warunkami technicznymi dokonywania wpisów danych przez organy, o których mowa w art. 4 ust. 1 ustawy, przy użyciu krajowego punktu dostępu są:

- **1)** przestrzeganie wymogów określonych w opisie interfejsu, o którym mowa w § 5 ust. 1 pkt 1;
- **2)** odbieranie przez użytkowników indywidualnych i użytkowników końcowych komunikatów dotyczących wpisów oraz komunikatów dotyczących błędów;
- **3)** uwierzytelnianie użytkowników końcowych w systemie teleinformatycznym organu, o którym mowa w art. 4 ust. 1 ustawy;
- **4)** dokonywanie wpisów danych wyłącznie przez uwierzytelnionych użytkowników końcowych.

**§ 5.**

1. Organ, o którym mowa w art. 4 ust. 1 ustawy, w celu uzyskania dostępu do krajowego punktu dostępu jako użytkownik instytucjonalny:

- **1)** występuje pisemnie do Centralnego Organu Technicznego Eurodac o wydanie certyfikatu uwierzytelniającego jego system teleinformatyczny oraz o przekazanie opisu interfejsu;
- **2)** zestawia bezpieczne połączenie z krajowym punktem dostępu z wykorzystaniem certyfikatu, o którym mowa w pkt 1, we współpracy z Centralnym Organem Technicznym Eurodac;
- **3)** przygotowuje na podstawie opisu interfejsu, o którym mowa w pkt 1, własny system teleinformatyczny do współpracy z krajowym punktem dostępu;
- **4)** występuje pisemnie do Centralnego Organu Technicznego Eurodac o potwierdzenie poprawności konfiguracji połączenia własnego systemu teleinformatycznego z krajowym punktem dostępu.

2. Po spełnieniu wymagań, o których mowa w ust. 1, Centralny Organ Techniczny Eurodac nadaje organowi, o którym mowa w art. 4 ust. 1 ustawy, uprawnienie do dostępu do krajowego punktu dostępu.

**§ 6.**

1. W celu dokonania wpisu użytkownik końcowy:

- **1)** dokonuje uwierzytelnienia w systemie teleinformatycznym organu, o którym mowa w art. 4 ust. 1 ustawy;
- **2)** dokonuje wpisu zgodnie z uprawnieniami przydzielonymi przez organ, o którym mowa w art. 4 ust. 1 ustawy.

2. W celu dokonania wpisu użytkownik indywidualny:

- **1)** uzyskuje połączenie z WUI za pośrednictwem wydzielonej sieci teleinformatycznej z wykorzystaniem protokołu HTTPS oraz VPN;
- **2)** dokonuje wpisu zgodnie z zakresem uprawnień wynikających z upoważnienia do dostępu do WUI, o którym mowa w art. 19 ust. 4 ustawy.

**§ 7.** Warunkami technicznymi występowania z wnioskami, o których mowa w art. 5 ustawy, są:

- **1)** zapewnienie połączenia z aplikacją służącą do obsługi wniosków, o których mowa w art. 5 ustawy, za pośrednictwem wydzielonej sieci teleinformatycznej z wykorzystaniem protokołu HTTPS oraz VPN;
- **2)** wykorzystanie protokołu TLS;
- **3)** uzyskanie:
    - **a)** certyfikatów dla brzegowego urządzenia sieciowego wydawanych przez Centralny Organ Techniczny Eurodac,
    - **b)** parametrów konfiguracji brzegowego urządzenia sieciowego określanych przez Centralny Organ Techniczny Eurodac, które umożliwiają bezpieczne nawiązanie połączenia.

**§ 8.** Wymogami technicznymi dla systemów teleinformatycznych są:

- **1)** posiadanie ważnego certyfikatu uwierzytelniającego wydanego przez Centralny Organ Techniczny Eurodac oraz aktualnego opisu interfejsu, o którym mowa w § 5 ust. 1 pkt 1;
- **2)** zapewnienie bezpiecznego połączenia z krajowym punktem dostępu, z wykorzystaniem ważnego certyfikatu uwierzytelniającego wydanego przez Centralny Organ Techniczny Eurodac;
- **3)** zapewnienie możliwości współpracy z krajowym punktem dostępu zgodnie z opisem interfejsu, o którym mowa w § 5 ust. 1 pkt 1;
- **4)** uzyskanie od Centralnego Organu Technicznego Eurodac potwierdzenia poprawności konfiguracji połączenia z krajowym punktem dostępu.

**§ 9.** Rozporządzenie wchodzi w życie z dniem 12 czerwca 2026 r. Minister Spraw Wewnętrznych i Administracji: wz. T. Szymański

