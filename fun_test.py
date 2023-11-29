from fun import *


class TestPlanarity:
	def test_if_k_3_is_planar(self):
		adjacency_matrix = [
			[0, 1, 1],
			[1, 0, 1],
			[1, 1, 0],
		]
		k_3 = Graph(adjacency_matrix)

		assert k_3.is_planar() is True

	def test_if_k_4_is_planar(self):
		adjacency_matrix = [
			[0, 1, 1, 1],
			[1, 0, 1, 1],
			[1, 1, 0, 1],
			[1, 1, 1, 0],
		]
		k_4 = Graph(adjacency_matrix)

		assert k_4.is_planar() is True

	def test_if_k_3_2_is_planar(self):  # K3,2
		adjacency_matrix = [
			[0, 0, 1, 1, 1],
			[0, 0, 1, 1, 1],
			[1, 1, 0, 0, 0],
			[1, 1, 0, 0, 0],
			[1, 1, 0, 0, 0],
		]
		k_3_2 = Graph(adjacency_matrix)

		assert k_3_2.is_planar() is True

	def test_if_k_5_is_planar(self):
		adjacency_matrix = [
			[0, 1, 1, 1, 1],
			[1, 0, 1, 1, 1],
			[1, 1, 0, 1, 1],
			[1, 1, 1, 0, 1],
			[1, 1, 1, 1, 0],
		]
		k_5 = Graph(adjacency_matrix)

		assert k_5.is_planar() is False
