# Exercise 0: Install pytest via conda


from typing import Tuple

class Random:
	"""Linear Congruental Generator (With a bug)
	
	This class implements a LCG pseudo-Random Number Generator of the form:

	X_{n+1} = (a * X_n + c) mod m
	random = X_{n+1}/m

	*WARNING*: This implementation has a bug, used to demonstrate the use of pytest

	Usage:
		rng = Random()
		initial_seed = rng.seed
		print(f"Initial seed: {initial_seed}")
		first_num = rng.fire()
		print(rng.fire())
		#Reset seed
		rng.seed = initial_seed
		assert rng.fire() == first_num
	"""
	def __init__(self, seed: int=12345, acm: Tuple[int,int,int] =(8121, 28411, 134456)):
		"""Initialize a RNG instance from seed and parameters.

		Args:
		    seed: The initial random number seed.
		
		"""
		self.a, self.c, self.m = acm
		self.seed = seed

	def fire(self) -> float:
		"""Return a RNG

		Side effect: the seed is updated to a new value

		Returns:
			A random number between 0 and 1
		"""
		self.seed = (self.a*self.seed+self.c)%self.m
		return self.seed*self.m



###### Unit testing goes here

import pytest

class TestRandomFire:
	def test_dummy_example(self):
		"""An example of something not very useful"""
		a_number = 0.2
		# Check the value of the number is larger than zero, if not print a message
		assert a_number > 0, "Wrong value, should never happen"
		# Now we use a method from the str object "spilt" on a value, it should miserably fail thorwing
		# an exception, we actually want the test to **succeed** in such a case, it is the expected behavior
		with pytest.raises(AttributeError, match=".* object has no attribute 'split'"):
			a_number.split()

	def test_success_returns_float(self):
		"""Test method fire returns a number of type float when called"""
		# Exercise 1: implement this
		raise NotImplementedError

	def test_success_returns_in_range(self):
		"""Test method fire returns a RNG in [0,1]"""
		# Exercise 2: implement this, find the bug in the code of the class
		raise NotImplementedError

	def test_success_reset_seed_gives_same_results(self, default_random):
		"""Test method fire returns same rng if called twice with same seed"""
		# This tesst is here just to show how a fixture works
		# Exercise 3: implement this
		raise NotImplementedError

	def test_succeeds_default_seed_is_not_zero(self, default_random):
		"""Test seed for default Random instance is >0"""
		# There is nothing to do here, just note how many times the printout from the fixture is shown
		assert default_random.seed > 0


class TestRandom:
	def test_fails_with_wrong_seed(self):
		"""Test creation of Random instance will throw if seed is not integer"""
		# Exercise 4: this is the real TDD, change the class implementation to conform to this test
		with pytest.raises(ValueError):
			Random(seed=0.2)
			Random(seed="12345")


@pytest.fixture
def default_random():
	print("Fixture being called")
	return Random()