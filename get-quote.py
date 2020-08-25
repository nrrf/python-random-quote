def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.read().splitlines()
  f.close()

  print(quotes)

if __name__== "__main__":
  primary()
