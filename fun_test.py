from fun import *


class TestPlanarity:
	def test_if_k3_is_planar(self):
		adjacency_matrix = [
			[0, 1, 1],
			[1, 0, 1],
			[1, 1, 0],
		]
		graph = Graph(adjacency_matrix)

		assert graph.is_planar() is True

	def test_if_k4_is_planar(self):
		adjacency_matrix = [
			[0, 1, 1, 1],
			[1, 0, 1, 1],
			[1, 1, 0, 1],
			[1, 1, 1, 0],
		]
		graph = Graph(adjacency_matrix)

		assert graph.is_planar() is True

	def test_if_k3_2_is_planar(self):  # K3,2
		adjacency_matrix = [
			[0, 0, 1, 1, 1],
			[0, 0, 1, 1, 1],
			[1, 1, 0, 0, 0],
			[1, 1, 0, 0, 0],
			[1, 1, 0, 0, 0],
		]
		graph = Graph(adjacency_matrix)

		assert graph.is_planar() is True

	def test_if_k5_is_planar(self):
		adjacency_matrix = [
			[0, 1, 1, 1, 1],
			[1, 0, 1, 1, 1],
			[1, 1, 0, 1, 1],
			[1, 1, 1, 0, 1],
			[1, 1, 1, 1, 0],
		]
		graph = Graph(adjacency_matrix)

		assert graph.is_planar() is False
