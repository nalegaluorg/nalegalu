# nalegalu — polskie akty prawne i orzecznictwo

Polskie prawo w formacie Markdown — akty prawne z Dziennika Ustaw oraz powiązane orzecznictwo sądowe z bazy [SAOS](https://www.saos.org.pl/). Gotowe do użycia z narzędziami AI (Claude, ChatGPT, Obsidian, Cursor).

Więcej informacji: [nalegalu.org](https://nalegalu.org)

## Najczęściej cytowane akty prawne

Akty z największą liczbą powiązanych orzeczeń sądowych:

| Akt | Orzeczeń | Orzecznictwo |
|-----|---:|---|
| [Ustawa z dnia 17 listopada 1964 r. - Kodeks postępowania cywilnego.](prawo-cywilne/WDU19640430296/index.md) | 172 479 | [orzecznictwo.md](prawo-cywilne/WDU19640430296/orzecznictwo.md) |
| [Ustawa z dnia 23 kwietnia 1964 r. - Kodeks cywilny.](prawo-cywilne/WDU19640160093/index.md) | 115 264 | [orzecznictwo.md](prawo-cywilne/WDU19640160093/orzecznictwo.md) |
| [Ustawa z dnia 6 czerwca 1997 r. - Kodeks karny.](prawo-karne/WDU19970880553/index.md) | 43 444 | [orzecznictwo.md](prawo-karne/WDU19970880553/orzecznictwo.md) |
| [Ustawa z dnia 6 czerwca 1997 r. - Kodeks postępowania karnego.](prawo-karne/WDU19970890555/index.md) | 40 021 | [orzecznictwo.md](prawo-karne/WDU19970890555/orzecznictwo.md) |
| [Konstytucja Rzeczypospolitej Polskiej z dnia 2 kwietnia 1997 r.](prawo-konstytucyjne/WDU19970780483/index.md) | 33 539 | [orzecznictwo.md](prawo-konstytucyjne/WDU19970780483/orzecznictwo.md) |
| [Ustawa z dnia 17 grudnia 1998 r. o emeryturach i rentach z Funduszu Ub](inne/WDU19981621118/index.md) | 22 994 | [orzecznictwo.md](inne/WDU19981621118/orzecznictwo.md) |
| [Ustawa z dnia 26 czerwca 1974 r. Kodeks pracy.](prawo-pracy/WDU19740240141/index.md) | 21 746 | [orzecznictwo.md](prawo-pracy/WDU19740240141/orzecznictwo.md) |
| [Ustawa z dnia 13 października 1998 r. o systemie ubezpieczeń społeczny](inne/WDU19981370887/index.md) | 17 636 | [orzecznictwo.md](inne/WDU19981370887/orzecznictwo.md) |
| [Ustawa z dnia 28 lipca 2005 r. o kosztach sądowych w sprawach cywilnyc](inne/WDU20051671398/index.md) | 12 480 | [orzecznictwo.md](inne/WDU20051671398/orzecznictwo.md) |
| [Ustawa z dnia 14 czerwca 1960 r. Kodeks postępowania administracyjnego](prawo-administracyjne/WDU19600300168/index.md) | 9 164 | [orzecznictwo.md](prawo-administracyjne/WDU19600300168/orzecznictwo.md) |

## Orzecznictwo

Repozytorium zawiera kompaktowe indeksy orzecznictwa — łącznie **654 745** powiązań między orzeczeniami a aktami prawnymi.

Każdy akt prawny, na który powołują się orzeczenia, posiada plik `orzecznictwo.md` z listą cytujących orzeczeń pogrupowanych wg artykułu. Dla największych aktów (np. Kodeks cywilny) orzecznictwo jest podzielone na osobne pliki per artykuł.

Każde orzeczenie zawiera link do pełnego tekstu w serwisie [SAOS](https://www.saos.org.pl/).

## Jak korzystać

Najprostszy sposób: otwórz repozytorium w **Claude Cowork**, **Obsidian** lub **Cursor** — narzędzia te pozwalają AI przeszukiwać i analizować wszystkie pliki jednocześnie. Bez ręcznego kopiowania i wklejania.

**Przykład:** Wskaż folder nalegalu w Claude Cowork i zapytaj:

```
Jakie przesłanki odpowiedzialności deliktowej wynikają z art. 415 k.c.
w świetle najnowszego orzecznictwa SN? Podaj sygnatury z bazy.
```

Claude sam otworzy Kodeks cywilny, znajdzie art. 415, sprawdzi orzecznictwo i przygotuje analizę z konkretnymi sygnaturami.

## Aktualizacja danych

Dane aktualizują się automatycznie. Najnowszą wersję można pobrać jako [ZIP z zakładki Releases](https://github.com/nalegaluorg/nalegalu-public/releases).

## Dokumentacja

| Przewodnik | Opis |
|------------|------|
| [Jak korzystać z nalegalu](docs/jak-korzystac-z-nalegalu.md) | Kompletny przewodnik — od przeglądania na GitHubie do pracy z AI |
| [Konfiguracja Claude Cowork](docs/konfiguracja-claude-cowork.md) | Krok po kroku: instalacja, ustawienie projektu, instrukcje dla AI |
| [Biblioteka promptów](docs/prompty.md) | Gotowe prompty do analizy przepisów, orzecznictwa, pism procesowych |
| [Przewodnik pracy LLM](docs/przewodnik-llm.md) | Architektura bazy, system scoringu, strategie wyszukiwania |

## Dziedziny prawa

| Dziedzina | Aktów | Opis |
|-----------|------:|------|
| [Ochrona danych osobowych](prawo-ochrony-danych/README.md) | 8 | [Pełna lista aktów →](prawo-ochrony-danych/README.md) (2 z orzecznictwem) |
| [Prawo administracyjne](prawo-administracyjne/README.md) | 68 | [Pełna lista aktów →](prawo-administracyjne/README.md) (16 z orzecznictwem) |
| [Prawo bankowe](prawo-bankowe/README.md) | 28 | [Pełna lista aktów →](prawo-bankowe/README.md) (8 z orzecznictwem) |
| [Prawo budowlane](prawo-budowlane/README.md) | 44 | [Pełna lista aktów →](prawo-budowlane/README.md) (7 z orzecznictwem) |
| [Prawo cywilne](prawo-cywilne/README.md) | 138 | [Pełna lista aktów →](prawo-cywilne/README.md) (61 z orzecznictwem) |
| [Prawo energetyczne](prawo-energetyczne/README.md) | 34 | [Pełna lista aktów →](prawo-energetyczne/README.md) (7 z orzecznictwem) |
| [Prawo handlowe](prawo-handlowe/README.md) | 25 | [Pełna lista aktów →](prawo-handlowe/README.md) (8 z orzecznictwem) |
| [Prawo karne](prawo-karne/README.md) | 159 | [Pełna lista aktów →](prawo-karne/README.md) (55 z orzecznictwem) |
| [Prawo konstytucyjne](prawo-konstytucyjne/README.md) | 2 | [Pełna lista aktów →](prawo-konstytucyjne/README.md) (1 z orzecznictwem) |
| [Prawo morskie](prawo-morskie/README.md) | 7 | [Pełna lista aktów →](prawo-morskie/README.md) (2 z orzecznictwem) |
| [Prawo ochrony środowiska](prawo-ochrony-srodowiska/README.md) | 65 | [Pełna lista aktów →](prawo-ochrony-srodowiska/README.md) (9 z orzecznictwem) |
| [Prawo podatkowe](prawo-podatkowe/README.md) | 193 | [Pełna lista aktów →](prawo-podatkowe/README.md) (34 z orzecznictwem) |
| [Prawo pracy](prawo-pracy/README.md) | 67 | [Pełna lista aktów →](prawo-pracy/README.md) (28 z orzecznictwem) |
| [Prawo telekomunikacyjne](prawo-telekomunikacyjne/README.md) | 6 | [Pełna lista aktów →](prawo-telekomunikacyjne/README.md) (2 z orzecznictwem) |
| [Prawo upadłościowe](prawo-upadlosciowe/README.md) | 18 | [Pełna lista aktów →](prawo-upadlosciowe/README.md) (6 z orzecznictwem) |
| [Prawo zamówień publicznych](prawo-zamowien/README.md) | 19 | [Pełna lista aktów →](prawo-zamowien/README.md) (7 z orzecznictwem) |
| [Inne](inne/README.md) | 18350 | [Pełna lista aktów →](inne/README.md) (1278 z orzecznictwem) |

## Bramka jakości

Każdy akt przed publikacją przechodzi automatyczną kontrolę jakości. Dokumenty z wykrytymi problemami są blokowane do czasu naprawy.

| Kontrola | Opis | Próg |
|----------|------|------|
| CID font | Uszkodzone glify — plik PDF używa wewnętrznych identyfikatorów znaków zamiast tekstu | dowolne wystąpienie `(cid:N)` |
| Null bytes | Bajty zerowe w pliku wyjściowym | dowolne wystąpienie |
| Pusty dokument | Treść zbyt krótka po ekstrakcji | < 50 znaków |
| PostScript CE | Pozostałości kodowania PostScript CE — zniekształcone polskie znaki diakrytyczne | 1 wzorzec |
| Mojibake | UTF-8 odczytane jako Latin-1 — ciągi typu `Ä\u0085`, `Ã³` | 3+ wystąpienia |
| Brak diakrytyków | Tekst prawny bez polskich znaków diakrytycznych (ą, ę, ś, ć...) | < 0.5% liter to diakrytyki (dla tekstów > 500 znaków) |
| Rozstrzelony tekst | Litery rozdzielone spacjami (artefakt OCR, np. `A r t 77`) | dowolna linia z > 30% jednoliterowych słów |
| Śmieci tabelaryczne | Linie z dużą ilością znaków pipe i slash — wynik ekstrakcji grafik i tabel z PDF | 3+ linie z > 25% tych znaków |
| Nagłówek PDF | Nagłówek `©Kancelaria Sejmu` przedostał się do treści | dowolne wystąpienie |
| Znacznik daty | Stopka z datą (np. `05/21/99`) na osobnej linii | dowolne wystąpienie |
| Powtórzenia | Ta sama linia (> 20 znaków) powtarza się wielokrotnie — prawdopodobnie nagłówek/stopka PDF | > 20 powtórzeń |

## Testy

**PASSED** — 203 tests — 203 passed, 0 failed, 0 errors, 33 skipped

Ostatni przebieg: 2026-06-14 08:22 UTC. Szczegóły: [TEST_RESULTS.md](TEST_RESULTS.md).

<!-- STATS:START -->
## Statystyki

![Wzrost bazy aktów](docs/growth.svg)

| | Wartość |
|---|---:|
| Opublikowane akty | **18,095** |
| Odrzucone (jakość) | 443 |
| Artykuły | 121,890 |
| Znaki treści | 458.6M |
| Śr. znaków/akt | 25,344 |
| Śr. artykułów/akt | 6.7 |

**Źródła danych:**

- PDF: 16,779 (93%)
- PDF: 1,112 (6%)
- ELI HTML: 204 (1%)

*Odrzucone: 1 skanów bez OCR, 818 zablokowanych przez bramkę jakości, 442 inne*

*Od 2026-05-18: +4,774 aktów*

*Ostatnia aktualizacja: 2026-06-14*
<!-- STATS:END -->

## Zakres i ograniczenia

Repozytorium zawiera obowiązujące akty prawne z Dziennika Ustaw (teksty jednolite) oraz indeksy orzecznictwa sądowego z bazy SAOS. To nie jest oficjalne źródło prawa — jedynym autentycznym źródłem jest Dziennik Ustaw publikowany na isap.sejm.gov.pl.

## Licencja

Treść aktów prawnych jest wyłączona spod ochrony prawa autorskiego na mocy art. 4 ustawy o prawie autorskim i prawach pokrewnych. Struktura i metadane: [CC0 1.0 — Public Domain](LICENSE).

*19231 aktów • wygenerowano automatycznie przez [nalegalu](https://github.com/nalegaluorg/nalegalu) • źródło danych: [ISAP](https://isap.sejm.gov.pl) + [SAOS](https://www.saos.org.pl) • aktualizacja: 2026-06-14*
