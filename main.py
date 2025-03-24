
import data_manager
dataman = data_manager.DataManager()
sheet_data = dataman.data
cities = []
if sheet_data[0]['iataCode'] == '':
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    print(f'sheet_data:\n{sheet_data}')