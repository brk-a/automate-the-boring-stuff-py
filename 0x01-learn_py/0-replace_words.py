sentence = input(f'Enter your sentence...\n')
target = input(f'Enter the word you want to remove...\n')
replacement = input(f'Enter the word you want to replace it with...\n')

print(f'Your sentence: {sentence}\nThe target: {target}\nReplacement: {replacement}\n')
print(f'{sentence.replace(target, replacement)}')