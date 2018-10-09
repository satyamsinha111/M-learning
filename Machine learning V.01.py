Data = ['Rahul', 'Vinod', 'Elephant', 'Monkey']

while True:


   Query=input('Enter the word:')
   if Query in Data:
       print('Its a noun')
   if Query not in Data:
    ask=input('Is it a noun??')
    if ask.lower() =='Yes'.lower():
           Data.append(Query.title())
    else:
        print('Ohh!!')
