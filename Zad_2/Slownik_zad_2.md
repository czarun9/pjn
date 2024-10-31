
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



## Analiza Taga `token.tag_` w języku polskim

Tagi w atrybucie `token.tag_` wskazują na specyficzne cechy gramatyczne tokenów w tekście. Analiza ta jest przydatna przy przetwarzaniu języka naturalnego, zwłaszcza w przypadku klasyfikacji, rozpoznawania wzorców lub analizy składniowej.

### Tabela: Opis Tagów `token.tag_`

| Tag       | Opis                                             | Przykłady           |
|-----------|--------------------------------------------------|----------------------|
| `subst`   | Rzeczownik                                       | kot, miasto         |
| `adj`     | Przymiotnik                                      | szybki, wysoki      |
| `adv`     | Przysłówek                                       | szybko, dobrze      |
| `fin`     | Czasownik w formie osobowej                      | idzie, widzimy      |
| `bedzie`  | Czasownik przyszły                               | będzie              |
| `aglt`    | Agregat czasownikowy (np. formy być)             | będzie, jestem      |
| `praet`   | Czas przeszły                                    | poszedł, mówił      |
| `impt`    | Tryb rozkazujący                                 | idź, zobacz         |
| `imps`    | Forma bezosobowa                                 | grzmi, pada         |
| `inf`     | Bezokolicznik                                    | iść, spać           |
| `pcon`    | Imiesłów przysłówkowy współczesny                | idąc, patrząc       |
| `pant`    | Imiesłów przysłówkowy uprzedni                   | zobaczywszy, poszedłszy |
| `ger`     | Rzeczownik odsłowny (gerundium)                  | bieganie, śpiewanie |
| `pact`    | Imiesłów przymiotnikowy czynny                   | biegnący, śpiewający|
| `ppas`    | Imiesłów przymiotnikowy bierny                   | zrobiony, pomalowany|
| `winien`  | Forma przymiotnikowa czasownika                  | winien, powinien    |
| `pred`    | Predykatyw                                       | szkoda, brak        |
| `prep`    | Przyimek                                         | na, w, pod          |
| `conj`    | Spójnik                                          | i, lub, ale         |
| `comp`    | Partykuła porównawcza                            | niż, jak            |
| `qub`     | Partykuła                                        | nie, by, już        |
| `brev`    | Skrót                                            | mgr, prof.          |
| `interp`  | Znak interpunkcyjny                              | ., !, ?             |
| `xxx`     | Token nieznany lub nieprzypisany                 |                     |

### Opis wybranych Tagów

- **`subst`**: Oznacza rzeczowniki, które są najczęściej odmieniane przez przypadki i liczby. Przykład: _kot_ (kot, kota, kotem).
- **`adj`**: Tagi dla przymiotników, które mogą pełnić rolę przydawki, np. w zdaniu _szybki pies_.
- **`adv`**: Przysłówki, które modyfikują znaczenie czasownika, przymiotnika lub innego przysłówka (np. _szybko_, _dobrze_).
- **`fin`**: Forma czasownika, która odzwierciedla osobę, czas oraz liczbę, np. _idzie_, _widzą_.
- **`inf`**: Forma bezosobowa czasownika, nie odmieniana przez osoby, np. _iść_, _biegać_.
- **`ger`**: Rzeczowniki odsłowne (ang. gerunds), które powstają z czasowników i pełnią rolę rzeczowników, np. _bieganie_, _czytanie_.
- **`interp`**: Znaki interpunkcyjne używane jako tokeny oddzielające zdania lub części wypowiedzi, np. kropka, przecinek.

### Wnioski z Analizy Taga `token.tag_`

Dzięki analizie poszczególnych tagów możemy:
- Wyodrębnić konkretne części mowy (np. rzeczowniki, przymiotniki), co jest przydatne w analizie tematycznej.
- Przeprowadzić analizę składniową, aby rozpoznać struktury zdań i wzorce gramatyczne.
- Klasyfikować słowa według funkcji gramatycznych, co może służyć do tworzenia słowników tematycznych lub analizy stylu.
