#-------------------------------------------------------------------------------
# Name:    continue_break_examples.py
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

def main():
    """main()"""

def continue_break_example(max_loop_value, continue_value, break_value):
    """Demonstrate continue and break in for loop
    """
    for i in range(max_loop_value + 1):
        if i == continue_value: continue
        if i == break_value: break
    else:
        print "No break"

def reformat_text(text, max_dash_count):
    """Given text that contains dashes, ignore dashes up to max_dash_count
    and return all text up to max_dash_count.  The returned text does not
    include the dashes.  For example, given text = 'a-b-c', and
    max_dash_count of 1, the function would return 'a'  If text contains
    no dashes, text will be returned.
    """
    n = 0
    newtext = ''
    for i in text :
        if i == '-' : continue
        if n == max_dash_count :break
        n = n + 1
        newtext = newtext + i
    return newtext

if __name__ == '__main__':
    main()
