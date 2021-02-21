def print_to_n(n):
	"""
	this function prints all the numbers from 1 up to n in this order.
	:param n: positive int number
	:return: prints all natural numbers smaller or equal to n, from 1 to n
	"""
	if n < 1:  # edge case
		return None
	if n == 1:  # base case
		print(n)
	else:
		print_to_n(n - 1)  # recursive call
		print(n)


def print_reversed(n):
	"""
	this function prints all the numbers from n down to 1 in this order.
	:param n: positive int number
	:return: prints all natural numbers smaller or equal to n, from n to 1
	"""
	if n < 1:  # edge case
		return None
	if n == 1:  # base case
		pass
	print(n)
	n = n - 1
	print_reversed(n)  # recursive call


def n_divides_by_i(n, i):
	"""
	aid function for is_prime function. thie function checks if i divides
	by n, when n<i<1.
	:param n: number to be checked if prime
	:param i: variable from n to 1
	:return: True if prime, False if not
	"""
	if n % i != 0 and i != 1:
		if n_divides_by_i(n, i - 1):  # recursive call
			return True
		else:
			return False
	if i == 1:  # base case
		return False
	elif n % i == 0 and i != 1:
		return True


def is_prime(n):
	"""
	checks if n is a prime number.
	:param n: a natural number
	:return: True- if n is prime, False- if it is not
	"""
	if n < 1:  # edge case
		return None
	if n == 1:  # base case
		return False
	i = n - 1
	if not n_divides_by_i(n, i):
		return True
	else:
		return False


def if_divides(n, i, list):
	"""
	aid function for divisor function. builds a list of all the natural
	dividers of n.
	:param n: natural number to be checked
	:param i: variable, if n%i == 0 then i gets in the dividers list
	:param list: the list to be built
	:return: returns the list of dividers
	"""
	if n % i == 0:
		list.append(int(n / i))
	if i == 1:  # base case
		return None
	if_divides(n, i - 1, list)  # recursive call


def divisors(n):
	"""
	this function gets an int as input and returns a list of all of the
	natural numbers that n is divided by without remainder
	:param n: a natural number
	:return: list of natural dividers of n
	"""
	divisors_lst = []  # creates a list to be filled
	i = n
	if_divides(n, i, divisors_lst)
	return divisors_lst


def factorial(n):
	"""
	this is an aid function for the exp_n_x function. it gets an int and
	returns the factorial value of n. this function uses recursion
	:param n: an int number
	:return: factorial of n (n!)
	"""
	if n == 0:  # base case
		return 1
	else:  # recursive case
		return n * factorial(n - 1)


def power_of_i(n, x):
	"""
	aid function for exp_n_x function. gets to ints (x, n) and returns
	x raised to the power of n
	:param n: int
	:param x: int
	:return: n ** x
	"""
	return x ** n


def exp_n_x(n, x):
	"""
	this function gets n and x (ints) and returns expn(x). this function uses
	two aid functions and uses recursion.
	:param n: int
	:param x: real number
	:return: exp n of x
	"""
	if n == 0:  # base case
		return 1
	else:  # recursive call
		single_val = power_of_i(n, x) / factorial(n)
		single_val += exp_n_x(n - 1, x)
		return single_val


def play_hanoi(hanoi, n, src, dest, temp):
	"""
	this function allows us to play the hanoi towers game, using a gui you
	built. this function uses recursion in order to play by the rules.
	:param hanoi:
	:param n: number of disks
	:param src: source poll
	:param dest: destination poll
	:param temp: temporary poll
	:return: plays the game
	"""
	if n < 0:  # edge case - if n is smaller than 0, regard to it as 0
		play_hanoi(hanoi, 0, src, dest, temp)
	elif n == 1:
		hanoi.move(src, dest)  # base case
	else:  # recursive case
		play_hanoi(hanoi, n - 1, src, temp, dest)
		play_hanoi(hanoi, 1, src, dest, temp)
		play_hanoi(hanoi, n - 1, temp, dest, src)


def print_binary_sequence_with_prefix(prefix, n):
	"""
	this function is an aid function for the print binary seq. it gets a
	prefix (0 or 1) and returns all the different combinations in the length
	of n that start in the prefix. this function uses recursion.
	:param prefix: 1 or 0
	:param n: wanted length of the binary sequences
	:return: all possible sequences in length n that start with prefix (0\1)
	"""
	if n == 1:  # base case
		print(prefix)
	else:  # recursion case
		print_binary_sequence_with_prefix((str(prefix) + '0'), n - 1),
		print_binary_sequence_with_prefix((str(prefix) + '1'), n - 1)


def print_binary_sequences(n):
	"""
	this function gets n (int) and returns all binary sequences in length n.
	:param n: wanted length of the binary seq
	:return: all possible binary seq in length n
	"""
	if n == 0:  # base case
		print('')
	else:  # recursive call (the aid function is recursive, this one is not)
		print_binary_sequence_with_prefix(1, n)
		print_binary_sequence_with_prefix(0, n)


def print_seq_with_prefix(char_list, n, prefix):
	"""
	this is an aid function for the print_sequence function. it prints all
	the possible sequences with the prefix "prefix", while prefix is obtained
	from a for loop on the char_list
	:param char_list: list of characters to be made into sequences in length n
	:param n: wanted length of sequences
	:param prefix: an item from char_list
	:return: all possible sequences in length n starting with prefix
	"""
	if n == 1:  # base case
		print(prefix)
	else:
		for k in char_list:  # for loop, iterating over all items in char_list
			# recursive call:
			print_seq_with_prefix(char_list, n - 1, str(k) + str(prefix))
			continue


def print_sequences(char_list, n):
	"""
	a function that prints all possible sequences of items in char_list in
	length n
	:param char_list: a list of different characters
	:param n: wanted length of returned sequences
	:return: all possible sequences in length n from items in char_list
	"""
	if n == 0: # edge case
		print('')
		return
	if n == 1:  # base case. prints all single items in char_list if n=1
		for i in char_list:  # iterating over char_list
			print(i)
	else:
		for j in char_list:  # iterating over char_list
			print_seq_with_prefix(char_list, n, j)  # recursive call


def print_no_rep_seq_with_pre(char_list, n, prefix):
	"""
	this is an aid function for the print_no_repetition_sequences function.
	it returns all possible sequences in length n that start with prefix.
	this function uses recursion.
	:param char_list: list to make sequences from
	:param n: wanted length of returned sequences
	:param prefix: an item from char_list
	:return: all possible sequences in length n that start with prefix
	"""
	if n == 1:  # base case
		print(prefix)
	else:
		for k in char_list:  # for loop, iterating over all items in char_list
			prefix_lst = list(str(prefix))
			if str(k) in prefix_lst:
				continue
			else:
				# recursive call:
				print_no_rep_seq_with_pre(char_list, n - 1,
				                          str(prefix) + str(k))


def print_no_repetition_sequences(char_list, n):
	"""
	this function returns all possible sequences in length n from char_list
	without repetition of characters.
	:param char_list: a given list of items
	:param n: wanted length of returned sequences
	:return: all possible sequences in length n
	"""
	for j in char_list:  # iterating over char_list
		print_no_rep_seq_with_pre(char_list, n, j)  # calls aid function


def no_rep_seq_with_pre(char_list, n, prefix, seq_list):
	"""
	this is an aid function for the no_repetition_sequences_list function.
	it returns all possible sequences in length n that start with prefix.
	this function uses recursion.
	:param char_list: list to make sequences from
	:param n: wanted length of returned sequences
	:param prefix: an item from char_list
	:return: all possible sequences in length n that start with prefix
	"""
	if n == 1:  # base case
		seq_list.append(prefix)
	else:
		for k in char_list:  # for loop, iterating over all items in char_list
			prefix_lst = list(str(prefix))
			if str(k) in prefix_lst:
				continue
			else:
				# recursive call:
				no_rep_seq_with_pre(char_list, n - 1, str(prefix) + str(k),
				                    seq_list)


def no_repetition_sequences_list(char_list, n):
	"""
	this function returns a list of all possible sequences in length n from
	char_list.
	:param char_list: a given list of items
	:param n: wanted length of returned sequences
	:return: all possible sequences in length n without having the same note
	in it more than once.
	"""
	seq_list = []
	if n == 0:
		return ['']
	else:
		for j in char_list:  # iterating over char_list
			# calls aid function
			no_rep_seq_with_pre(char_list, n, j, seq_list)
		return seq_list
