
def WeatherData(records):
    City_data = {}
    for record in records:
        City = record.get("City")
        if City not in City_data:
            City_data[City] = {"total_temp":0,"temp_count":0,"total_humidity":0,"humidity_count":0}
        if "temperature" in record:
            City_data[City]["total_temp"] += record["temperature"]
            City_data[City]["temp_count"] += 1

        if "humidity" in record:
            City_data[City]["total_humidity"] += record["humidity"]
            City_data[City]["humidity_count"] += 1
    return {
        City:{
            "average_temperature":(data["total_temp"] / data["temp_count"])
            if data["temp_count"] else None,
            "average_humidity":(data["total_humidity"] / data["humidity_count"])
            if data["humidity_count"] else None
        }
        for City,data in City_data.items()
    }

def main():
    
    records = [
        {"City":"Mohali","temperature":65,"humidity":55},
        {"City":"Mohali","temperature":70},
        {"City":"Nashik","temperature":75,"humidity":35},
        {"City":"Pune","humidity":40},
        {"City":"Mumbai","temperature":60}
    ]
    Result = WeatherData(records)
    print(Result)

if __name__ == "__main__":
    main()