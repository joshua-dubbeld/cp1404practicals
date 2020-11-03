import wikipedia

query = input("Search Wikipedia: ")
while query != '':
    try:
        search = wikipedia.page(query)
        print(search.title)
        print(search.summary)
        print(search.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Did you mean...", e.options[:5])
    query = input("Search Wikipedia: ")
