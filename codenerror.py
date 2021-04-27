def measurements(m1, m2):
    if m1 > 0 and m2 > 0:
        large = float(max(m1, m2))
        small = float(min(m1, m2))
        way1 = (large / 2) * small
        way2 = (small / 2) * large
        print(f'method1 = {way1} ')
        print(f'method2 = {way2} ')
    m1 = float(input('Enter input 1: '))
    m2 = float(input('Enter input 2: '))
    if m1 > 0 and m2 > 0:
        pass


m1 = float(input('Enter input 1: '))
m2 = float(input('Enter input 2: '))

method1 = measurements(m1,m2)
method2 = measurements(m2,m1)