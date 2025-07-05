import pytest
import multiprocessing
from .solution import Solution


class TestSolution:
    solution = Solution()

    def test_climb_stairs_memoization_parameter_2(self):
        assert self.solution.climb_stairs_memoization(2) == 2

    def test_climb_stairs_memoization_parameter_3(self):
        assert self.solution.climb_stairs_memoization(3) == 3

    def test_climb_stairs_memoization_parameter_38(self):
        """Test parameter 38 with timeout using multiprocessing"""
        TestSolution._test_climb_stairs_with_timeout(38, 'climb_stairs_memoization', 63245986, 0.3)

    def test_climb_stairs_dp_parameter_2(self):
        assert self.solution.climb_stairs_dp(2) == 2

    def test_climb_stairs_dp_parameter_3(self):
        assert self.solution.climb_stairs_dp(3) == 3

    def test_climb_stairs_dp_parameter_38(self):
        """Test parameter 38 with timeout using multiprocessing"""
        TestSolution._test_climb_stairs_with_timeout(38, 'climb_stairs_dp', 63245986, 0.3)

    @staticmethod
    def _run_climb_stairs(solution, n, method_name, queue):
        """
        Generic wrapper for executing climb stairs functions

        Args:
            solution: Solution instance
            n: Number of stairs
            method_name: Method name to execute (e.g., 'climb_stairs_memoization', 'climb_stairs_dp')
            queue: Multiprocessing communication queue
        """
        try:
            # Use getattr to dynamically get the method
            method = getattr(solution, method_name)
            result = method(n)
            queue.put(('success', result))
        except AttributeError:
            queue.put(('error', f"Method '{method_name}' not found in Solution class"))
        except Exception as e:
            queue.put(('error', str(e)))

    @staticmethod
    def _test_climb_stairs_with_timeout(n, method_name, expected, timeout):
        """
        Generic timeout test method

        Args:
            n: Number of stairs
            method_name: Method name to test
            expected: Expected result
            timeout: Timeout in seconds
        """
        queue = multiprocessing.Queue()
        process = multiprocessing.Process(
            target=TestSolution._run_climb_stairs,
            args=(TestSolution.solution, n, method_name, queue)
        )

        process.start()
        process.join(timeout=timeout)

        if process.is_alive():
            process.terminate()
            process.join()
            pytest.fail(f"Test exceeded {timeout} second - algorithm needs optimization!")

        if queue.empty():
            pytest.fail("Process ended without result!")

        status, result = queue.get()
        if status == 'error':
            pytest.fail(f"Error in subprocess: {result}")

        assert result == expected, f"Expected {expected}, got {result}"
