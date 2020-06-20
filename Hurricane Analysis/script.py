# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def update_list_damages(damages_list):
    for index, damage in enumerate(damages_list):
        if damage.endswith("M"):
            damages_list[index] = float(damage[:-1]) * 1000000
        if damage.endswith("B"):
            damages_list[index] = float(damage[:-1]) * 1000000000


update_list_damages(damages)


# write your construct hurricane dictionary function here:
def generate_dictionary(names_list,
                        months_list,
                        years_list,
                        max_sustained_winds_list,
                        areas_affected_list,
                        damages_list,
                        deaths_list):
    dictionary = {}
    for index in range(len(names_list)):
        dictionary[names_list[index]] = {
            "Name": names_list[index],
            "Month": months_list[index],
            "Year": years_list[index],
            "Max Sustained Wind": max_sustained_winds_list[index],
            "Areas Affected": areas_affected_list[index],
            "Damages": damages_list[index],
            "Deaths": deaths_list[index]
        }
    return dictionary


hurricanes_data = generate_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)


# write your construct hurricane by year dictionary function here:
def set_dictionary_keys_by_year(hurricanes_dictionary):
    new_dictionary = {}
    for key, value in hurricanes_dictionary.items():
        year = hurricanes_dictionary[key]["Year"]
        if not new_dictionary.get(year):
            new_dictionary[year] = [value]
        else:
            new_dictionary[year].append(value)
    return new_dictionary


hurricanes_data_by_years = set_dictionary_keys_by_year(hurricanes_data)


# write your count affected areas function here:
def find_most_affected_area(areas_affected_list):
    affliction_count = {}
    for areas in areas_affected_list:
        for area in areas:
            if affliction_count.get(area):
                affliction_count[area] += 1
                continue
            affliction_count[area] = 1
    most_affected_area = max(affliction_count, key=affliction_count.get)
    return most_affected_area, affliction_count[most_affected_area]


# write your find most affected area function here:
max_area, max_area_count = find_most_affected_area(areas_affected)
print(f"The most affected area is {max_area} with {max_area_count} hurricanes.")


# Find the highest value of a specified category:
def find_highest_number_of(hurricanes_dictionary, category):
    highest_number = 0
    hurricane = str()
    for hurricane_name, hurricane_data in hurricanes_dictionary.items():
        category_count = hurricane_data[category]
        if (isinstance(category_count, float) or isinstance(category_count, int)) and category_count > highest_number:
            highest_number = category_count
            hurricane = hurricane_name
    return hurricane, highest_number


# write your greatest number of deaths function here:
max_mortality_cane, max_mortality = find_highest_number_of(hurricanes_data, "Deaths")
print(f"The deadliest hurricane is {max_mortality_cane} with {max_mortality} deaths.")


# Function to categorize in 5 scales:
def categorize_data_five_scales(hurricanes_dictionary, category, *scales):
    scales_dictionary = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane_data in hurricanes_dictionary.values():
        category_count = hurricane_data[category]
        if isinstance(category_count, float) or isinstance(category_count, int):
            if category_count > scales[4]:
                scales_dictionary[5].append(hurricane_data)
            elif category_count > scales[3]:
                scales_dictionary[4].append(hurricane_data)
            elif category_count > scales[2]:
                scales_dictionary[3].append(hurricane_data)
            elif category_count > scales[1]:
                scales_dictionary[2].append(hurricane_data)
            elif category_count > scales[0]:
                scales_dictionary[1].append(hurricane_data)
            else:
                scales_dictionary[0].append(hurricane_data)
    return scales_dictionary


# write your categorize by mortality function here:
hurricanes_by_mortality = categorize_data_five_scales(hurricanes_data, "Deaths",
                                                      0, 100, 500, 1000, 10000)

# write your greatest damage function here:
max_damage_cane, max_damage = find_highest_number_of(hurricanes_data, "Damages")
print(f"The most expensive hurricane is {max_damage_cane} with {max_damage}$ worth of damages.")

# write your categorize by damage function here:
hurricanes_by_damage = categorize_data_five_scales(hurricanes_data, "Damages",
                                                   0, 100000000, 1000000000, 10000000000, 50000000000)
