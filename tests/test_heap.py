from typed_data_structures import Heap
import pytest


class TestHeap:
	@pytest.fixture
	def empty_heap(self) -> Heap[int]:
		return Heap()

	@pytest.fixture
	def abs_heap(self) -> Heap[int]:
		return Heap([3, -2, -6, 1, 7, -4, 5, -8, 0, 9], abs)

	def test_push(self, abs_heap: Heap[int], empty_heap: Heap[int]):
		assert len(empty_heap) == 0
		empty_heap.push(0)
		assert len(empty_heap) == 1
		assert 0 in empty_heap

		abs_heap.push(100, -1)
		assert abs_heap.peek() == 100

	def test_pop(self, abs_heap: Heap[int], empty_heap: Heap[int]):
		assert 0 in abs_heap
		assert abs_heap.pop() == 0
		assert 0 not in abs_heap

		with pytest.raises(IndexError):
			empty_heap.pop()

	def test_peek(self, abs_heap: Heap[int]):
		assert abs_heap.peek() == 0
		assert 0 in abs_heap

	def test_len(self, abs_heap: Heap[int], empty_heap: Heap[int]):
		assert len(abs_heap) == 10
		assert len(empty_heap) == 0

	def test_bool(self, abs_heap: Heap[int], empty_heap: Heap[int]):
		assert abs_heap
		assert not empty_heap

	def test_contains(self, abs_heap: Heap[int], empty_heap: Heap[int]):
		assert -2 in abs_heap
		assert 2 not in abs_heap
		assert -2 not in empty_heap