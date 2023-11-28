class Graph:
	def __init__(self, adjacency_matrix: list[list[int]]) -> None:
		self._adjacency_matrix = adjacency_matrix

	def is_planar(self) -> bool:
		v = self._count_vertices()
		e = self._count_edges()
		return e <= 3 * v - 6

	def _count_vertices(self) -> int:
		return len(self._adjacency_matrix)

	def _count_edges(self) -> int:
		return sum(sum(row) for row in self._adjacency_matrix) / 2
