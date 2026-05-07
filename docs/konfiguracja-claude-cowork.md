# Konfiguracja Claude Cowork do pracy z nalegalu

*Przewodnik krok po kroku — od pobrania aplikacji do pierwszego pytania prawnego.*

---

## Co to jest Claude Cowork?

Claude Cowork to tryb w aplikacji desktopowej Claude (od firmy Anthropic), który pozwala wskazać folder z plikami na Twoim komputerze. Claude „widzi" te pliki i może je czytać, przeszukiwać, porównywać i analizować — bez ręcznego kopiowania i wklejania.

Dla prawnika oznacza to: wskazujesz folder nalegalu, zadajesz pytanie, a Claude sam otwiera odpowiednie akty prawne i orzecznictwo, szuka przepisów, porównuje linie orzecznicze i przygotowuje analizę.

---

## Wymagania

- Komputer z systemem macOS lub Windows
- Konto na [claude.ai](https://claude.ai) (darmowe konto wystarczy na początek; plan Pro daje więcej wiadomości dziennie)
- Około 1 GB wolnego miejsca na dysku (na pliki nalegalu)

---

## Krok 1: Pobierz pliki nalegalu

Musisz mieć kopię bazy nalegalu na swoim komputerze.

**Opcja A — Pobierz ZIP (prostsze):**

1. Wejdź na stronę repozytorium nalegalu na GitHubie
2. Kliknij zielony przycisk **Code** → **Download ZIP**
3. Rozpakuj archiwum do wybranego folderu, np. `Dokumenty/nalegalu`

**Opcja B — Git clone (jeśli masz zainstalowanego gita):**

```
git clone https://github.com/depodefi/nalegalu-public.git ~/Documents/nalegalu
```

Zaletą gita jest łatwa aktualizacja — wystarczy `git pull` zamiast ponownego pobierania ZIP-a.

---

## Krok 2: Zainstaluj Claude Desktop

1. Wejdź na [claude.ai/download](https://claude.ai/download)
2. Pobierz wersję na swój system (macOS lub Windows)
3. Zainstaluj i otwórz aplikację
4. Zaloguj się swoim kontem claude.ai

---

## Krok 3: Utwórz projekt i wskaż folder nalegalu

1. W Claude Desktop kliknij **Cowork** (ikona w lewym panelu)
2. Kliknij **Nowy projekt** (lub „New project")
3. Nadaj nazwę, np. „Prawo — nalegalu"
4. Kliknij **Wybierz folder** i wskaż folder, do którego rozpakowałeś nalegalu (np. `Dokumenty/nalegalu`)
5. Claude wyświetli potwierdzenie, że ma dostęp do plików

---

## Krok 4: Ustaw instrukcje projektu

Instrukcje projektu to stały kontekst, który Claude otrzymuje na początku każdej rozmowy. Dzięki nim nie musisz za każdym razem tłumaczyć, czym są te pliki.

1. W ustawieniach projektu znajdź pole **Instrukcje** (lub „Project instructions")
2. Wklej poniższy tekst:

```
To jest baza polskiego prawa nalegalu.

STRUKTURA PLIKÓW:
- Katalogi tematyczne (prawo-cywilne/, prawo-karne/, prawo-pracy/ itd.) zawierają podkatalogi poszczególnych aktów prawnych.
- Każdy akt ma katalog o nazwie będącej adresem ISAP (np. WDU19640160093 = Kodeks cywilny).
- index.md — pełny tekst aktu w markdown z frontmatter YAML (tytuł, status, ELI).
- orzecznictwo.md — indeks orzeczeń sądowych powiązanych z tym aktem, pogrupowanych wg artykułów.
- orzecznictwo/*.csv — szczegółowe listy orzeczeń per artykuł (format: saos_id|date|court|case_number|type|score|saos_url).

SYSTEM SCORINGU ORZECZEŃ:
Każde orzeczenie ma score odzwierciedlający wagę precedensową:
- ★★★ (score 75+): wyroki TK, uchwały SN — najwyższa waga
- ★★ (score 50-74): wyroki SN, postanowienia SN
- ★ (score 25-49): orzeczenia pomocnicze
Przy cytowaniu priorytetem są orzeczenia z najwyższym score.

ZASADY PRACY:
1. Każdą sygnaturę orzeczenia, którą podajesz w odpowiedzi, MUSISZ wcześniej znaleźć w plikach bazy. Nigdy nie wymyślaj sygnatur — halucynacje prawne są najgroźniejszym błędem.
2. Przed cytowaniem przepisu sprawdź pole "status" we frontmatter — jeśli nie jest "akt posiada tekst jednolity" lub "obowiązujący", zaznacz to w odpowiedzi.
3. Szukaj orzecznictwa najpierw w orzecznictwo.md (przegląd), potem w plikach CSV (szczegóły).
4. Artykuły z indeksami górnymi (np. art. 442¹) w nazwach plików CSV zapisane są bez znaków specjalnych: art-4421.csv.
```

3. Zapisz instrukcje

---

## Krok 5: Pierwszy test

Otwórz nową rozmowę w projekcie i wpisz:

```
Znajdź treść art. 415 Kodeksu cywilnego i pokaż 5 najważniejszych orzeczeń SN, 
które go dotyczą. Podaj sygnatury i daty.
```

Claude powinien:
1. Otworzyć `prawo-cywilne/WDU19640160093/index.md` i znaleźć art. 415
2. Sprawdzić `prawo-cywilne/WDU19640160093/orzecznictwo/art-415.csv`
3. Wybrać orzeczenia z najwyższym score
4. Podać treść artykułu + sygnatury z datami

Jeśli Claude odpowiada prawidłowo — konfiguracja działa.

---

## Rozwiązywanie problemów

**Claude nie widzi plików / mówi, że nie ma dostępu:**
Upewnij się, że folder jest wskazany w ustawieniach projektu Cowork. Sprawdź, czy folder zawiera podkatalogi z plikami `.md`.

**Claude odpowiada z pamięci zamiast z plików:**
Dodaj w pytaniu: „Odpowiedz na podstawie plików w bazie, nie z pamięci. Podaj ścieżki do plików, z których korzystasz."

**Claude wymyśla sygnatury:**
To najczęstszy problem. Dodaj w pytaniu: „Podawaj TYLKO sygnatury, które faktycznie znalazłeś w plikach CSV. Jeśli nie znalazłeś orzecznictwa, napisz to wprost."

**Odpowiedzi są zbyt ogólne:**
Zadawaj konkretne pytania z numerami artykułów. Zamiast „co mówi prawo o odszkodowaniu?" napisz „jakie przesłanki odpowiedzialności wynikają z art. 415 k.c. w świetle orzeczeń SN z CSV?"

---

## Konfiguracja dla innych narzędzi

Ten przewodnik dotyczy Claude Cowork. Instrukcje dla innych narzędzi (Obsidian, Cursor, ChatGPT) znajdziesz w osobnych dokumentach — będą dodawane na bieżąco.

---

*Ostatnia aktualizacja: maj 2026*
