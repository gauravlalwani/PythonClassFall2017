while True:
  print('What is your name?')
  name = input()
  if name != 'Robin':
    continue
  print('Hello, Robin. What is your favorite color?') 
  color = input()
  if color == 'green':
    break
  print('Sorry, wrong color!')
print('Congrats!')

