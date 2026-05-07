# Biblioteka promptów nalegalu

*Gotowe prompty do pracy z bazą nalegalu w Claude Cowork i innych narzędziach AI. Każdy prompt zakłada, że AI ma dostęp do plików nalegalu.*

---

## Jak korzystać z tej biblioteki

1. Otwórz rozmowę w Claude Cowork z podpiętym folderem nalegalu
2. Skopiuj wybrany prompt i wklej do czatu
3. Zastąp fragmenty w `[nawiasach kwadratowych]` swoimi danymi
4. Po otrzymaniu odpowiedzi — zweryfikuj sygnatury orzeczeń

**Ważne:** Prompty są punktem wyjścia. Modyfikuj je pod swoje potrzeby. Jeśli odpowiedź jest zbyt ogólna, dopytaj o konkrety.

---

## 1. Analiza przepisu

### 1.1. Treść artykułu + wiodące orzecznictwo

```
Znajdź treść [art. 415 Kodeksu cywilnego] i pokaż 10 najważniejszych orzeczeń
z pliku CSV. Podaj: sygnaturę, datę, typ sądu i score.
Zacznij od orzeczeń z najwyższym score (TK, uchwały SN).
```

*Co dostaniesz:* Treść artykułu + tabelę orzeczeń posortowaną od najważniejszych. Pozwala szybko zorientować się, jak przepis jest interpretowany.

### 1.2. Wyjaśnienie przepisu prostym językiem

```
Przeczytaj [art. 58 Kodeksu cywilnego] z pliku index.md.
Wyjaśnij go prostym językiem, jak dla studenta pierwszego roku prawa.
Podaj 2-3 praktyczne przykłady zastosowania.
```

*Co dostaniesz:* Przystępne wyjaśnienie z przykładami. Przydatne przy nauce lub tłumaczeniu klientowi.

### 1.3. Porównanie dwóch instytucji prawnych

```
Na podstawie plików nalegalu porównaj:
- odpowiedzialność kontraktową (art. 471 k.c.)
- odpowiedzialność deliktową (art. 415 k.c.)

Dla każdej podaj: treść przepisu, przesłanki, różnice w ciężarze dowodu,
oraz 3 najważniejsze orzeczenia SN z CSV (z sygnaturami).
```

*Co dostaniesz:* Tabelę porównawczą z konkretnymi przepisami i orzeczeniami. Solidna baza do pisma lub opracowania.

---

## 2. Badanie orzecznictwa

### 2.1. Linia orzecznicza do artykułu

```
Przeanalizuj orzecznictwo do [art. 24 Kodeksu cywilnego].
1. Sprawdź orzecznictwo.md — ile jest orzeczeń, jakich sądów.
2. Pobierz top 20 z CSV (najwyższy score).
3. Pogrupuj chronologicznie i wskaż, jak zmieniała się interpretacja
   tego przepisu na przestrzeni lat.
```

*Co dostaniesz:* Chronologiczny przegląd orzecznictwa z trendami. Pokazuje ewolucję wykładni.

### 2.2. Weryfikacja sygnatury

```
Sprawdź, czy orzeczenie o sygnaturze [II CSK 111/08] istnieje w bazie nalegalu.
Przeszukaj pliki CSV we wszystkich katalogach.
Jeśli znajdziesz — podaj przy jakich artykułach i ustawach się pojawia,
jaki ma score i datę.
Jeśli nie znajdziesz — napisz wprost, że go nie ma w bazie.
```

*Co dostaniesz:* Potwierdzenie istnienia orzeczenia lub informację o jego braku. Kluczowe przy weryfikacji pism procesowych.

### 2.3. Orzecznictwo SN do tematu

```
Znajdź orzeczenia Sądu Najwyższego dotyczące [zadośćuczynienia za naruszenie
dóbr osobistych w internecie].
1. Sprawdź orzecznictwo do art. 23, 24, 448 Kodeksu cywilnego.
2. Wybierz TYLKO orzeczenia SN (score 69+) z plików CSV.
3. Podaj sygnatury, daty i przy jakim artykule się pojawiają.
```

*Co dostaniesz:* Listę orzeczeń SN z konkretnymi sygnaturami z bazy. Bez halucynacji.

---

## 3. Przygotowanie pism i dokumentów

### 3.1. Argumentacja prawna

```
Reprezentuję [powoda/pozwanego] w sprawie o [opis sprawy].
Kluczowe przepisy to [art. X, Y, Z ustawy].

Na podstawie plików nalegalu:
1. Przytocz treść tych przepisów.
2. Znajdź orzeczenia SN wspierające moją argumentację (score 69+).
3. Zaproponuj strukturę argumentacji z powołaniem na konkretne przepisy
   i orzeczenia (podaj sygnatury z bazy).
```

*Co dostaniesz:* Szkic argumentacji opartej na faktycznych przepisach i zweryfikowanych orzeczeniach.

### 3.2. Analiza pisma strony przeciwnej

```
Oto treść pisma od strony przeciwnej:

[wklej treść pisma]

Na podstawie plików nalegalu:
1. Zidentyfikuj przepisy i sygnatury powołane w piśmie.
2. Sprawdź każdą sygnaturę w plikach CSV — czy istnieje, jaki ma score,
   przy jakich artykułach się pojawia.
3. Oceń siłę argumentów strony przeciwnej.
4. Zaproponuj kontrargumenty z powołaniem na orzeczenia SN o wyższym score.
```

*Co dostaniesz:* Weryfikację powołanych orzeczeń + propozycję kontrargumentów. Szczególnie wartościowe, gdy strona przeciwna cytuje orzeczenia niższych sądów.

### 3.3. Procedura krok po kroku

```
Na podstawie przepisów w bazie nalegalu opisz krok po kroku procedurę
[np. dochodzenia odszkodowania za błąd medyczny / zakładania spółki z o.o. /
odwołania od decyzji administracyjnej].

Dla każdego kroku podaj:
- konkretny przepis (artykuł i ustawa)
- terminy (jeśli są określone w przepisach)
- wymagane dokumenty
```

*Co dostaniesz:* Checklistę proceduralną z konkretnymi podstawami prawnymi. Przydatne jako punkt wyjścia dla klienta lub jako notatka robocza.

---

## 4. Nauka i egzaminy

### 4.1. Pytania egzaminowe

```
Na podstawie [Rozdziału X Kodeksu cywilnego / art. 1-50 KPC / działu o umowach]
z plików nalegalu wygeneruj 10 pytań egzaminacyjnych.
Dla każdego pytania:
- podaj prawidłową odpowiedź z powołaniem na konkretny artykuł
- wskaż 1 orzeczenie SN, które potwierdza tę interpretację
```

*Co dostaniesz:* Zestaw pytań z odpowiedziami opartymi na faktycznych przepisach i orzeczeniach.

### 4.2. Notatka do egzaminu

```
Przeczytaj [art. 1-20 Kodeksu postępowania karnego] z index.md.
Przygotuj zwięzłą notatkę do egzaminu:
- kluczowe zasady procesu karnego
- najważniejsze terminy i ich długość
- 3-5 orzeczeń SN, które warto znać (z sygnaturami z CSV)
```

*Co dostaniesz:* Skondensowane opracowanie z konkretnymi przepisami i orzeczeniami do zapamiętania.

### 4.3. Kazus

```
Na podstawie przepisów w bazie nalegalu rozwiąż następujący kazus:

[opis stanu faktycznego]

Wskaż:
1. Które przepisy mają zastosowanie (z treścią z index.md)
2. Jakie roszczenia przysługują stronom
3. Jak orzekały sądy w podobnych sprawach (sygnatury z CSV)
```

*Co dostaniesz:* Analizę kazusu z przepisami i orzeczeniami z bazy. Dobry trening przed egzaminem.

---

## 5. Analiza porównawcza

### 5.1. Mapa przepisów do problemu

```
Jakie przepisy w bazie nalegalu regulują [np. odpowiedzialność za produkt
niebezpieczny / ochronę danych osobowych / mobbing]?

Przeszukaj pliki index.md w różnych katalogach tematycznych.
Dla każdego znalezionego przepisu podaj:
- ustawa i artykuł
- krótkie streszczenie
- liczbę orzeczeń w CSV (jeśli istnieje)
```

*Co dostaniesz:* Mapę przepisów z różnych ustaw dotyczących jednego tematu.

### 5.2. Krzyżowe odwołania między ustawami

```
Sprawdź, w jaki sposób [art. 415 Kodeksu cywilnego] jest powiązany z innymi
przepisami w bazie nalegalu.
1. Przeszukaj pliki index.md — które inne ustawy odwołują się do art. 415 k.c.?
2. Czy te same sygnatury orzeczeń pojawiają się przy art. 415 k.c.
   i przy przepisach innych ustaw?
```

*Co dostaniesz:* Sieć powiązań między przepisami różnych ustaw.

---

## Wskazówki

**Jeśli odpowiedź jest zbyt ogólna** — dodaj: „Odpowiedz wyłącznie na podstawie plików w bazie. Podaj ścieżki do plików, z których korzystasz."

**Jeśli Claude wymyśla sygnatury** — dodaj: „Podawaj TYLKO sygnatury znalezione w plikach CSV. Jeśli nie znalazłeś orzeczeń, napisz to wprost."

**Jeśli potrzebujesz więcej orzeczeń** — w orzecznictwo.md jest przegląd, ale pełna lista jest w plikach CSV. Poproś Claude'a o przeczytanie konkretnego pliku CSV.

**Jeśli szukasz przepisu, ale nie znasz numeru** — użyj promptu tematycznego (sekcja 5.1) zamiast pytania o konkretny artykuł.

---

## Zgłaszanie nowych promptów

Ta biblioteka jest rozwijana na podstawie rzeczywistego użycia. Jeśli masz prompt, który dobrze działa z nalegalu — zgłoś go przez Issues na GitHubie lub wyślij na kontakt@nalegalu.org.

---

*Ostatnia aktualizacja: maj 2026*
