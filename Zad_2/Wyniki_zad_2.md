## Wykresy częstości występowania klas gramatycznych i części mowy (POS)

### Calineczka
| Częstości POS'ów                                           | Częstości klas gramatycznych                               |
|------------------------------------------------------------|------------------------------------------------------------|
| ![POS](/resources/plots/zad2/calineczka-pos-frequency.png) | ![Tag](/resources/plots/zad2/calineczka-tag-frequency.png) |

### Dziewczynka z zapałkami
| Częstości POS'ów                                                          | Częstości klas gramatycznych                                            |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| ![POS](/resources/plots/zad2/dziewczynka-z-zapalkami-pos-frequency.png)   | ![Tag](/resources/plots/zad2/dziewczynka-z-zapalkami-tag-frequency.png) |

### Królowa Śniegu
| Częstości POS'ów                                               | Częstości klas gramatycznych                                   |
|----------------------------------------------------------------|----------------------------------------------------------------|
| ![POS](/resources/plots/zad2/krolowa-sniegu-pos-frequency.png) | ![Tag](/resources/plots/zad2/krolowa-sniegu-tag-frequency.png) |

### Mała Syrenka
| Częstości POS'ów                                             | Częstości klas gramatycznych                                 |
|--------------------------------------------------------------|--------------------------------------------------------------|
| ![POS](/resources/plots/zad2/mala-syrenka-pos-frequency.png) | ![Tag](/resources/plots/zad2/mala-syrenka-tag-frequency.png) |

### W pustyni i w puszczy
| Częstości POS'ów                                                      | Częstości klas gramatycznych                                          |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| ![POS](/resources/plots/zad2/w-pustyni-i-w-puszczy-pos-frequency.png) | ![Tag](/resources/plots/zad2/w-pustyni-i-w-puszczy-tag-frequency.png) |

# Częstość występowania rzeczowników w formach podstawowych

## Wykresy częstości występowania rzeczowników w formach podstawych (lematach)

### Calineczka
| Częstość występowania lematu rzeczownika                     |
|--------------------------------------------------------------|
| ![Noun](/resources/plots/zad2/calineczka-noun-frequency.png) |

### Dziewczynka z zapałkami
| Częstość występowania lematu rzeczownika                                   |
|----------------------------------------------------------------------------|
| ![Noun](/resources/plots/zad2/dziewczynka-z-zapalkami-noun-frequency.png)  |

### Królowa Śniegu
| Częstość występowania lematu rzeczownika                          |
|-------------------------------------------------------------------|
| ![Noun](/resources/plots/zad2/krolowa-sniegu-noun-frequency.png)  |

### Mała Syrenka
| Częstość występowania lematu rzeczownika                       |
|----------------------------------------------------------------|
| ![Noun](/resources/plots/zad2/mala-syrenka-noun-frequency.png) |

### W pustyni i w puszczy
| Częstość występowania lematu rzeczownika                                |
|-------------------------------------------------------------------------|
| ![Noun](/resources/plots/zad2/w-pustyni-i-w-puszczy-noun-frequency.png) |

# Wizualizacja wagi słów w macierzy TfIdf w postaci chmury tagów

### Calineczka
| Chmura słów po wadze słowa w macierzy TfIdf                             |
|-------------------------------------------------------------------------|
| ![WordCloud](/resources/plots/zad2/calineczka-wordcloud.png)            |

### Dziewczynka z zapałkami
| Chmura słów po wadze słowa w macierzy TfIdf                                     |
|---------------------------------------------------------------------------------|
| ![WordCloud](/resources/plots/zad2/dziewczynka-z-zapalkami-wordcloud.png)       |

### Królowa Śniegu
| Chmura słów po wadze słowa w macierzy TfIdf                            |
|------------------------------------------------------------------------|
| ![WordCloud](/resources/plots/zad2/krolowa-sniegu-wordcloud.png)       |

### Mała Syrenka
| Chmura słów po wadze słowa w macierzy TfIdf                          |
|----------------------------------------------------------------------|
| ![WordCloud](/resources/plots/zad2/mala-syrenka-wordcloud.png)       |

### W pustyni i w puszczy
| Chmura słów po wadze słowa w macierzy TfIdf                                  |
|------------------------------------------------------------------------------|
| ![WordCloud](/resources/plots/zad2/w-pustyni-i-w-puszczy-wordcloud.png)      |

# Analiza niejednoznaczności znaczeniowej

Poniżej znajduje się kilka słów, które morfeusz wskazał jako takie, które posiadają więcej niż jedno potencjalne znaczenie wraz z ich potencjalnymi lematami oraz ich morfologią.

```
Słowo: dostępne
Możliwe analizy:
 - dostępny (adj:pl:acc:m2.m3.f.n:pos)
 - dostępny (adj:pl:nom.voc:m2.m3.f.n:pos)
 - dostępny (adj:sg:acc:n:pos)
 - dostępny (adj:sg:nom.voc:n:pos)


Słowo: brodzie
Możliwe analizy:
 - broda (subst:sg:dat.loc:f)
 - bród (subst:sg:loc:m3)
 - bród (subst:sg:voc:m3)


Słowo: otworzyliście
Możliwe analizy:
 - otworzyć (praet:pl:m1:perf)
 - być (aglt:pl:sec:imperf:nwok)


Słowo: Mały
Możliwe analizy:
 - mały:A (adj:sg:acc:m3:pos)
 - mały:A (adj:sg:nom.voc:m1.m2.m3:pos)
 - mały:S (subst:sg:nom:m1)
 - mały:S (subst:sg:voc:m1)
 - Mały:Sf (subst:sg.pl:nom.gen.dat.acc.inst.loc.voc:f)
 - Mały:Sm1 (subst:sg:nom:m1)
 - Mały:Sm1 (subst:sg:voc:m1)


Słowo: działo
Możliwe analizy:
 - działo (subst:sg:nom.acc.voc:n:ncol)
 - dziać (praet:sg:n:imperf)

```

# Analiza związków podmiotowo-orzeczeniowych

Poniżej znajdują się przykładowe podmioty wraz z ich orzeczeniami, które są związane grafem w spacy. Identyfikując podmioty w postaci rzeczowników możemy odwołać się do ich headu w grafie zdania, co w tym przypadku reprezentuje orzeczenie.

| Zdanie                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Hen, daleko od brzegów, aż na środku morza, gdzie nic nie widać, tylko błękit nad falami, gdzie woda przezroczysta jak kryształ najczystszy, a ciemnoszafirowa jak bławatek, jest głębia niezmierzona, otchłań tak głęboka, iż żaden okręt tutaj przystanąć nie może, bo kotwica dna nie dosięgnie.*                                                                                                                                               |
| *W tej niezgłębionej otchłani mieszkały piękne Syreny.*                                                                                                                                                                                                                                                                                                                                                                                             |



Wypis z programu:
```

Rzeczowniki pełniące funkcję podmiotu i związane z nimi czasowniki:
Podmiot: woda, Orzeczenie: kryształ
Podmiot: głębia, Orzeczenie: jest
Podmiot: okręt, Orzeczenie: przystanąć
Podmiot: kotwica, Orzeczenie: dosięgnie
Podmiot: otchłani, Orzeczenie: mieszkały

```

Jak widać nie działa to idealnie, ponieważ analiza związków podmiotowo-orzeczeniowych jest bardzo złożonym zagadanieniem, które wymaga analizy kontekstu oraz dużo bardziej rozbudowanych metod do analizy zdań, gdzie choćby słowo *jest* jest w domyśle, jak w fragmencie:
***gdzie woda przezroczysta jak kryształ najczystszy***. Co prawda zauważył on, że słowo kryształ zawiera się w orzeczeniu, a także niepoprawnie dopasował orzeczenie w przykładzie z otchłanią, gdzie mieszkały syreny, a nie otchłań, natomiast pokazuje to jak duży problem mają nawet popularne rozwiązania takie jak spacy z tym zadaniem.



