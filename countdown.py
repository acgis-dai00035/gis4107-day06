#-------------------------------------------------------------------------------
# Name:    countdown.py
#
# Purpose:
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

def get_countdown_as_text_using_for(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0
    """
    output =  str(start_value)
    for i in range(0,start_value):
        output = output + ' ' + str(start_value - i - 1)
    return output



def get_countdown_as_text_using_while(start_value=10):
    """Given a start_value, default is 10, return a space delimited string
       containing numbers descending from start_value to 0
   """
    n=0
    outputw = str(start_value)
    while n < start_value:
        outputw = outputw + ' ' + str(start_value - n - 1)
        n += 1
    return outputw
if __name__ == '__main__':
    main()
