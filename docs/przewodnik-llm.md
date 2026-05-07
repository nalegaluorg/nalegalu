# Przewodnik pracy LLM z bazą nalegalu

*Dokumentacja techniczna dla modeli językowych i zaawansowanych użytkowników. Opisuje architekturę bazy, strategie wyszukiwania, system scoringu i krytyczne zasady bezpieczeństwa prawnego.*

---

## 1. Architektura bazy

### 1.1. Skala

Baza zawiera ok. 5700 aktów prawnych w pełnym tekście (markdown z frontmatter YAML) oraz powiązane orzecznictwo sądowe z systemu SAOS. Sam Kodeks cywilny ma ponad 114 000 orzeczeń w 6552 artykułach.

### 1.2. Katalogi tematyczne

Akty pogrupowane w 17 dziedzin prawa: `prawo-cywilne/`, `prawo-karne/`, `prawo-pracy/`, `prawo-administracyjne/`, `prawo-handlowe/`, `prawo-budowlane/`, `prawo-bankowe/`, `prawo-podatkowe/`, `prawo-konstytucyjne/`, `prawo-morskie/`, `prawo-ochrony-danych/`, `prawo-ochrony-srodowiska/`, `prawo-energetyczne/`, `prawo-telekomunikacyjne/`, `prawo-upadlosciowe/`, `prawo-zamowien/`, `inne/`.

### 1.3. Struktura katalogów aktu prawnego

Każdy akt ma katalog o nazwie będącej adresem ISAP (np. `WDU19640160093`):

```
prawo-cywilne/WDU19640160093/
  index.md              ← pełny tekst ustawy z frontmatter
  orzecznictwo.md       ← indeks orzeczeń (tabela + lista per artykuł)
  orzecznictwo/         ← pliki CSV per artykuł
    art-24.csv
    art-24-par-1.csv
    art-415.csv
    art-4421.csv        ← art. 442¹ (indeksy górne bez znaków specjalnych)
```

### 1.4. Frontmatter aktów

```yaml
---
title: "Ustawa z dnia 23 kwietnia 1964 r. - Kodeks cywilny."
address: WDU19640160093
eli: DU/1964/93
publisher: DU
year: 1964
pos: 93
act_type: Ustawa
status: akt posiada tekst jednolity   # ← oznacza akt obowiązujący
---
```

### 1.5. Format CSV orzeczeń

Separator: `|` (pipe). Kolumny:

```
saos_id|date|court|case_number|type|score|saos_url
206816|2015-02-12|TK|SK 70/13|Wyrok|98|https://www.saos.org.pl/judgments/206816
```

CSV jest posortowany od najwyższego score.

### 1.6. System scoringu orzeczeń

Score odzwierciedla wagę precedensową orzeczenia (0-100):

| Score | Typowy sąd | Znaczenie |
|-------|-----------|-----------|
| 98 | TK | Wyroki Trybunału Konstytucyjnego |
| 96 | SN (uchwały 7+ sędziów) | Uchwały pełnego składu SN |
| 89 | SN (uchwały) | Uchwały SN |
| 78 | SN (wyroki) | Wyroki Sądu Najwyższego |
| 69 | SN (postanowienia) | Postanowienia SN |
| 56 | SA (wyroki) | Wyroki sądów apelacyjnych |
| 40-55 | SO | Wyroki sądów okręgowych |
| <25 | SR | Sądy rejonowe — odfiltrowane z bazy |

Sądy rejonowe są odfiltrowane z publicznej bazy. Widoczne są orzeczenia sądów okręgowych i wyższych.

---

## 2. Strategie wyszukiwania

### 2.1. Od przepisu do orzecznictwa (zalecana)

To najskuteczniejsza strategia. Trzy kroki:

**Krok 1 — Zlokalizuj przepis w tekście ustawy.** Szukaj w `index.md` odpowiedniego aktu.

**Krok 2 — Sprawdź indeks orzecznictwa.** Plik `orzecznictwo.md` zawiera tabelę z liczbą orzeczeń per artykuł, podziałem na gwiazdki i listę 20 wiodących orzeczeń per artykuł.

**Krok 3 — Pobierz szczegóły z CSV.** Pliki `orzecznictwo/art-XXX.csv` zawierają pełną listę orzeczeń posortowaną od najwyższego score. Pierwsze 10-20 wierszy to najważniejsze orzeczenia.

### 2.2. Od sygnatury do kontekstu

Gdy trzeba zweryfikować konkretną sygnaturę — przeszukaj pliki CSV we wszystkich katalogach. Jedno orzeczenie może pojawiać się przy wielu artykułach różnych ustaw, co ujawnia jego szeroki kontekst prawny.

### 2.3. Od tematu do przepisu

Gdy pytanie dotyczy problemu, nie konkretnego artykułu — szukaj tematycznie w plikach `index.md` odpowiednich katalogów. Zidentyfikuj potencjalnie właściwe ustawy, potem szukaj w nich konkretnych fraz.

### 2.4. Szukanie aktów w dziedzinie

Przeglądaj katalogi tematyczne. Frontmatter każdego `index.md` zawiera tytuł i status aktu. Szukaj po słowach kluczowych w tytułach lub treści.

---

## 3. Krytyczne zasady

### 3.1. Weryfikacja sygnatur — bezwzględny wymóg

**Nigdy nie cytuj sygnatury, której nie znalazłeś w plikach bazy.** Modele językowe mają silną tendencję do generowania prawdopodobnie brzmiących, ale fikcyjnych sygnatur. Każde orzeczenie powołane w odpowiedzi musi być zweryfikowane — znalezione w pliku CSV z konkretnym score i datą.

Jeśli nie znaleziono orzecznictwa w bazie — napisz to wprost. Lepiej „w orzecznictwie SN utrwalony jest pogląd, że..." bez sygnatury niż fikcyjna sygnatura.

### 3.2. Krzyżowa weryfikacja sygnatur strony przeciwnej

Gdy pismo procesowe strony przeciwnej powołuje orzeczenia, zawsze sprawdź je w bazie. Pozwala to potwierdzić, że orzeczenie istnieje, oraz ustalić, przy jakich artykułach się pojawia — co może ujawnić kontekst odmienny od tego, w jakim je powołano.

### 3.3. Score jako priorytet cytowania

Zawsze zaczynaj od orzeczeń z najwyższym score. Wyrok TK (score 98) lub uchwała SN (score 96) ma nieporównywalnie większą wagę niż wyrok sądu okręgowego (score 40-55). Przy budowaniu argumentacji opartej wyłącznie na orzeczeniach SO, zaznacz, że linia orzecznicza nie została jeszcze potwierdzona przez SN.

### 3.4. Sprawdzanie statusu aktu

Przed cytowaniem przepisu sprawdź pole `status` we frontmatter:
- `akt posiada tekst jednolity` — akt obowiązujący
- `obowiązujący` — akt obowiązujący
- inne statusy (np. `uchylony`) mogą oznaczać akt nieaktualny — zaznacz to w odpowiedzi

### 3.5. Artykuły z indeksami górnymi

Artykuły typu 442¹, 446² w nazwach plików CSV zapisane są bez znaków specjalnych: `art-4421.csv`, `art-4462.csv`. W tekście ustawy (`index.md`) indeks górny jest zapisany jako znak Unicode (np. `Art. 442¹`).

### 3.6. Brak w bazie nie oznacza braku orzeczenia

Baza nalegalu zawiera orzeczenia z systemu SAOS, ale nie jest kompletna. Jeśli orzeczenie nie znaleziono w bazie, nie oznacza to, że nie istnieje — zaznacz źródło informacji: „wg bazy nalegalu" lub „nie znaleziono w bazie nalegalu".

---

## 4. Wzorzec pełnej analizy prawnej

Optymalny przepływ pracy przy złożonym pytaniu:

**1. Identyfikacja przepisów** — szukaj po słowach kluczowych w `index.md` odpowiednich ustaw. Przeczytaj pełną treść artykułów.

**2. Zbieranie orzecznictwa** — pobierz top 10-20 orzeczeń z CSV per artykuł. Filtruj: score 69+ dla wiodących, 40+ dla uzupełniających. Sprawdź, czy orzeczenia pojawiają się przy wielu artykułach.

**3. Weryfikacja krzyżowa** — każda sygnatura zweryfikowana w plikach bazy. Sygnatury strony przeciwnej sprawdzone i ocenione. Brak halucynacji.

**4. Budowanie argumentacji** — struktura: przepis, interpretacja, orzeczenie potwierdzające. Hierarchia źródeł: TK, uchwały SN, wyroki SN, SA, SO. Kontekst: przy jakich artykułach pojawia się dane orzeczenie.

**5. Weryfikacja końcowa** — ponowne sprawdzenie wszystkich sygnatur, spójności dat, statusu aktu.

---

## 5. Najczęstsze pułapki

| Pułapka | Skutek | Zapobieganie |
|---------|--------|-------------|
| Halucynacja sygnatury | Podanie fikcyjnego orzeczenia | Każda sygnatura musi być znaleziona w CSV |
| Cytowanie uchylonego aktu | Powołanie nieobowiązującego przepisu | Sprawdzenie pola `status` we frontmatter |
| Ignorowanie score | Powołanie wyroku SO zamiast uchwały SN | Sortowanie po score, priorytet 69+ |
| Szukanie tylko w jednym pliku | Pominięcie orzeczenia przy innym artykule | Przeszukanie wielu plików CSV |
| Brak w bazie = brak orzeczenia | Błędne założenie | Zaznacz źródło: „wg bazy nalegalu" |

---

## 6. Kluczowe akty — skrócona mapa

| Akt | Katalog | Adres ISAP |
|-----|---------|------------|
| Kodeks cywilny | `prawo-cywilne/WDU19640160093/` | WDU19640160093 |
| Kodeks postępowania cywilnego | `prawo-cywilne/WDU19640430296/` | WDU19640430296 |
| Kodeks karny | `prawo-karne/WDU19970880553/` | WDU19970880553 |
| Kodeks postępowania karnego | `prawo-karne/WDU19970890555/` | WDU19970890555 |
| Kodeks pracy | `prawo-pracy/WDU19740240141/` | WDU19740240141 |
| Kodeks spółek handlowych | `prawo-handlowe/WDU20001201252/` | WDU20001201252 |
| Kodeks postępowania administracyjnego | `prawo-administracyjne/WDU19600300168/` | WDU19600300168 |
| Ustawa o prawach pacjenta | `inne/WDU20090520417/` | WDU20090520417 |

---

*Dokument przeznaczony zarówno dla użytkowników zaawansowanych, jak i dla systemów AI pracujących z bazą nalegalu. Struktura bazy może ewoluować — w razie wątpliwości zweryfikuj aktualne ścieżki.*

*Ostatnia aktualizacja: maj 2026*
