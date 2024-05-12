# Tokenizer

## Implementacja

Implementacja jest bardzo prosta i opiera się na podziale tekstu na tokeny poprzez iterację po każdym jego znaku i weryfikację każdego z nich.

Funkcja `__split_text` zwraca listę tokenów zgodnie z zadanymi kryteriami.

Do wyboru mamy **4** gotowe metody tokenizacji:
- `by_sentence()` - podział tekstu na zdania
- `by_word()` - podział tekstu na słowa (znaki interpunkcyjne są traktowane jako osobne tokeny)
- `by_custom_delimiter()` - podział tekstu podanym przez użytkownika separatorem, np. `by_custom_delimiter(',')`
- `by_character()` - podział tekstu na pojedyncze znaki

W pliku głównym podany jest gotowy przykład użycia każdej z metod.

## Ograniczenia

- Metody tokenizacji na sentencje i słowa obsługują jedynie podstawowe znaki interpunkcyjne (`.`, `!`, `?`, `,`, `;`, `:`) oraz niektóre znaki specjalne
- Brak obsługi zagnieżdżonych separatorów
- Brak obsługi wyrażeń specyficznych dla danego języka
- Wydajność spadająca wraz z długością tekstu

## Dodatkowe parametry funkcji `__split_text`

- `strip` - usuwania białych znaków z tokenów
- `skip_delimiter` - pomijanie separatorów w wynikowej liście tokenów
- `punctuation_as_item` - traktowanie znaków interpunkcyjnych jako osobnych tokenów (użyte w metodzie `by_word`)