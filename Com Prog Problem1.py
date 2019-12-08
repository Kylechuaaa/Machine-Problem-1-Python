import matplotlib.pyplot as plt

print ('')


a = list(range(100))

def Python(a):

    if a <= 9:
        
        D = (a**(2)-7)
        return D
    
    return Python(a-10)

first = []
second = []
for C in a:

    first.append(C)
    second.append(Python(C))
    
    
    
plt.stem(first, second, '--')
plt.grid()
plt.suptitle('Graph')
plt.show()
