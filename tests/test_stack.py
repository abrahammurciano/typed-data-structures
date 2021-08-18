"""
tests.test_stack.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the Stack.py module.
"""

import pytest
from typed_data_structures import Stack


class TestStack:
	"""Test suite for SupplyCurve class."""

	@pytest.fixture
	def empty_stack(self) -> Stack[int]:
		return Stack[int]()

	@pytest.fixture
	def stack_to_ten(self) -> Stack[int]:
		return Stack[int](range(10))

	def test_push(self, stack_to_ten: Stack[int]):
		assert 11 not in stack_to_ten
		stack_to_ten.push(11)
		assert 11 in stack_to_ten

	def test_pop(self, empty_stack: Stack[int], stack_to_ten: Stack[int]):
		with pytest.raises(IndexError):
			empty_stack.pop()
		assert stack_to_ten.pop() == 9
		assert 9 not in stack_to_ten

	def test_len(self, empty_stack: Stack[int], stack_to_ten: Stack[int]):
		assert len(empty_stack) == 0
		assert len(stack_to_ten) == 10
		empty_stack.push(1)
		assert len(empty_stack) == 1

	def test_bool(self, empty_stack: Stack[int], stack_to_ten: Stack[int]):
		assert not empty_stack
		assert stack_to_ten
		empty_stack.push(1)
		assert empty_stack

	def test_contains(self, empty_stack: Stack[int], stack_to_ten: Stack[int]):
		assert 0 not in empty_stack
		assert 0 in stack_to_ten
		empty_stack.push(3)
		assert 3 in empty_stack

	def test_reversed(self, stack_to_ten: Stack[int]):
		assert list(reversed(stack_to_ten)), list(range(10, 1, -1))

	def test_iter(self, stack_to_ten: Stack[int]):
		i = 0
		for item in stack_to_ten:
			assert item == i
			i += 1
