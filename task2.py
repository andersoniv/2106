def word_palindrome(word):
    word1 = word.replace(' ', '')[::-1]
    if word1 == word.replace(' ', ''):
        print(f'Слово "{word}" - является палиндромом')
    else:
        print(f'Слово "{word}"  - не является палиндромом')
word_palindrome(input('Напишите слово: '))