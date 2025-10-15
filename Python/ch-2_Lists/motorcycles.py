#Changing, Adding and Removing Elements

motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements
motorcycles.append('honda')
print(motorcycles)

cars = []
cars.append('BMW')
cars.append('Lambo')
cars.append('Buggati')
cars.append('Audi')
print(cars)

#Inserting Elements into a list
cars.insert(4, 'Supra')
print(cars)

#Removing Elements From a list
del motorcycles[3]
print(motorcycles)

#Removing an item using pop method
Dark = ['jonas', 'martha', 'hannah', 'charlotte']
dark_pop = Dark.pop()
print(Dark)
print(dark_pop)

message = f'{dark_pop.title()} is a police officer in winden. '
print(message)

#popping items any position in a list
Avengers = ['Stark', 'Rogers', 'odinson', 'romanaff', 'barthon', 'banner']
print(Avengers)
pop_avengers = Avengers.pop(4)
print(Avengers)
print(pop_avengers)

print(f'My favourite avenger is Tony {Avengers[0].title()}')

#Removing an item by values

#use .remove('x') for it

upcoming = ['spiderman', 'doomsday','wednesday']