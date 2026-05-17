---
title: Rozporządzenie Rady Ministrów z dnia 15 października 2012 r. w sprawie państwowego systemu odniesień przestrzennych
address: WDU20120001247
eli: DU/2012/1247
publisher: DU
year: 2012
pos: 1247
act_type: Rozporządzenie
status: akt posiada tekst jednolity
domain: null
source: "isap-pdf"
---

# RZECZYPOSPOLITEJ POLSKIEJ Warszawa, dnia 14 listopada 2012 r.

| Pole | Wartość |
|---|---|
| Adres publikacyjny | Dz.U. 2012 poz. 1247 |
| ISAP | WDU20120001247 |
| Typ aktu | Rozporządzenie |
| Status | akt posiada tekst jednolity |
| W mocy | tak |
| Data ogłoszenia | 2012-10-15 |
| Data wydania | 2012-11-14 |
| Ostatnia zmiana | 2025-01-27 |
| Źródło | [ISAP](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20120001247) · [PDF](https://api.sejm.gov.pl/eli/acts/DU/2012/1247/text.pdf) |

Załąc nik nr 1 i uk a ów wspó rzędnych Tabela 1. Parametry techniczne geodezyjnego układu odniesienia PL-ETRF2000 Tabela 2. Parametry techniczne geodezyjnego układu odniesienia PL-ETRF89 Tabela 3. Parametry techniczne układu współrzędnych geocentrycznych kartezjańskich XYZ Tabela 4. Parametry techniczne układu współrzędnych geocentrycznych geodezyjnych GRS80h Tabela 5. Parametry techniczne układu współrzędnych geodezyjnych GRS80H Tabela 6. Parametry techniczne układu wysokościowego PL-EVRF2007-NH - Tabela 7. Parametry techniczne układu wysokościowego PL-KRON86-NH - Tabela 8. Parametry techniczne układu współrzędnych płaskich prostokątnych PL-LAEA Tabela 9. Parametry techniczne układu współrzędnych płaskich prostokątnych PL-LCC Tabela 10. Parametry techniczne układu współrzędnych płaskich prostokątnych PL-1992 Tabela 11. Parametry techniczne układu współrzędnych płaskich prostokątnych PL-UTM × × Tabela 12. Parametry techniczne układu współrzędnych płaskich prostokątnych PL-2000 × × Tabela nr 1 Klasa: SOP Elipsoida Nazwa: elipsoida Definicja: Elipsoida obrotowa, wykorzystywana w geodezji jako najlepsze przybliżenie figury Ziemi (powierzchni geoidy). Jej osią obrotu jest oś krótsza.
Stereotypy: «FeatureType» Atrybut: Nazwa: nazwa Nazwa (pełna): nazwa Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa elipsoidy. Ciąg znaków tworzący unikalny identyfikator w ramach bazy danych.
Atrybut: Nazwa: duzaPolos Nazwa (pełna): duża półoś Dziedzina: Distance Liczność: 1 Definicja: Połowa dłuższej osi elipsoidy wyrażonej w metrach.
Atrybut: Nazwa: odwrotnoscSplaszczenia Nazwa (pełna): odwrotność spłaszczenia Dziedzina: Real Liczność: 1 Definicja: Parametr określający odstępstwo kształtu elipsoidy od kształtu sfery. Wyraża je stosunek dużej półosi do różnicy dużej półosi i krótkiej półosi 1/f = a/(a-b).
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa dotycząca elipsoidy.
Relacja: Typ: Aggregation Rola: Dziedzina: SOP_UkladGeodezyjny Liczność: 1..* Definicja: Układ geodezyjny, w którego skład wchodzi elipsoida.
Klasa: SOP Elipsoida Relacja: Typ: Association Rola: geoida2 Dziedzina: SOP_Geoida Liczność: 0..* Definicja: Określa powiązanie modelu quasi-geoidy z elipsoidą, na której została oparta.
Tabela nr 2 Klasa: SOP Geoida Nazwa: model quasi-geoidy Definicja: Dyskretny model będący aproksymacją quasi-geoidy, wyrażony w postaci regularnej siatki, dla której punktów węzłowych zostały określone odległości (odstępy) powierzchni quasi-geoidy od powierzchni elipsoidy odniesienia.
Stereotypy: «FeatureType» Atrybut: Nazwa: nazwa Nazwa (pełna): nazwa Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa geoidy. Ciąg znaków tworzący unikalny identyfikator w ramach bazy danych.
Atrybut: Nazwa: innaNazwa Nazwa (pełna): inna nazwa Dziedzina: CharacterString Liczność: 0..* Definicja: Alternatywna nazwa, przez którą jest określany model quasigeoidy.
Atrybut: Nazwa: epokaRealizacji Nazwa (pełna): epoka realizacji Dziedzina: Date Liczność: 1 Definicja: Określenie daty, na którą zostały wyznaczone parametry geoidy.
Atrybut: Nazwa: rozdzielczoscPol Nazwa (pełna): rozdzielczość wzdłuż południka Dziedzina: Angle Liczność: 1 Definicja: Odległość pomiędzy punktami węzłowymi mierzona wzdłuż południka. Jednostką zapisu jest minuta.
Klasa: SOP Geoida Atrybut: Nazwa: rozdzielczoscRown Nazwa (pełna): rozdzielczość wzdłuż równoleżnika Dziedzina: Angle Liczność: 1 Definicja: Odległość pomiędzy punktami węzłowymi mierzona wzdłuż równoleżnika. Jednostką zapisu jest minuta.
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa dotycząca quasi-geoidy.
Relacja: Typ: Aggregation Rola: Dziedzina: SOP_UkladWysokosciowy Liczność: 1 Definicja: Układ wysokościowy, w którego skład wchodzi geoida.
Relacja: Typ: Association Rola: elipsoida2 Dziedzina: SOP_Elipsoida Liczność: 1 Definicja: Określa elipsoidę, na której został obliczony model quasigeoidy.
Tabela nr 3 Klasa: SOP Odwzorowanie Nazwa: odwzorowanie kartograficzne Definicja: Definicja i zbiór parametrów przedstawiający relację między elipsoidą a płaszczyzną odwzorowania.
Stereotypy: «FeatureType» Atrybut: Nazwa: identyfikator Nazwa (pełna): identyfikator odwzorowania Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa odwzorowania kartograficznego. Ciąg znaków tworzący unikalny identyfikator w ramach bazy danych.
Atrybut: Nazwa: innaNazwa Nazwa (pełna): inna nazwa odwzorowania Dziedzina: CharacterString Liczność: 0..* Definicja: Alternatywna nazwa, przez którą jest określane odwzorowanie.
Klasa: SOP Odwzorowanie Atrybut: Nazwa: typOdwz Nazwa (pełna): typ odwzorowania Dziedzina: CharacterString Liczność: 1 Definicja: Określenie typu odwzorowania.
Atrybut: Nazwa: parametr Nazwa (pełna): parametr odwzorowania Dziedzina: SOP_ParametrOdwzor Liczność: 4..8 Definicja: Parametr odwzorowania.
Atrybut: Nazwa: formulyObliczeniowe Nazwa (pełna): formuły obliczeniowe Dziedzina: CharacterString Liczność: 0..* Definicja: Informacja na temat literatury, w której zostały opisane formuły odwzorowawcze danego odwzorowania.
Atrybut: Nazwa: zastosowanie Nazwa (pełna): zastosowanie Dziedzina: CharacterString Liczność: 0..1 Definicja: Rodzaj prac oraz dziedziny gospodarki, w których może być zastosowane odwzorowanie.
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa dotycząca odwzorowania.
Relacja: Typ: Association Rola: siatkaKarto Dziedzina: SOP_SiatkaKarto Liczność: 1 Definicja: Określa siatkę kartograficzną dla konkretnego odwzorowania kartograficznego.
Relacja: Typ: Association Rola: uklWspGeod Dziedzina: SOP_UklWspGeod Liczność: 2 Definicja: Określa układ współrzędnych geodezyjnych, w którym jest realizowane odwzorowanie. Jeden z układów współrzędnych geodezyjnych jest układem wyjściowym, a drugi układem odwzorowanym.
Tabela nr 4 Klasa: SOP OsUkladu Nazwa: oś układu Definicja: Opis poszczególnych osi dla występujących układów współrzędnych.
Stereotypy: «FeatureType» Atrybut: Nazwa: nazwa Nazwa (pełna): nazwa Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa osi.
Atrybut: Nazwa: oznaczenie Nazwa (pełna): oznaczenie Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęte oznaczenie dla nazwy osi.
Atrybut: Nazwa: jednostkaMiary Nazwa (pełna): jednostka miary Dziedzina: SOP_Jednostka Liczność: 1 Definicja: Jednostka miary wybrana dla osi. W zależności od układu współrzędnych są to metry lub stopnie.
Atrybut: Nazwa: zwrot Nazwa (pełna): zwrot osi Dziedzina: SOP_ZwrotOsi Liczność: 1 Definicja: Kierunek zmian jednostki osi uznany za dodatni.
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa na temat wybranej osi współrzędnych.
Relacja: Typ: Aggregation Rola: Dziedzina: SOP_UkladWsp Liczność: 1..* Definicja: Układ współrzędnych, w którego skład wchodzi oś układu.
Tabela nr 5 Klasa: SOP PojSystOdn Nazwa: pojedynczy system odniesienia Definicja: Definicja systemu odniesienia.
Klasa bazowa: SOP_SystOdn Stereotypy: «FeatureType» Klasa: SOP PojSystOdn Atrybut: Nazwa: identyfikator Nazwa (pełna): identyfikator Dziedzina: SOP_IdSystOdn Liczność: 1 Definicja: Identyfikator systemu odniesienia. Ciąg znaków tworzący unikalny identyfikator w ramach bazy danych.
Atrybut: Nazwa: typ Nazwa (pełna): typ systemu odniesienia Dziedzina: SOP_TypSystOdn Liczność: 1 Definicja: Informacja na temat typu systemu odniesienia określająca, czy dany układ jest układem geodezyjnym, odwzorowanym czy wysokościowym.
Atrybut: Nazwa: zastosowanie Nazwa (pełna): zastosowanie Dziedzina: CharacterString Liczność: 0..1 Definicja: Asortyment prac oraz dziedzin gospodarki, w których może być stosowany zdefiniowany system odniesienia.
Relacja: Typ: Aggregation Rola: ukladOdn Dziedzina: SOP_UkladOdn Liczność: 1 Definicja: Układ odniesienia wchodzący w skład pojedynczego systemu odniesienia.
Relacja: Typ: Aggregation Rola: ukladWsp Dziedzina: SOP_UkladWsp Liczność: 1 Definicja: Układ współrzędnych wchodzący w skład pojedynczego systemu odniesienia.
Relacja: Typ: Generalization Dziedzina: SOP SystOdn Relacja: Typ: Aggregation Rola: Dziedzina: SOP_ZlozSystOdn Liczność: 0..* Definicja: Złożony system odniesienia, w którego skład wchodzą pojedyncze systemy odniesienia.
Tabela nr 6 Klasa: SOP PolPocz Nazwa: południk początkowy Definicja: Południk, względem którego oblicza się długości geodezyjne innych południków.
Stereotypy: «FeatureType» Atrybut: Nazwa: nazwa Nazwa (pełna): nazwa Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa południka początkowego. Ciąg znaków tworzący unikalny identyfikator w ramach bazy danych.
Atrybut: Nazwa: wartosc Nazwa (pełna): wartość Dziedzina: Angle Liczność: 1 Definicja: Wartość długości geodezyjnej określana w stopniach, wyrażana względem południka Greenwich.
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa dotycząca południka początkowego.
Relacja: Typ: Aggregation Rola: Dziedzina: SOP_UkladGeodezyjny Liczność: 1..* Definicja: Układ geodezyjny, w którego skład wchodzi południk początkowy.
Tabela nr 7 Klasa: SOP SiatkaKarto Nazwa: siatka kartograficzna Definicja: Opis siatki kartograficznej.
Stereotypy: «FeatureType» Atrybut: Nazwa: naroznik Nazwa (pełna): narożnik Dziedzina: DirectPosition Liczność: 1 Definicja: Współrzędne dolnego lewego narożnika siatki kartograficznej.
Klasa: SOP SiatkaKarto Atrybut: Nazwa: jednostka Nazwa (pełna): jednostka rozdzielczości Dziedzina: SOP_Jednostka Liczność: 1 Definicja: Określenie jednostek, w których jest wyrażona rozdzielczość siatki kartograficznej.
Atrybut: Nazwa: rozdzielczoscN Nazwa (pełna): rozdzielczość północna Dziedzina: Angle Liczność: 1 Definicja: Rozdzielczość siatki kartograficznej określona dla składowej północnej. Jednostką zapisu jest stopień, minuta lub sekunda łuku.
Atrybut: Nazwa: rozdzielczoscE Nazwa (pełna): rozdzielczość wschodnia Dziedzina: Angle Liczność: 1 Definicja: Rozdzielczość siatki kartograficznej określona dla składowej wschodniej. Jednostką zapisu jest stopień, minuta lub sekunda łuku.
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa dotycząca siatki kartograficznej.
Relacja: Typ: Association Rola: odwzorowanie2 Dziedzina: SOP_Odwzorowanie Liczność: 1 Definicja: Określa odwzorowanie kartograficzne według siatki kartograficznej.
Tabela nr 8 Klasa: SOP_SystOdn Abstract Nazwa: system odniesienia Definicja: Zbiór informacji pozwalający na wyrażenie położenia obiektu w świecie rzeczywistym za pomocą układu współrzędnych zrealizowanym w konkretnym układzie odniesienia.
Stereotypy: «FeatureType» Klasa: SOP SystOdn Abstract Atrybut: Nazwa: idIIP Nazwa (pełna): identyfikator IIP Dziedzina: BT_Identyfikator Liczność: 1 Definicja: Identyfikator obiektu infrastruktury informacji przestrzennej.
Atrybut: Nazwa: innaNazwa Nazwa (pełna): inna nazwa Dziedzina: CharacterString Liczność: 0..* Definicja: Alternatywna nazwa, przez którą jest określany system odniesienia.
Relacja: Typ: Generalization Dziedzina: SOP PojSystOdn Relacja: Typ: Generalization Dziedzina: SOP ZlozSystOdn Tabela nr 9 Klasa: SOP UklWspGeod Nazwa: układ współrzędnych geodezyjnych Definicja: Szczególny typ układu współrzędnych zawierający dwie lub trzy osie określające położenie obiektu.
Klasa bazowa: SOP_UkladWsp Stereotypy: «FeatureType» Relacja: Typ: Generalization Dziedzina: SOP UkladWsp Relacja: Typ: Association Rola: odwzorowanie1 Dziedzina: SOP_Odwzorowanie Liczność: 1 Definicja: Określa odwzorowanie dla układu współrzędnych geodezyjnych.
Ograniczenie: tylkoDlaOdwzorowania Relacja jest realizowana tylko dla obiektu układ współrzędnych geodezyjnych, przy założeniu, że parametr typ odwzorowania został określony jako „odwzorowany”.
inv: if SOP_PojSystOdn.typ='odwzorowany' then self--> notEmpty() else self--> isEmpty() endif Tabela nr 10 Klasa: SOP UklWspPion Nazwa: układ pionowy Definicja: Szczególny typ układu współrzędnych zawierający tylko jedną oś związaną z pionem.
Klasa bazowa: SOP_UkladWsp Stereotypy: «FeatureType» Relacja: Typ: Generalization Dziedzina: SOP UkladWsp Tabela nr 11 Klasa: SOP UkladGeodezyjny Nazwa: geodezyjny układ odniesienia Definicja: Układ odniesienia opisujący związek dwu- lub trójwymiarowego układu współrzędnych z Ziemią.
Klasa bazowa: SOP_UkladOdn Stereotypy: «FeatureType» Atrybut: Nazwa: punktPrzylozenia Nazwa (pełna): punkt przyłożenia Dziedzina: CharacterString Liczność: 1 Definicja: Definicja fizycznych punktów na powierzchni Ziemi, dla których została określona relacja z elipsoidą.
Relacja: Typ: Generalization Dziedzina: SOP UkladOdn Relacja: Typ: Aggregation Rola: elipsoida1 Dziedzina: SOP_Elipsoida Liczność: 1 Definicja: Elipsoida wchodząca w skład układu geodezyjnego.
Relacja: Typ: Aggregation Rola: polPocz Dziedzina: SOP_PolPocz Liczność: 1 Definicja: Południk początkowy wchodzący w skład układu geodezyjnego.
Tabela nr 12 Klasa: SOP UkladOdn Nazwa: układ odniesienia Definicja: Zbiór parametrów definiujący położenie początku układu, skalę i orientację układu współrzędnych.
Stereotypy: «FeatureType» Klasa: SOP UkladOdn Atrybut: Nazwa: identyfikator Nazwa (pełna): identyfikator Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa układu odniesienia. Ciąg znaków tworzący unikalny identyfikator w ramach bazy danych.
Atrybut: Nazwa: nazwaPelna Nazwa (pełna): nazwa pełna Dziedzina: CharacterString Liczność: 1 Definicja: Pełna nazwa układu odniesienia.
Atrybut: Nazwa: innaNazwa Nazwa (pełna): inna nazwa Dziedzina: CharacterString Liczność: 0..* Definicja: Alternatywna nazwa, przez którą jest określany układ odniesienia.
Atrybut: Nazwa: epokaRealizacji Nazwa (pełna): epoka realizacji Dziedzina: Date Liczność: 1 Definicja: Określenie daty, na którą zostały wyznaczone parametry układu odniesienia.
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa dotycząca układu odniesienia.
Relacja: Typ: Generalization Dziedzina: SOP_UkladGeodezyjny Relacja: Typ: Generalization Dziedzina: SOP_UkladWysokosciowy Relacja: Typ: Aggregation Rola: Dziedzina: SOP_PojSystOdn Liczność: 1..* Definicja: Pojedynczy system odniesienia, w którego skład wchodzi układ odniesienia.
Tabela nr 13 Klasa: SOP UkladWsp Nazwa: układ współrzędnych Definicja: Zbiór reguł matematycznych określających, w jaki sposób punktom są przypisywane współrzędne.
Stereotypy: «FeatureType» Atrybut: Nazwa: identyfikator Nazwa (pełna): identyfikator Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa układu współrzędnych. Ciąg znaków tworzący unikalny identyfikator w ramach bazy danych.
Atrybut: Nazwa: innaNazwa Nazwa (pełna): inna nazwa Dziedzina: CharacterString Liczność: 1 Definicja: Alternatywna nazwa, przez którą jest określany układ współrzędnych.
Atrybut: Nazwa: typUkladu Nazwa (pełna): typ układu współrzędnych Dziedzina: SOP_TypUkladuWsp Liczność: 1 Definicja: Informacja na temat typu układu współrzędnych określająca, czy dany układ jest układem kartezjańskim, elipsoidalnym czy pionowym. Wybranie odpowiedniego typu definiuje relacje pomiędzy osiami układu współrzędnych.
Atrybut: Nazwa: zastosowanie Nazwa (pełna): zastosowanie Dziedzina: CharacterString Liczność: 0..1 Definicja: Asortyment prac oraz dziedzin gospodarki, w których może być zastosowany układ współrzędnych.
Atrybut: Nazwa: liczbaOsi Nazwa (pełna): liczba osi Dziedzina: Integer Liczność: 1 Definicja: Wymiar układu współrzędnych definiowany przez liczbę osi układu.
Relacja: Typ: Aggregation Rola: Dziedzina: SOP_PojSystOdn Liczność: 1..* Definicja: Pojedynczy system odniesienia, w którego skład wchodzi układ współrzędnych.
Klasa: SOP UkladWsp Relacja: Typ: Generalization Dziedzina: SOP UklWspGeod Relacja: Typ: Generalization Dziedzina: SOP UklWspPion Relacja: Typ: Aggregation Rola: osUkladu Dziedzina: SOP_OsUkladu Liczność: 1..3 Definicja: Oś układu wchodząca w skład układu współrzędnych.
Tabela nr 14 Klasa: SOP_UkladWysokosciowy Nazwa: układ wysokościowy Definicja: Układ odniesienia opisujący związek pomiędzy wysokością fizyczną (zależną od pola grawitacyjnego) a Ziemią.
Klasa bazowa: SOP_UkladOdn Stereotypy: «FeatureType» Atrybut: Nazwa: poziomOdniesienia Nazwa (pełna): poziom odniesienia Dziedzina: CharacterString Liczność: 1 Definicja: Nazwa punktu lub punktów na powierzchni Ziemi, dla których została określona relacja z polem ciężkości Ziemi (geoidą).
Relacja: Typ: Generalization Dziedzina: SOP UkladOdn Relacja: Typ: Aggregation Rola: geoida1 Dziedzina: SOP_Geoida Liczność: 0..1 Definicja: Geoida wchodząca w skład układu wysokościowego.
Tabela nr 15 Klasa: SOP ZlozSystOdn Nazwa: złożony system odniesienia Definicja: System odniesienia wykorzystujący do opisu położenia dwa niezależne systemy odniesienia.
Klasa bazowa: SOP_SystOdn Stereotypy: «FeatureType» Klasa: SOP ZlozSystOdn Atrybut: Nazwa: identyfikator Nazwa (pełna): identyfikator systemu złożonego Dziedzina: CharacterString Liczność: 1 Definicja: Identyfikator składa się z dwóch identyfikatorów systemu pojedynczego, oddzielonych znakiem "/" (ukośnik).
Relacja: Typ: Generalization Dziedzina: SOP SystOdn Relacja: Typ: Aggregation Rola: pojSystOdn Dziedzina: SOP_PojSystOdn Liczność: 2 Definicja: Pojedynczy system odniesienia wchodzący w skład złożonego systemu odniesienia.
Ograniczenie: systemZlozony Dopuszcza się jedynie relacje, wówczas gdy pierwszy system jest systemem geodezyjnym lub odwzorowanym, a drugi jest systemem wysokościowym.
Tabela nr 16 Klasa: SOP IdSystOdn Nazwa: identyfikator systemu odniesienia Definicja: Słownik identyfikatorów systemów odniesienia.
Stereotypy: «enumeration» Atrybut: Nazwa: PL-ETRF89-GRS80H Nazwa (pełna): PL-ETRF89-GRS80H Definicja: Atrybut: Nazwa: PL-ETRF2000-GRS80H Nazwa (pełna): PL-ETRF2000-GRS80H Definicja: Atrybut: Nazwa: PL-ETRF2000-GRS80h Nazwa (pełna): PL-ETRF2000-GRS80h Definicja: Atrybut: Nazwa: PL-ETRF2000-XYZ Nazwa (pełna): PL-ETRF2000-XYZ Definicja: Atrybut: Nazwa: PL-EVRF2007-NH Nazwa (pełna): PL-EVRF2007-NH Definicja: Klasa: SOP IdSystOdn Atrybut: Nazwa: PL-KRON86-NH Nazwa (pełna): PL-KRON86-NH Definicja: Atrybut: Nazwa: PL-ETRF89-LAEA Nazwa (pełna): PL-ETRF89-LAEA Definicja: Atrybut: Nazwa: PL-ETRF89-LCC Nazwa (pełna): PL-ETRF89-LCC Definicja: Atrybut: Nazwa: PL-ETRF89-UTM Nazwa (pełna): PL-ETRF89-UTM Definicja: Atrybut: Nazwa: PL-ETRF89-1992 Nazwa (pełna): PL-ETRF89-1992 Definicja: Atrybut: Nazwa: PL-ETRF89-2000 Nazwa (pełna): PL-ETRF89-2000 Definicja: Atrybut: Nazwa: PL-ETRF2000-LAEA Nazwa (pełna): PL-ETRF2000-LAEA Definicja: Atrybut: Nazwa: PL-ETRF2000-LCC Nazwa (pełna): PL-ETRF2000-LCC Definicja: Atrybut: Nazwa: PL-ETRF2000-UTM Nazwa (pełna): PL-ETRF2000-UTM Definicja: Atrybut: Nazwa: PL-ETRF2000-1992 Nazwa (pełna): PL-ETRF2000-1992 Definicja: Atrybut: Nazwa: PL-ETRF2000-2000 Nazwa (pełna): PL-ETRF2000-2000 Definicja: Tabela nr 17 Klasa: SOP Jednostka Nazwa: jednostka miary Definicja: Słownik jednostek miar.
Stereotypy: «enumeration» Atrybut: Nazwa: metry Nazwa (pełna): metry Definicja: Miara zgodna z SI.
Atrybut: Nazwa: stopnie Nazwa (pełna): stopnie Definicja: Miara zgodna z SI.
Tabela nr 18 Klasa: SOP ParametrOdwzor Nazwa: parametr odwzorowania Definicja: Wykaz parametrów odwzorowania.
Stereotypy: «DataType» Atrybut: Nazwa: nazwaParametru Nazwa (pełna): nazwa parametru Dziedzina: CharacterString Liczność: 1 Definicja: Przyjęta nazwa dla parametru odwzorowania.
Atrybut: Nazwa: wartoscParametru Nazwa (pełna): wartość parametru Dziedzina: CharacterString Liczność: 1 Definicja: Wartość parametru.
Atrybut: Nazwa: informDodatkowa Nazwa (pełna): informacja dodatkowa Dziedzina: CharacterString Liczność: 0..1 Definicja: Informacja dodatkowa dotycząca parametru odwzorowania.
Tabela nr 19 Klasa: SOP_TypSystOdn Nazwa: typ systemu odniesienia Definicja: Słownik typów systemów odniesienia.
Stereotypy: «enumeration» Atrybut: Nazwa: geodezyjny Nazwa (pełna): geodezyjny Definicja: System odniesienia opisujący związek dwu- lub trójwymiarowego układu współrzędnych z Ziemią.
Klasa: SOP TypSystOdn Atrybut: Nazwa: wysokosciowy Nazwa (pełna): wysokościowy Definicja: System odniesienia opisujący związki pomiędzy wysokością fizyczną a Ziemią.
Atrybut: Nazwa: odwzorowany Nazwa (pełna): odwzorowany Definicja: System odniesienia powstały z dwuwymiarowego geodezyjnego systemu odniesienia przez zastosowanie odwzorowania.
Tabela nr 20 Klasa: SOP TypUkladuWsp Nazwa: typ układu współrzędnych Definicja: Słownik typów układów współrzędnych.
Stereotypy: «enumeration» Atrybut: Nazwa: kartezjanski Nazwa (pełna): kartezjański Definicja: Układ współrzędnych, który podaje pozycję punktów względem dwóch lub trzech wzajemnie prostopadłych osi.
Wszystkie osie powinny mieć te same jednostki miary.
Atrybut: Nazwa: elipsoidalny Nazwa (pełna): elipsoidalny Definicja: Układ współrzędnych, w którym położenie jest określone przez szerokość geodezyjną, długość geodezyjną oraz (w przypadku układu trójwymiarowego) wysokość elipsoidalną.
Atrybut: Nazwa: pionowy Nazwa (pełna): pionowy Definicja: Jednowymiarowy układ współrzędnych używany do wyrażenia wysokości punktu w zależności od pola grawitacyjnego Ziemi.
Tabela nr 21 Klasa: SOP ZwrotOsi Nazwa: kierunek osi Definicja: Słownik zwrotów osi.
Stereotypy: «enumeration» Atrybut: Nazwa: polnoc Nazwa (pełna): północ Definicja: Klasa: SOP ZwrotOsi Atrybut: Nazwa: poludnie Nazwa (pełna): południe Definicja: Atrybut: Nazwa: wschod Nazwa (pełna): wschód Definicja: Atrybut: Nazwa: zachod Nazwa (pełna): zachód Definicja: Atrybut: Nazwa: gora Nazwa (pełna): w górę Definicja: Zwrot osi przeciwny do zwrotu siły ciężkości.
Atrybut: Nazwa: geocentrycznyX Nazwa (pełna): geocentryczny X Definicja: Oś jest zwrócona od środka elipsoidy do punktu przecięcia równika z południkiem Greenwich.
Atrybut: Nazwa: geocentrycznyY Nazwa (pełna): geocentryczny Y Definicja: Oś jest zwrócona od środka elipsoidy do punktu przecięcia równika z południkiem 90°.
Atrybut: Nazwa: geocentrycznyZ Nazwa (pełna): geocentryczny Z Definicja: Oś jest zwrócona od środka elipsoidy do północnego bieguna geograficznego.
Tabela nr 22 Klasa: BT_Identyfikator Nazwa: identyfikator IIP Definicja: Typ reprezentujący unikalny identyfikator obiektu nadawany przez dostawcę zbioru danych. Identyfikator ten może zostać wykorzystany przez zewnętrzne systemy/aplikacje, aby zbudować referencję do obiektu.
Stereotypy: «DataType» Atrybut: Nazwa: lokalnyId Nazwa (pełna): identyfikator lokalny Dziedzina: CharacterString Liczność: 1 Definicja: Lokalny identyfikator obiektu przestrzennego nadawany przez dostawcę zbioru danych. Identyfikator musi być unikalny w zakresie przestrzeni nazw, tzn. że żaden obiekt nie może mieć takiego samego identyfikatora. Unikalność Klasa: BT Identyfikator identyfikatora w przestrzeni nazw gwarantuje dostawca zbioru danych.
Atrybut: Nazwa: przestrzenNazw Nazwa (pełna): przestrzeń nazw Dziedzina: CharacterString Liczność: 1 Definicja: Nazwa przestrzeni nazw identyfikującej zbiór danych, z którego pochodzi obiekt przestrzenny.
Atrybut: Nazwa: wersjaId Nazwa (pełna): identyfikator wersji Dziedzina: CharacterString Liczność: 0..1 Definicja: Identyfikator poszczególnej wersji obiektu przestrzennego.
Jeżeli specyfikacja obiektu zawiera informacje o cyklu życia obiektu, identyfikator wersji jest używany do rozróżnienia poszczególnych wersji obiektu. W zestawie wszystkich wersji danego obiektu identyfikator wersji musi być unikalny.
Ograniczenie: Nazwa: dozwolone znaki dla atrybutów lokalnyId i przestrzenNazw Język naturalny: Atrybuty lokalnyId i przestrzenNazw mogą być zdefiniowane tylko przy użyciu następującego zestawu znaków: {„A” …„Z”, „a”…„z”, „0”…„9”, „_”, „.”, „-“}. Dozwolone są tylko litery alfabetu łacińskiego, cyfry, podkreślenie, kropka i myślnik.
OCL: inv: let allowedChar : Set {'A'..'Z', 'a'..'z', '0'..'9', '_', '.', '-'} in (przestrzenNazw.element->forAll( char | allowedChar>exists(char)) and lokalnyId.element->forAll( char | allowedChar->exists( char ) )) Tabela. Rozdzielczość siatki kilometrowej w zależności od skali mapy Skala mapy Odstępy linii siatki 1:1 000 000 co 100 000 000 (dopuszczalne co 10 000 m) 1:500 000, 1:250 000 co 10 000 m 1:100 000 co 1000 m (dopuszczalne co 10 000 m) 1:50 000, 1:25 000 co 1000 m 1:10 000, 1:5000 co 1000 m (dopuszczalne co 100 m) 1:2000, 1:1000, 1:500 co 100 m Tabela 1. Podział i oznaczenie godeł arkuszy map w układach współrzędnych PL-LCC i PL-1992, PL-UTM (na przykładzie arkusza mapy w skali 1:1 000 000 o godle M-34) Skala mapy Arkusz pojedynczy Arkusz podwójny obszar [º,’] oznaczenie godła obszar [º,́’́́́ ] oznaczenie godła szerokość długość mapy szerokość długość mapy 1:1 000 000 4° 6° M-34 4° 12° M-34,35 1:500 000 2° 3° M-34-D 2° 6° M-34-C,D 1:250 000 1° 1,5° M-34-D-d 1° 3° M-34-D-c,d 1:100 000 20’ 30’ M-34-144 20’ 1° M-34-143,144 1:50 000 10’ 15’ M-34-144-D 10’ 30’ M-34-144-C,D 1:25 000 5’ 7,5’ M-34-144-D-d 5’ 15’ M-34-144-D-c,d 1:10 000 2,5’ 3,75’ M-34-144-D-d-4 2,5’ 7,5’ M-34-144-D-d-3,4 Tabela 2. Podział i oznaczenia arkuszy map w układzie współrzędnych PL-2000 (na przykładzie arkusza mapy w skali 1:10 000 o godle 6.115.27) Skala mapy Obszar [km] Oznaczenie godła mapy szerokość długość 1:10 000 5,0 8,0 6.115.27 1:5 000 2,5 4,0 6.115.27.4 1:2 000 1,0 1,6 6.115.27.25 1:1 000 0,5 0,8 6.115.27.25.4 1:500 0,25 0,4 6.115.27.25.4.4

