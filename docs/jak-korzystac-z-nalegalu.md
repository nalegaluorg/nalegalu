# Jak korzystać z nalegalu — przewodnik dla prawników i studentów prawa

*nalegalu.org — polskie prawo w formacie przyjaznym dla AI*

---

## Czym jest nalegalu?

nalegalu to otwarta baza polskiego prawa w formacie Markdown — ustrukturyzowanym tekście, który doskonale rozumieją zarówno ludzie, jak i narzędzia sztucznej inteligencji. Zawiera akty prawne z Dziennika Ustaw oraz orzeczenia sądowe z systemu SAOS, połączone wzajemnymi odnośnikami.

W tradycyjnych bazach prawnych (LEX, Legalis, ISAP) teksty aktów są zamknięte w skomplikowanych interfejsach webowych. Skopiowanie artykułu do ChatGPT czy Claude'a wymaga ręcznego formatowania, a wynik często traci strukturę — numery artykułów, ustępów i punktów mieszają się.

nalegalu rozwiązuje ten problem: każdy akt prawny ma czystą, czytelną strukturę z prawidłową hierarchią artykułów, a każde orzeczenie zawiera metadane, skład sędziowski i odniesienia do konkretnych przepisów. Wszystko jest ze sobą powiązane.

## Co znajdziesz w nalegalu?

### Akty prawne

Pełne teksty aktów prawnych z Dziennika Ustaw, w tym:

- Kodeksy (cywilny, karny, postępowania cywilnego, postępowania karnego, pracy, spółek handlowych i inne)
- Ustawy szczegółowe
- Rozporządzenia

Każdy akt jest zapisany w Markdown z zachowaniem pełnej struktury: części, księgi, tytuły, działy, rozdziały, artykuły z ustępami i punktami.

### Orzecznictwo

Orzeczenia sądowe z systemu SAOS (System Analizy Orzeczeń Sądowych), obejmujące:

- Sąd Najwyższy
- Trybunał Konstytucyjny
- Naczelny Sąd Administracyjny
- Sądy powszechne
- Krajową Izbę Odwoławczą

Każde orzeczenie zawiera sygnaturę akt, datę, skład sędziowski, słowa kluczowe oraz listę powoływanych przepisów z linkami do odpowiednich aktów prawnych.

### Powiązania między aktami a orzecznictwem

To jest kluczowa wartość nalegalu. Dla każdego aktu prawnego generowany jest plik `orzecznictwo.md`, który grupuje powołujące się na niego orzeczenia według konkretnych artykułów. Chcesz wiedzieć, jak sądy interpretują art. 415 Kodeksu cywilnego? Otwierasz `orzecznictwo.md` tego kodeksu i widzisz tabelę wszystkich orzeczeń z podziałem na artykuły.

---

## Jak zacząć?

Są trzy sposoby korzystania z nalegalu — od najprostszego do najbardziej zaawansowanego. Wybierz ten, który pasuje do Twojego poziomu komfortu z technologią.

### Sposób 1: Przeglądanie na GitHub (bez instalacji)

Najprościej — otwórz repozytorium nalegalu na GitHubie w przeglądarce. GitHub automatycznie renderuje pliki Markdown, więc widzisz ładnie sformatowany tekst z klikalnymi linkami.

**Krok po kroku:**

1. Wejdź na [github.com/nalegalu](https://github.com/nalegalu) (lub link z nalegalu.org)
2. Przejdź do interesującego Cię aktu prawnego (np. `prawo-cywilne/WDU19640160093/`)
3. Otwórz plik `index.md` — to pełny tekst aktu
4. Otwórz `orzecznictwo.md` — to lista orzeczeń powołujących się na ten akt
5. Skopiuj interesujący fragment (np. art. 415 + kilka orzeczeń z tabeli)
6. Wklej do ChatGPT, Claude'a lub Gemini z pytaniem

**Przykładowy prompt:**

```
Oto treść art. 415 Kodeksu cywilnego oraz fragmenty orzeczeń Sądu Najwyższego,
które go dotyczą:

[wklej skopiowany tekst]

Pytanie: Jakie przesłanki odpowiedzialności deliktowej wynikają z art. 415 k.c.
w świetle orzecznictwa SN? Podaj konkretne przykłady z wklejonych orzeczeń.
```

### Sposób 2: Obsidian — lokalna baza wiedzy (zalecane)

Obsidian to darmowa aplikacja do pracy z plikami Markdown. Działa offline, na każdym systemie (Windows, Mac, Linux), i świetnie radzi sobie z dużymi kolekcjami powiązanych dokumentów.

**Dlaczego Obsidian?**

- **Nawigacja po linkach** — klikasz odnośnik do orzeczenia i od razu je widzisz
- **Widok grafu** — wizualna mapa powiązań między aktami a orzeczeniami
- **Wyszukiwanie** — szukaj hasła we wszystkich aktach i orzeczeniach jednocześnie
- **Działa offline** — raz pobrane, nie potrzebuje internetu

**Krok po kroku:**

1. Pobierz Obsidian z [obsidian.md](https://obsidian.md/) (darmowy do użytku osobistego)
2. Pobierz repozytorium nalegalu (przycisk „Code → Download ZIP" na GitHubie, lub `git clone` jeśli znasz git)
3. Rozpakuj archiwum
4. W Obsidian: „Otwórz folder jako vault" → wskaż rozpakowany folder
5. Gotowe — przeglądaj, szukaj, klikaj w linki

**Jak korzystać z AI w Obsidian:**

Obsidian ma wtyczki społecznościowe, które dodają czat z AI bezpośrednio w aplikacji:

- **Obsidian Copilot** — zaznacz fragment tekstu, zadaj pytanie, AI odpowiada w kontekście Twojego vaulta
- **Smart Connections** — AI przeszukuje cały vault i znajduje powiązane dokumenty

Instalacja wtyczki: Ustawienia → Wtyczki społecznościowe → Przeglądaj → szukaj „Copilot" → Zainstaluj → Włącz.

Dzięki temu nie musisz ręcznie kopiować tekstu — zaznaczasz artykuł, klikasz i pytasz.

### Sposób 3: Claude Desktop, Cursor, VS Code — praca z AI na plikach lokalnych

Te narzędzia pozwalają wskazać AI cały folder nalegalu na dysku i rozmawiać z nim w kontekście wszystkich aktów i orzeczeń jednocześnie. AI „widzi" pliki i może je przeszukiwać, porównywać i analizować bez ręcznego kopiowania.

#### Claude Desktop (Cowork) — zalecane

Aplikacja desktopowa Claude od Anthropic ma tryb Cowork, który pozwala wskazać folder na dysku i pracować z jego zawartością bezpośrednio w czacie. To najwygodniejszy sposób pracy z nalegalu dla większości użytkowników.

**Co wyróżnia Claude Cowork:**

- Może czytać i przeszukiwać pliki bez limitu okna kontekstowego — sam decyduje, które pliki otworzyć
- Potrafi tworzyć nowe dokumenty na podstawie analizy (np. podsumowanie orzecznictwa do danego artykułu)
- Może uruchamiać skrypty — np. przefiltrować orzeczenia po dacie lub typie sądu
- Działa na Mac i Windows

Szczegółowa instrukcja konfiguracji (krok po kroku, z instrukcjami projektu i rozwiązywaniem problemów): **[Konfiguracja Claude Cowork](konfiguracja-claude-cowork.md)**

Gotowe prompty do pracy z nalegalu: **[Biblioteka promptów](prompty.md)**

**Przykład użycia:**

```
Przeanalizuj orzecznictwo do art. 415 Kodeksu cywilnego.
Jakie przesłanki odpowiedzialności deliktowej wynikają z orzeczeń SN
z ostatnich 5 lat? Sporządź zestawienie z sygnaturami.
```

Claude sam otworzy odpowiednie pliki, przeczyta orzeczenia i przygotuje analizę.

#### Cursor / VS Code

Cursor i VS Code to edytory kodu z wbudowanym AI, które potrafią analizować cały projekt (folder z plikami).

**Krok po kroku:**

1. Pobierz Cursor z [cursor.com](https://cursor.com/) (darmowy plan wystarczy)
2. File → Open Folder → wskaż folder nalegalu
3. Otwórz czat (Ctrl+L) i zadaj pytanie — AI ma dostęp do wszystkich plików

**Przykład użycia:**

```
Jakie orzeczenia SN z ostatnich 5 lat dotyczą art. 58 Kodeksu cywilnego?
Streść główne tezy.
```

Cursor przeszuka pliki orzecznictwa i odpowie na podstawie faktycznych danych, a nie z pamięci.

---

## Praktyczne zastosowania

### Dla studentów prawa

**Przygotowanie do egzaminu:**
Skopiuj treść artykułów z danego tematu + powiązane orzeczenia i poproś AI o wyjaśnienie w przystępny sposób, porównanie stanowisk doktryny, albo wygenerowanie pytań egzaminacyjnych.

**Pisanie pracy semestralnej / magisterskiej:**
Użyj nalegalu jako źródła aktualnych orzeczeń dotyczących badanego zagadnienia. Tabele w `orzecznictwo.md` dają Ci gotowy przegląd orzecznictwa — z sygnaturami, datami i typami orzeczeń.

**Nauka przepisów:**
Poproś AI o wytłumaczenie skomplikowanego artykułu „jak dla studenta pierwszego roku" albo o porównanie dwóch instytucji prawnych na podstawie faktycznych przepisów.

**Przykładowe prompty:**

```
Na podstawie poniższych przepisów Kodeksu cywilnego wyjaśnij różnicę między
odpowiedzialnością kontraktową (art. 471) a deliktową (art. 415).
Podaj przykłady stanów faktycznych dla każdej z nich.

[wklej art. 415 i art. 471 z nalegalu]
```

```
Oto lista orzeczeń SN dotyczących art. 58 k.c. z pliku orzecznictwo.md.
Jakie główne trendy orzecznicze można zaobserwować w ostatnich 10 latach?

[wklej tabelę z orzecznictwo.md]
```

### Dla praktykujących prawników

**Badanie orzecznictwa do sprawy:**
Zamiast ręcznego przeszukiwania LEX-a, otwórz `orzecznictwo.md` dla konkretnego przepisu i natychmiast zobacz, które orzeczenia go dotyczą. Użyj AI do streszczenia linii orzeczniczej.

**Przygotowanie pisma procesowego:**
Skopiuj relevantne przepisy + orzeczenia i poproś AI o pomoc w sformułowaniu argumentacji prawnej. AI oparty na faktycznych tekstach nie będzie wymyślał nieistniejących artykułów.

**Analiza zmian w orzecznictwie:**
Sortowanie orzeczeń po datach w `orzecznictwo.md` pozwala śledzić, jak zmieniała się interpretacja danego przepisu na przestrzeni lat.

**Przykładowy prompt:**

```
Reprezentuję powoda w sprawie o odszkodowanie z art. 415 k.c.
Na podstawie poniższych orzeczeń SN pomóż mi zidentyfikować argumenty
przemawiające za szeroką interpretacją „winy" w kontekście odpowiedzialności
deliktowej. Podaj sygnatury orzeczeń, na które mogę się powołać.

[wklej przepis + wybrane orzeczenia]
```

---

## Dlaczego AI + nalegalu działa lepiej niż samo AI?

Modele językowe (ChatGPT, Claude, Gemini) znają polskie prawo — ale z pamięci. To oznacza, że:

- Mogą pomylić numery artykułów
- Mogą „wymyślić" nieistniejące przepisy (tzw. halucynacje)
- Nie znają najnowszych zmian w prawie
- Nie mają dostępu do treści orzeczeń

Kiedy wklejasz tekst z nalegalu jako kontekst, AI pracuje na **faktycznych, aktualnych przepisach**. Nie musi zgadywać — ma przed sobą dokładną treść artykułu i może ją analizować, porównywać, wyjaśniać. To jak różnica między pytaniem kogoś „co pamiętasz o tym artykule?" a daniem mu otwartego kodeksu.

---

## Dobre praktyki

1. **Zawsze weryfikuj odpowiedzi AI.** Narzędzia AI to asystenci, nie wyrocznia. Traktuj odpowiedzi jako punkt wyjścia do dalszej analizy.

2. **Podawaj kontekst.** Im więcej relevantnych przepisów i orzeczeń wkleisz, tym lepsza będzie odpowiedź. Ale nie przesadzaj — skup się na temacie.

3. **Pytaj o sygnatury.** Gdy AI powołuje się na orzeczenie, poproś o sygnaturę i zweryfikuj ją w nalegalu lub na saos.org.pl.

4. **Korzystaj ze struktury.** nalegalu grupuje orzeczenia po artykułach — nie musisz przeszukiwać wszystkiego. Zacznij od konkretnego przepisu.

5. **Aktualizuj bazę.** nalegalu jest regularnie synchronizowane ze źródłami. Pobierz nową wersję repozytorium co jakiś czas (`git pull` lub ponowne pobranie ZIP).

---

## FAQ

**Czy nalegalu jest darmowe?**
Tak. Projekt jest otwarty i dostępny dla wszystkich.

**Czy mogę zaufać, że teksty są aktualne?**
Teksty są pobierane bezpośrednio z oficjalnych źródeł — Dziennika Ustaw (ISAP) i systemu SAOS. Data ostatniej synchronizacji jest widoczna w repozytorium. Zawsze warto zweryfikować z oficjalnym publikatorem.

**Czy potrzebuję płatnego konta w ChatGPT/Claude?**
Darmowe wersje wystarczą do podstawowego użycia. Płatne konta mają wyższe limity wiadomości i dostęp do nowszych modeli, co przydaje się przy dłuższych analizach.

**Czy nalegalu zastąpi LEX/Legalis?**
Nie — nalegalu to inne narzędzie z innym celem. LEX i Legalis oferują komentarze, glosy, piśmiennictwo i zaawansowane wyszukiwanie. nalegalu dostarcza surowe teksty prawne w formacie optymalnym do pracy z AI. Narzędzia te się uzupełniają.

**Jak mogę pomóc?**
Projekt jest open source. Możesz zgłaszać błędy, proponować ulepszenia, lub po prostu korzystać i dzielić się z innymi.

---

---

## Dokumentacja techniczna

Dla zaawansowanych użytkowników i osób konfigurujących systemy AI do pracy z nalegalu:

- **[Konfiguracja Claude Cowork](konfiguracja-claude-cowork.md)** — krok po kroku od pobrania aplikacji do pierwszego pytania
- **[Biblioteka promptów](prompty.md)** — gotowe prompty podzielone na kategorie
- **[Przewodnik pracy LLM z bazą](przewodnik-llm.md)** — architektura bazy, system scoringu, strategie wyszukiwania, krytyczne zasady

---

*Ostatnia aktualizacja: maj 2026*
*nalegalu.org — polskie prawo, otwarcie i przystępnie*
