country_data = []

while True:
    country_name = input("Enter Country Name: ").strip()
    if country_name == "":
        break
    else:
        population = int(input("Enter Country's Population: "))
        area = int(input("Enter Country's Area: "))
        density = population / area
        country_data.append((country_name, population, area, density))

if len(country_data) > 0:
    total_density = sum(country[3] for country in country_data)
    average_density = total_density / len(country_data)
    print("Average population density:", average_density)

    min_density_country = min(country_data, key=lambda x: x[3])
    print("The country with the minimum population density is:", min_density_country[0])
else:
    print("No country data entered.")


