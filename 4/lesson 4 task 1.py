from sys import argv
def salary()
  try:
    hours, wrate, bon = map(float, argv[1:])
    print(f' Your salary is: {hours * wrate + bon}')
  except ValueError:
    print('Error')

    
salary()
    
