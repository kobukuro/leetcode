# Hash Table, String, Design
class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.journey_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in[id]
        del self.check_in[id]
        if (start_station, stationName) not in self.journey_data:
            self.journey_data[(start_station, stationName)] = [(t - start_time), 1]
        else:
            self.journey_data[(start_station, stationName)][0] += (t - start_time)
            self.journey_data[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        data = self.journey_data[(startStation, endStation)]
        return data[0] / data[1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
