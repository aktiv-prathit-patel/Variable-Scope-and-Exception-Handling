"""
Data variable for Store all country, state, city data
Perform_operation variable for identify which operation perform

Description : First to ask which operation perform after call that function 
and perform on dictionary data to perform that some operation. operation 
such as create, delete, print, update. on data work on country, State, City
"""
Data = {}
def Create():
    """
    Data variable : In this function to only create data and store in Data Variable
    Country_want, State_Want, City_want: This three variable to use of Country, State, City to want you add or not
    Country_Name, State_Name, City_Name: This Three variable use of new add value in dictionary 

    Description : Create Function to use of create new data. if their data already exist to show msg.
    """
    global Data
    while True:
        Country_Want = input("enter you want country or not, write y/n = ")
        if Country_Want == 'n':
            if not Data:pass
            else:
                print("you created Data: ")
                Print_Data()
            return
        elif Country_Want != 'y':
            print("Unknown Option")
            continue
        else:
             Country_Name = str(input("enter country name: "))
             if Country_Name in Data:
                 print("This name already added please try delete or new country")
                 continue
             Data[Country_Name] = {}
             while True:
                 State_Want = input(f"Enter you want add state in {Country_Name} country or not, write y/n = ")
                 if State_Want == 'n':
                     break
                 elif State_Want != 'y':
                     print("Unknown Option")
                     continue
                 else:
                     State_Name = str(input("Enter State name: "))
                     if State_Name in Data[Country_Name]:
                         print(f"This name already added in {Country_Name} please try delete or update state ")
                         continue
                     Data[Country_Name][State_Name] = []
                     while True:
                         city_want = input(f"enter you want to add city {Country_Name} in {State_Name} city or not, write y/n = ")
                         if city_want == 'n':
                             break
                         elif city_want != 'y':
                             print("Unknown Option")
                             continue
                         else:
                             city_name = str(input("Enter City name: "))
                             if city_name in Data[Country_Name][State_Name]:
                                 print(f"This name already added in {Country_Name} in {State_Name}please try delete or new city")
                                 continue
                             Data[Country_Name][State_Name].append(city_name)

# update uploaded Data file
def Update():
    """
    Which_update : This variable to use of find user which level to change a value.

    Description : Create Function to use of create new data. If their data already exist to show msg.
    """
    def country_Update():
        """
        Data variable : In this function to stored country name update.
        Country_inserted_name: This variable to use of Country name already exist or not
        Country_update_name: This variable use for new Country name to replace exist country

        Description : This Function use for only Country name replace to new Name.
        """
        print(Data.keys())
        country_inserted_name = input("enter which country you make update operation: ")
        if country_inserted_name in Data.keys():
            country_update_name = input("enter new country name: ")
            Data[country_update_name] = Data.pop(country_inserted_name)
            return

    def state_Update():
        """
        Data variable : In this function to stored country name update.
        Country_inserted_name: which country name of state name update.
        State_inserted_name: This variable to use of State name already exist or not.
        State_update_name: This variable use for new State name to replace exist country.

        Description : This Function use for only State name replace to new Name.
        """
        print(Data.keys())
        country_inserted_name = input("enter which country state update ")
        if country_inserted_name in Data.keys():
            print(Data[country_inserted_name].keys())
            state_inserted_name = input("enter which country you make update operation: ")
            if state_inserted_name in Data[country_inserted_name].keys():
                state_update_name = input("enter new state name: ")
                Data[country_inserted_name][state_update_name] = Data[country_inserted_name].pop(state_inserted_name)
                Print_Data()
                return
            else: print(f"{state_inserted_name} is not Data")
        else: print(f"{country_inserted_name} is not Data")

    def city_Update():
        """
        Data variable : In this function to stored country name update.
        Country_inserted_name, State_inserted_name: which country name in state name to update City name.
        City_inserted_name: This variable to use of City name already exist or not.
        City_update_name: This variable use for new City name to replace exist country.

        Description : This Function use for only City name replace to new Name.
        """
        print(Data.keys())
        country_inserted_name = input("enter which country city update ")
        if country_inserted_name in Data.keys():
            print(Data[country_inserted_name].keys())
            state_inserted_name = input("enter which state city update: ")
            if state_inserted_name in Data[country_inserted_name].keys():
                print(Data[country_inserted_name][state_inserted_name])
                city_inserted_name = input("enter which city name you update: ")
                if city_inserted_name in Data[country_inserted_name][state_inserted_name]:
                    city_update_name = input("enter new city name: ")
                    Data[country_inserted_name][state_inserted_name].append(city_update_name)
                    Data[country_inserted_name][state_inserted_name].remove(city_inserted_name)
                else: print('This city in not list')

    while True:
        if not Data:
            print("Data empty, Update not possible")
            return
        try:
            which_Update = int(input("""
change country = 1
change states = 2
change city = 3
exit = 4
enter number which operation perform: """))
            match which_Update:
                case 1:
                    country_Update()
                case 2:
                    state_Update()
                case 3:
                    city_Update()
                case 4:
                    print("updated Data")
                    Print_Data()
                    return
                case _: print("Unknown Option")
        except: print("Unknown Option")


def Delete():
    """
    Which_Delete : This variable to use of find user which level to Delete a value.

    Description : Create Function to use of create new data. If their data already exist to show msg.
    """
    def country_Delete():
        """
        Data variable : In this function to stored country name Delete.
        Country_inserted_name: This variable to use of Country name already exist or not. If exist so delete that full country data.

        Description : This Function use for only Country Data delete.
        """
        print(Data.keys())
        country_inserted_name = input("enter which country you make delete operation: ")
        Data.pop(country_inserted_name) if country_inserted_name in Data.keys() else print(f"{country_inserted_name} not Data ")
        Print_Data()
        return

    def state_Delete():
        """
        Data variable : In this function to stored State name Delete.
        Country_inserted_name: which country name of state name Delete.
        State_inserted_name: This variable to use of State name already exist or not. If exist so delete that full State data.

        Description : This Function use for only State Data delete.

        """
        print(Data.keys())
        country_inserted_name = input("enter which country state delete ")
        if country_inserted_name in Data.keys():
            if not Data[country_inserted_name]: 
                print(f'In {country_inserted_name} not any states')
                return
            else: print(Data[country_inserted_name].keys())
            state_inserted_name = input("enter which country you make delete operation: ")
            if state_inserted_name in Data[country_inserted_name].keys():
                Data[country_inserted_name].pop(state_inserted_name)
                Print_Data()
                return
            else:
                print(f"{state_inserted_name} is not in Data")
        else:
            print(f"{country_inserted_name} is not in Data")

    def city_Delete():
        """
        Data variable : In this function to stored State name Delete.
        Country_inserted_name,State_inserted_name: which country name in state name of city name Delete.
        State_inserted_name: This variable to use of city name already exist or not. If exist so delete that full city data.

        Description : This Function use for only city Data delete.

        """
        print(Data.keys())
        country_inserted_name = input("enter which country city delete: ")
        if country_inserted_name in Data.keys():
            if not Data[country_inserted_name]: 
                print(f'In {country_inserted_name} not any states')
                return  
            else: print(Data[country_inserted_name].keys())
            state_inserted_name = input("enter which state city delete: ")
            if state_inserted_name in Data[country_inserted_name].keys():
                if not Data[country_inserted_name][state_inserted_name]:
                    print(f'In {state_inserted_name} not any City')
                    return
                else: print(Data[country_inserted_name][state_inserted_name])
                city_inserted_name = input("enter which city name you delete: ")
                if city_inserted_name in Data[country_inserted_name][state_inserted_name]:
                    city_update_name = input("enter new city name: ")
                    Data[country_inserted_name][state_inserted_name].append(city_update_name)
                    Data[country_inserted_name][state_inserted_name].remove(city_inserted_name)
                else:
                    print('This city not in Data')
            else: print(f'{state_inserted_name} not found')
        else: print(f'{country_inserted_name} not found')
    while True:
        if not Data:
            print("Data empty, delete not possible")
            return
        try:
            which_Delete = int(input("""
    Delete country = 1
    Delete states = 2
    Delete city = 3
    Exit = 4
    enter number which operation perform: """))
            match which_Delete:
                case 1:
                    country_Delete()
                case 2:
                    state_Delete()
                case 3:
                    city_Delete()
                case 4:
                    print("updated Data")
                    Print_Data()
                    return
                case _:
                    print("Unknown Option")
        except: print("Unknown Option")

def Print_Data():
    """
    Data variable : Data variable to only read and print data.
    Country, State, city: this three variable to use print data.
        
    Description : This Function use for only print exist data.
    """
    global Data
    if not Data:
        print("not created any Data")
        return
    for country in Data:
        print("->",country)
        if Data[country] == "": continue
        for state in Data[country]:
            print(" "*4," - ",state)
            if len(Data[country][state]) == 0: continue
            for city in Data[country][state]:
                print(" " * 8, " - ", city)

while True:
    try:
        Perform_operation = int(input('''
    create = 1
    update = 2
    delete = 3
    print = 4
    exit = 5
    >>> '''))
        match Perform_operation:
            case 1 : Create()
            case 2 : Update()
            case 3 : Delete()
            case 4 : Print_Data()
            case 5 : break
            case _: print("Unknown Option")
    except: print("Unknown Option")