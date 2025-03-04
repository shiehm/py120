class NegativeNumberError(ValueError):
    def __init__(self, message='Number cannot be negative.'):
        super().__init__(message)

def divider():
    try:
        first = float(input('Enter first number (the dividend): '))
        second = float(input('Enter second number (the divisor): '))
        result = first / second
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print(f'Error: {e}')
    else:
        if first < 0 or second < 0:
            raise NegativeNumberError 
        print(f'The result is {result}')
    finally:
        print('End of program.')

def inverse(lst):
    # try:
        # return [1/num for num in lst]
    # except (ValueError, TypeError) as e:
    #     print(f'Error: {e}')
    new_lst = []
    for num in lst:
        try:
            new_lst.append(1/num)
        except ZeroDivisionError:
            new_lst.append(float('inf'))
        except TypeError:
            pass
    return new_lst

lst = [num for num in range(10)] + ['abc', 'def'] + [11, 12, 13]
print(inverse(lst))

# lst = ['abc']
# print(inverse(lst))



students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return 'Student not found'

print(get_age('John'))
print(get_age('Melvin'))



numbers = [1, 2, 3, 4, 5]

# LBYL
def get_sixth_lbyl(lst):
    if len(lst) > 5:
        return lst[5]
    return None

print(get_sixth_lbyl(numbers))

# AFNP
def get_sixth_afnp(lst):
    try:
        return lst[5]
    except IndexError:
        return None

print(get_sixth_afnp(numbers))