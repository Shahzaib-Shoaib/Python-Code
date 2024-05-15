def calculate_density(population, area):
    return population / area

def find_low_density_country(country_data):
    min_density = float('inf')
    low_density_country = None
    for country in country_data:
        density = calculate_density(country[1], country[2])
        if density < min_density:
            min_density = density
            low_density_country = country[0]
    return low_density_country

def main():
    country_data = []
    while True:
        country_name = input("Enter country name (or enter blank to stop): ").strip()
        if country_name == "":
            break
        population = int(input("Enter population: "))
        area = float(input("Enter area (in square km): "))
        country_data.append((country_name, population, area))
    
    total_density = 0
    for country in country_data:
        total_density += calculate_density(country[1], country[2])
    
    average_density = total_density / len(country_data)
    print(f"The average population density is: {average_density:.2f} people per square km")
    
    low_density_country = find_low_density_country(country_data)
    if low_density_country:
        print(f"The country with the lowest population density is: {low_density_country}")
    else:
        print("No country data entered.")

if __name__ == "__main__":
    main()
