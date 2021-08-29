import pytest
from typed_data_structures import Queue


class TestQueue:
	@pytest.fixture
	def empty_queue(self) -> Queue[int]:
		return Queue[int]()

	@pytest.fixture
	def queue_to_ten(self) -> Queue[int]:
		return Queue[int](range(10))

	def test_push(self, queue_to_ten: Queue[int]):
		assert 11 not in queue_to_ten
		queue_to_ten.push(11)
		assert 11 in queue_to_ten

	def test_pop(self, empty_queue: Queue[int], queue_to_ten: Queue[int]):
		with pytest.raises(IndexError):
			empty_queue.pop()
		assert queue_to_ten.pop() == 0
		assert 0 not in queue_to_ten

	def test_len(self, empty_queue: Queue[int], queue_to_ten: Queue[int]):
		assert len(empty_queue) == 0
		assert len(queue_to_ten) == 10
		empty_queue.push(1)
		assert len(empty_queue) == 1

	def test_bool(self, empty_queue: Queue[int], queue_to_ten: Queue[int]):
		assert not empty_queue
		assert queue_to_ten
		empty_queue.push(1)
		assert empty_queue

	def test_contains(self, empty_queue: Queue[int], queue_to_ten: Queue[int]):
		assert 0 not in empty_queue
		assert 0 in queue_to_ten
		empty_queue.push(3)
		assert 3 in empty_queue

	def test_reversed(self, queue_to_ten: Queue[int]):
		assert list(reversed(queue_to_ten)), list(range(10, 1, -1))

	def test_iter(self, queue_to_ten: Queue[int]):
		i = 0
		for item in queue_to_ten:
			assert item == i
			i += 1
