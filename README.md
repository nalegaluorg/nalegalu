# nalegalu — polskie akty prawne i orzecznictwo

Polskie prawo w formacie Markdown — akty prawne z Dziennika Ustaw oraz powiązane orzecznictwo sądowe z bazy [SAOS](https://www.saos.org.pl/). Gotowe do użycia z narzędziami AI (Claude, ChatGPT, Obsidian, Cursor).

Więcej informacji: [nalegalu.org](https://nalegalu.org)

## Najczęściej cytowane akty prawne

Akty z największą liczbą powiązanych orzeczeń sądowych:

| Akt | Orzeczeń | Orzecznictwo |
|-----|---:|---|
| [Ustawa z dnia 17 listopada 1964 r. - Kodeks postępowania cywilnego.](prawo-cywilne/WDU19640430296/index.md) | 14 085 | [orzecznictwo.md](prawo-cywilne/WDU19640430296/orzecznictwo.md) |
| [Konstytucja Rzeczypospolitej Polskiej z dnia 2 kwietnia 1997 r.](prawo-konstytucyjne/WDU19970780483/index.md) | 6 424 | [orzecznictwo.md](prawo-konstytucyjne/WDU19970780483/orzecznictwo.md) |
| [Ustawa z dnia 23 kwietnia 1964 r. - Kodeks cywilny.](prawo-cywilne/WDU19640160093/index.md) | 6 224 | [orzecznictwo.md](prawo-cywilne/WDU19640160093/orzecznictwo.md) |
| [Ustawa z dnia 26 czerwca 1974 r. Kodeks pracy.](prawo-pracy/WDU19740240141/index.md) | 3 214 | [orzecznictwo.md](prawo-pracy/WDU19740240141/orzecznictwo.md) |
| [Ustawa z dnia 19 grudnia 2008 r. o emeryturach pomostowych](inne/WDU20082371656/index.md) | 2 124 | [orzecznictwo.md](inne/WDU20082371656/orzecznictwo.md) |
| [Ustawa z dnia 6 czerwca 1997 r. - Kodeks postępowania karnego.](prawo-karne/WDU19970890555/index.md) | 1 744 | [orzecznictwo.md](prawo-karne/WDU19970890555/orzecznictwo.md) |
| [Ustawa z dnia 6 czerwca 1997 r. - Kodeks karny.](prawo-karne/WDU19970880553/index.md) | 1 339 | [orzecznictwo.md](prawo-karne/WDU19970880553/orzecznictwo.md) |
| [Ustawa z dnia 12 maja 2011 r. o kredycie konsumenckim](inne/WDU20111260715/index.md) | 1 139 | [orzecznictwo.md](inne/WDU20111260715/orzecznictwo.md) |
| [Ustawa z dnia 16 grudnia 2010 r. o zmianie ustawy o finansach publiczn](inne/WDU20102571726/index.md) | 1 118 | [orzecznictwo.md](inne/WDU20102571726/orzecznictwo.md) |
| [Ustawa z dnia 14 czerwca 1960 r. Kodeks postępowania administracyjnego](prawo-administracyjne/WDU19600300168/index.md) | 1 115 | [orzecznictwo.md](prawo-administracyjne/WDU19600300168/orzecznictwo.md) |

## Orzecznictwo

Repozytorium zawiera kompaktowe indeksy orzecznictwa — łącznie **61 995** powiązań między orzeczeniami a aktami prawnymi.

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
| [Prawo administracyjne](prawo-administracyjne/README.md) | 69 | [Pełna lista aktów →](prawo-administracyjne/README.md) (13 z orzecznictwem) |
| [Prawo bankowe](prawo-bankowe/README.md) | 28 | [Pełna lista aktów →](prawo-bankowe/README.md) (7 z orzecznictwem) |
| [Prawo budowlane](prawo-budowlane/README.md) | 45 | [Pełna lista aktów →](prawo-budowlane/README.md) (6 z orzecznictwem) |
| [Prawo cywilne](prawo-cywilne/README.md) | 144 | [Pełna lista aktów →](prawo-cywilne/README.md) (47 z orzecznictwem) |
| [Prawo energetyczne](prawo-energetyczne/README.md) | 35 | [Pełna lista aktów →](prawo-energetyczne/README.md) (5 z orzecznictwem) |
| [Prawo handlowe](prawo-handlowe/README.md) | 26 | [Pełna lista aktów →](prawo-handlowe/README.md) (7 z orzecznictwem) |
| [Prawo karne](prawo-karne/README.md) | 160 | [Pełna lista aktów →](prawo-karne/README.md) (40 z orzecznictwem) |
| [Prawo konstytucyjne](prawo-konstytucyjne/README.md) | 2 | [Pełna lista aktów →](prawo-konstytucyjne/README.md) (1 z orzecznictwem) |
| [Prawo morskie](prawo-morskie/README.md) | 7 | [Pełna lista aktów →](prawo-morskie/README.md) (2 z orzecznictwem) |
| [Prawo ochrony środowiska](prawo-ochrony-srodowiska/README.md) | 65 | [Pełna lista aktów →](prawo-ochrony-srodowiska/README.md) (9 z orzecznictwem) |
| [Prawo podatkowe](prawo-podatkowe/README.md) | 196 | [Pełna lista aktów →](prawo-podatkowe/README.md) (29 z orzecznictwem) |
| [Prawo pracy](prawo-pracy/README.md) | 68 | [Pełna lista aktów →](prawo-pracy/README.md) (21 z orzecznictwem) |
| [Prawo telekomunikacyjne](prawo-telekomunikacyjne/README.md) | 6 | [Pełna lista aktów →](prawo-telekomunikacyjne/README.md) (2 z orzecznictwem) |
| [Prawo upadłościowe](prawo-upadlosciowe/README.md) | 19 | [Pełna lista aktów →](prawo-upadlosciowe/README.md) (4 z orzecznictwem) |
| [Prawo zamówień publicznych](prawo-zamowien/README.md) | 19 | [Pełna lista aktów →](prawo-zamowien/README.md) (7 z orzecznictwem) |
| [Inne](inne/README.md) | 18723 | [Pełna lista aktów →](inne/README.md) (1074 z orzecznictwem) |

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

**PASSED** — 0 tests — 0 passed, 0 failed, 0 errors

Ostatni przebieg: 2026-05-27 02:03 UTC. Szczegóły: [TEST_RESULTS.md](TEST_RESULTS.md).

<!-- STATS:START -->
## Statystyki

![Wzrost bazy aktów](docs/growth.svg)

| | Wartość |
|---|---:|
| Opublikowane akty | **16,649** |
| Odrzucone (jakość) | 5,958 |
| Artykuły | 131,289 |
| Znaki treści | 387.1M |
| Śr. znaków/akt | 23,250 |
| Śr. artykułów/akt | 7.9 |

**Źródła danych:**

- ELI HTML: 15,785 (95%)
- ISAP PDF: 864 (5%)

*Odrzucone: 59 skanów bez OCR, 42 zablokowanych przez bramkę jakości, 5899 inne*

*Od 2026-05-18: +3,328 aktów*

*Ostatnia aktualizacja: 2026-05-28*
<!-- STATS:END -->

## Zakres i ograniczenia

Repozytorium zawiera obowiązujące akty prawne z Dziennika Ustaw (teksty jednolite) oraz indeksy orzecznictwa sądowego z bazy SAOS. To nie jest oficjalne źródło prawa — jedynym autentycznym źródłem jest Dziennik Ustaw publikowany na isap.sejm.gov.pl.

## Licencja

Treść aktów prawnych jest wyłączona spod ochrony prawa autorskiego na mocy art. 4 ustawy o prawie autorskim i prawach pokrewnych. Struktura i metadane: [CC0 1.0 — Public Domain](LICENSE).

*19620 aktów • wygenerowano automatycznie przez [nalegalu](https://github.com/nalegaluorg/nalegalu) • źródło danych: [ISAP](https://isap.sejm.gov.pl) + [SAOS](https://www.saos.org.pl) • aktualizacja: 2026-05-28*
