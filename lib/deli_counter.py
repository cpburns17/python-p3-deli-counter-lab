

katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print('The line is currently empty.')
    else:
        line_msg = 'The line is currently:'
        for place, name in enumerate(katz_deli, start=1):
            line_msg += f' {place}. {name}'
        print(line_msg)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')


def now_serving(katz_deli):
    if not katz_deli:
        print('There is nobody waiting to be served!')
    else:
        next_person = katz_deli.pop(0)
        print(f'Currently serving {next_person}.')
        
        


# take_a_number(katz_deli, 'Connor')
# take_a_number(katz_deli, 'Charlie')
line(katz_deli)
# now_serving(katz_deli)
# now_serving(katz_deli)