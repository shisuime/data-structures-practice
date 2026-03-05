dataArray = [
    {"date": "Jan 1", "temperature": 27},
    {"date": "Jan 2", "temperature": 31},
    {"date": "Jan 3", "temperature": 23},
    {"date": "Jan 4", "temperature": 34},
    {"date": "Jan 5", "temperature": 37},
    {"date": "Jan 6", "temperature": 38},
    {"date": "Jan 7", "temperature": 29},
    {"date": "Jan 8", "temperature": 30},
    {"date": "Jan 9", "temperature": 35},
    {"date": "Jan 10", "temperature": 30}
]

class HashMap:
    def __init__(self):
        pass

    def getAverage(self,dataArray,rangeStart,rangeEnd):

        temps=[]

        for item in dataArray[rangeStart:rangeEnd]:
            temps.append(item["temperature"])

        return sum(temps)/len(temps)    
    
    def getMax(self,dataArray):

        temps=[]

        for item in dataArray:
            temps.append(item["temperature"])
        return max(temps)
    


if __name__ == '__main__':
    hash=HashMap()

    # print(hash.getAverage(dataArray,0,7))
    # print(hash.getMax(dataArray))
