# Tokenizer

## Implementacja

Implementacja tokenizacji opiera się na bardzo prostym algorytmie, który iteruje po każdym znaku tekstu i na podstawie zadanego kryterium decyduje o podziale tekstu na tokeny.
Funkcja `__split_text` zwraca listę tokenów zgodnie z zadanymi kryteriami.

Wybrałem takie podejście, ponieważ jest to prosta implementacja przydatna do zastosowań, w których niewymagane są zaawansowane metody tokenizacji.

Dostępne są cztery metody tokenizacji:
- `by_sentence()` - podział tekstu na zdania
- `by_word()` - podział tekstu na słowa (znaki interpunkcyjne są traktowane jako osobne tokeny)
- `by_custom_delimiter()` - podział tekstu podanym przez użytkownika separatorem, np. `by_custom_delimiter(',')`
- `by_character()` - podział tekstu na pojedyncze znaki

W pliku głównym podany jest gotowy przykład użycia każdej z metod.

## Dodatkowe parametry funkcji `__split_text`

- `strip` - usuwania białych znaków z tokenów
- `skip_delimiter` - pomijanie separatorów w wynikowej liście tokenów
- `punctuation_as_item` - traktowanie znaków interpunkcyjnych jako osobnych tokenów (użyte w metodzie `by_word`)

## Ograniczenia

Głównymi ograniczeniami tego rozwiązania są:
- brak obsługi zagnieżdżonych separatorów
- brak obsługi wyrażeń specyficznych dla danego języka
- obsługa jedynie podstawowych znaków interpunkcyjnych oraz niektórych znaków specjalnych
- wydajność spadająca wraz z długością tekstu