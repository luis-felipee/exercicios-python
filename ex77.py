words = ('Software', 'Engineer', 'Computer', 'Science', 'Math', 'Python', 'Ethical Hacker')
for i in words:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letter in i:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
