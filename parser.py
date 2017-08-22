import sys

class Parser(object):
  def parseInt(self,text):
    if text=='':
      self.error()
    n = len(text)
    if n < 1:
      self.error() 
    factor = 1
    startPos = 0
    firstChar = text[0]
    if firstChar == '+' or firstChar == '-':
      startPos = 1
      if firstChar == '-':
        factor = -1

    if n <= startPos:
      self.error()
    
    firstDigit = text[startPos]
    if firstDigit == '0':
      for i in range(startPos+1, n):
        if text[i] != '0':
          self.error()
      return 0
      
    if firstDigit < '1' or firstDigit > '9':
      self.error()

    result = int(firstDigit)
    isValid = True
    for i in range(startPos+1, n):
      digit = text[i]
      if digit >= '0' and digit <= '9':
        result *= 10
        result += int(digit)
      else:
        isValid = False 

    if isValid:
      return result * factor
    self.error()


  def error(self):
    raise Exception('invalid parsing')


def main():
    while True:
      try:
        text = input('A string: ')
      except EOFError:
        break

      try:
        parser = Parser()
        print(parser.parseInt(text))
      except:
        print("Unexpected error:", sys.exc_info()[0])



if __name__ == '__main__':
    main()

      
