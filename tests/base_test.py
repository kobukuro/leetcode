import pytest
import multiprocessing


class BaseTestSolution:
    DEFAULT_TIMEOUT = 1  # Default timeout for tests in seconds

    @staticmethod
    def _run_method_in_process(solution, method_name, args, queue):
        """
        Generic wrapper for executing a specified method in a separate process

        Args:
            solution: Instance of the solution class
            method_name: Name of the method to execute
            args: Method arguments as a tuple
            queue: Multiprocessing communication queue
        """
        try:
            method = getattr(solution, method_name)
            result = method(*args)
            queue.put(('success', result))
        except AttributeError:
            queue.put(('error', f"Method '{method_name}' not found in Solution class"))
        except Exception as e:
            queue.put(('error', str(e)))

    @staticmethod
    def _test_with_timeout(solution, method_name, args, expected, timeout):
        """
        Generic timeout test method

        Args:
            solution: Instance of the solution class
            method_name: Name of the method to test
            args: Method arguments as a tuple
            expected: Expected result
            timeout: Timeout in seconds
        """
        queue = multiprocessing.Queue()
        process = multiprocessing.Process(
            target=BaseTestSolution._run_method_in_process,
            args=(solution, method_name, args, queue)
        )

        process.start()
        process.join(timeout=timeout)

        if process.is_alive():
            process.terminate()
            process.join()
            pytest.fail(f"Test exceeded {timeout} second(s) - algorithm needs optimization!")

        if queue.empty():
            pytest.fail("Process ended without result!")

        status, result = queue.get()
        if status == 'error':
            pytest.fail(f"Error in subprocess: {result}")

        assert result == expected, f"Expected {expected}, got {result}"

    def _run_test(self, solution, method_name, args, expected, timeout=None):
        """
        Unified entry point for running tests

        Args:
            solution: Instance of the solution class
            method_name: Name of the method to test
            args: Method arguments as a tuple
            expected: Expected result
            timeout: Timeout in seconds, if None then no timeout is used
        """
        if timeout is None:
            method = getattr(solution, method_name)
            assert method(*args) == expected
        else:
            self._test_with_timeout(solution, method_name, args, expected, timeout)
