class Author:
    def __init__(self, name): #Initalized with a name and an empty list of books
        self.name = name
        self.books = []
    
    def publish(self, title): # Publish method, simply appending to the list, no duplicate checking
        self.books.append(title)
    
    def __str__(self):
        titles = ', '.join(self.books) or 'This Author Has No Published Books' # Join the list of books together into a single string, unless there are no books.
        return f'Name: {self.name} | Books Published: {titles}'

def main():
    shakespeare = Author('William Shakespeare') # Example data
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    print(shakespeare)

    jake = Author('Jake') # More example data
    jake.publish('My new book')
    jake.publish('My new book') # Test too check if the program is catching duplicates.
    jake.publish('My new book 2: The revenge')
    print(jake)

if __name__ == '__main__': # Call main
    main()