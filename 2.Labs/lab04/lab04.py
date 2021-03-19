""" Lab 04 """


this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if(n<=0):
        return 0
    return skip_add(n-2)+n

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if(n==1):
        return term(n)
    return summation(n-1,term)+term(n)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if (a%b==0):
        return b
    elif a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def helper(m,n):
        if m==0 and n==0:
            return 1
        if m<0 or n<0:
            return 0
        down=helper(m-1,n)
        left=helper(m,n-1)
        return down+left
    return helper(m-1,n-1) #start at (m-1,n-1), goal is at (0,0)

def max_subseq(n, l):
    """
    Return the maximum subsequence of length at most l that can be found in the given number n.
    For example, for n = 20125 and l = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    # traversal all the way to length==0 then return 0 becuase length zero means nonthing, or return n when n is single digit, which it will go back to compare the previosu digit
    if(l==0):
        return 0
    elif(n<10):
        return n
    #n//10 : both recurrsion call round down one digit, the one with (l-1) will return l-1 digits plus the last digit (total: l digits), the one with (l) will reurn l (total:l digits), and these two will compare
    with_Last_digit_and_minus_length_by_one=max_subseq(n//10,l-1)*10+n%10
    without_last_digit_and_keep_length_unchange=max_subseq(n//10,l)
    return max(with_Last_digit_and_minus_length_by_one, without_last_digit_and_keep_length_unchange)
