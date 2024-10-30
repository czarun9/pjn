
# Klasy Gramatyczne i Części Mowy w spaCy

## Części Mowy (`pos_`)

| Skrót | Pełna nazwa (po angielsku) | Opis (po polsku) |
|-------|-----------------------------|-------------------|
| ADJ   | Adjective                   | Przymiotnik       |
| ADP   | Adposition                  | Przyimek          |
| ADV   | Adverb                      | Przysłówek        |
| AUX   | Auxiliary                   | Czasownik posiłkowy (np. "być", "mieć" w kontekstach gramatycznych) |
| CCONJ | Coordinating Conjunction    | Spójnik współrzędny |
| DET   | Determiner                  | Określnik (np. "ten", "ta") |
| INTJ  | Interjection                | Wykrzyknik        |
| NOUN  | Noun                        | Rzeczownik        |
| NUM   | Numeral                     | Liczebnik         |
| PART  | Particle                    | Partykuła (np. "nie", "czy") |
| PRON  | Pronoun                     | Zaimek            |
| PROPN | Proper Noun                 | Nazwa własna      |
| PUNCT | Punctuation                 | Znak interpunkcyjny |
| SCONJ | Subordinating Conjunction   | Spójnik podrzędny |
| SYM   | Symbol                      | Symbol (np. %, $, &) |
| VERB  | Verb                        | Czasownik         |
| X     | Other                       | Inne (elementy niepasujące do standardowych kategorii) |
| SPACE | Space                       | Przestrzeń, biały znak |



# Analiza parametrów `morph` w spaCy

Parametr `morph` w bibliotece spaCy zawiera informacje gramatyczne dotyczące tokenów. Oto najważniejsze kategorie oraz przykłady, które mogą się pojawić jako wartości `morph`:

## 1. Liczba (Number)
- **Singular**: Liczba pojedyncza
- **Plural**: Liczba mnoga

## 2. Rodzaj (Gender)
- **Masculine**: Rodzaj męski
- **Feminine**: Rodzaj żeński
- **Neuter**: Rodzaj nijaki

## 3. Przypadek (Case)
- **Nominative**: Mianownik
- **Genitive**: Dopełniacz
- **Dative**: Celownik
- **Accusative**: Biernik
- **Instrumental**: Narzędnik
- **Locative**: Miejscownik
- **Vocative**: Wołacz

## 4. Czas (Tense)
- **Present**: Czas teraźniejszy
- **Past**: Czas przeszły
- **Future**: Czas przyszły

## 5. Aspekt (Aspect)
- **Perfective**: Aspekt dokonany
- **Imperfective**: Aspekt niedokonany

## 6. Tryb (Mood)
- **Indicative**: Tryb oznajmujący
- **Subjunctive**: Tryb łączący
- **Imperative**: Tryb rozkazujący

## 7. Osoba (Person)
- **1st Person**: 1. osoba (ja, my)
- **2nd Person**: 2. osoba (ty, wy)
- **3rd Person**: 3. osoba (on, ona, ono, oni)

## 8. Liczba (Degree)
- **Positive**: Stopień podstawowy (przymiotników i przysłówków)
- **Comparative**: Stopień wyższy
- **Superlative**: Stopień najwyższy

## Przykłady wartości `morph`:
- `Number=Plur` (liczba mnoga)
- `Gender=Fem` (rodzaj żeński)
- `Case=Gen` (dopełniacz)
- `Tense=Past` (czas przeszły)
- `Mood=Ind` (tryb oznajmujący)