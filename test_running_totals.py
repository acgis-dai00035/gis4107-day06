import running_totals
reload(running_totals)

def main():
    """main()"""
    test_running_total()
    strange_sum()

def test_running_total():
    expected = '1 + 2 + 3 = 6'
    arg = 3
    actual = running_totals.running_total(arg)
    compare_expected_and_actual(arg, expected, actual)

def strange_sum():
    expected = 6.41667
    arg = 4
    actual = round(running_totals.strange_sum(arg),5)
    compare_expected_and_actual(arg, expected, actual)



def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:{}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
