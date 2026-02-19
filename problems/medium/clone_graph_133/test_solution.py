from .solution import Node, Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def _verify_deep_copy(self, original, clone):
        """Verify that clone is a deep copy of original"""
        if original is None:
            assert clone is None
            return

        visited_orig = set()
        visited_clone = set()

        def verify_nodes(orig, cln):
            # Different objects, same values
            assert orig is not cln
            assert orig.val == cln.val
            assert len(orig.neighbors) == len(cln.neighbors)

            # Avoid infinite loops
            if orig in visited_orig:
                # If we've seen this original node, we should have seen the clone too
                assert cln in visited_clone
                return
            visited_orig.add(orig)
            visited_clone.add(cln)

            # Recursively verify each neighbor
            for i, orig_neighbor in enumerate(orig.neighbors):
                clone_neighbor = cln.neighbors[i]
                assert orig_neighbor.val == clone_neighbor.val
                verify_nodes(orig_neighbor, clone_neighbor)

        verify_nodes(original, clone)

    def test_example_1(self):
        # adjList = [[2,4],[1,3],[2,4],[1,3]]
        # 1 ↔ 2, 1 ↔ 4, 2 ↔ 3, 3 ↔ 4
        node1 = Node(val=1)
        node2 = Node(val=2)
        node3 = Node(val=3)
        node4 = Node(val=4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        clone = self.solution.clone_graph(node1)

        # Verify structure
        assert clone.val == 1
        assert len(clone.neighbors) == 2
        assert clone.neighbors[0].val == 2
        assert clone.neighbors[1].val == 4
        assert len(clone.neighbors[0].neighbors) == 2
        assert clone.neighbors[0].neighbors[1].val == 3

        # Verify deep copy
        assert clone is not node1
        self._verify_deep_copy(node1, clone)

    def test_example_2(self):
        # adjList = [[]]
        node1 = Node(val=1)

        clone = self.solution.clone_graph(node1)

        # Verify structure
        assert clone.val == 1
        assert len(clone.neighbors) == 0

        # Verify deep copy
        assert clone is not node1

    def test_example_3(self):
        # adjList = []
        clone = self.solution.clone_graph(None)
        assert clone is None
