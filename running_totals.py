def main():
    """main()"""

def running_total(iteration):
    """it will return the sum of numbers from 1 to iterations inclusively.
    That is, if iterations was 3, then the function would return 1 + 2 + 3 = 6
    """
    output =''
    result = 0
    for i in range(iteration+1) :
        result += i+1
        output += str(i+1) +' '
        if i==iteration-1 :break
        output += '+ '
    output +='= ' + str(result)
    return output

def strange_sum(number) :
    """has one parameter named number.
    If the number was 4, this function would return the sum of the following series of numbers:
    1/4 + 2/3 + 3/2 + 4/1 = 6.41667
    """
    result = 0.0
    for i in range(number+1) :
        result += float(i+1)/float(number-i)
        if i==number-1 :break
    return result

if __name__ == '__main__':
    main()
