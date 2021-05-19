def main():
    # add a quote to 'quotes.txt'

    quote = input("Enter the quote: ")

    f = open('quotes.txt','a',encoding='utf-8')
    f.write(quote)
    f.close()


if __name__== "__main__":
    main()
