def geo(*args):
    product = 1;
    for x in args:

        product = product*x
    print(product)


geo(3,4,5,6,2)
# using 'get' class function on dicts returns a none rather than crashing when the key is not in the dictionary.

class Bird:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')



birdie = Bird(make = 'blue jay', model = 'small bird', year = 3)
bordie = Bird(make = 'Filtch')

print(birdie.model, bordie.model)