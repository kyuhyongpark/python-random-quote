import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt", encoding='utf-8')
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1

  rnd1 = random.randint(0, last)

  print(quotes[rnd1].rstrip())

  rnd2 = random.randint(0, last)
  while rnd1 == rnd2:
    rnd2 = random.randint(0, last)

  print(quotes[rnd2].rstrip())

if __name__== "__main__":
  primary()
