from .solution import ParkingSystem


class TestSolution:

    def call(self, methods, params, expected):
        results = []
        obj = None
        for method, param in zip(methods, params):
            if method == "ParkingSystem":
                obj = ParkingSystem(*param)
                results.append(None)
            else:
                result = getattr(obj, method)(*param)
                results.append(result)
        assert results == expected

    def test_example_1(self):
        """
        Example 1:
        Input: ["ParkingSystem", "add_car", "add_car", "add_car", "add_car"]
               [[1, 1, 0], [1], [2], [3], [1]]
        Output: [null, true, true, false, false]

        Explanation:
        ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
        parkingSystem.add_car(1); // return true because there is 1 available slot for a big car
        parkingSystem.add_car(2); // return true because there is 1 available slot for a medium car
        parkingSystem.add_car(3); // return false because there is no available slot for a small car
        parkingSystem.add_car(1); // return false because there is no available slot for a big car. It is already occupied.
        """
        self.call(
            ["ParkingSystem", "add_car", "add_car", "add_car", "add_car"],
            [[1, 1, 0], [1], [2], [3], [1]],
            [None, True, True, False, False],
        )
