def reverse_string(s):
    return s[::-1]

def unreverse_customer_name(reversed_name):
    words = reversed_name.split()
    return ' '.join(reverse_string(word) for word in words)
