#-------------------------------------------------------------------------------
# Name:    test_continue_break_examples.py
#
# Purpose: Test continue_break_examples module.
#
# Author:  David Viljoen
#
# Created: 29/09/2019
#-------------------------------------------------------------------------------

import continue_break_examples as cbe
reload(cbe)

def main():
    """main()"""
    test_continue_break_example()
    test_reformat_text()

def test_continue_break_example():
    print "\ntest_continue_break_example()"
    max_loop_value = 5
    continue_value = 3
    break_value = 4
    cbe.continue_break_example(max_loop_value, continue_value, break_value)

def test_reformat_text():
    print '\ntest_reformat_text()'
    expected = 'abc'
    text = 'a-b-c-d'
    max_dash_count = 3
    actual = cbe.reformat_text(text, 3)
    compare_expected_and_actual(expected, actual, text, max_dash_count)

def compare_expected_and_actual(expected, actual, *args):
    print 'args are (text, max_dash_count)'
    if expected == actual:
        print 'PASSED:  For args =', args
    else:
        fmt = 'FAILED: For args = {}\nExpected: {}\nActual:   {}'
        print fmt.format(args, expected, actual)

if __name__ == '__main__':
    main()
