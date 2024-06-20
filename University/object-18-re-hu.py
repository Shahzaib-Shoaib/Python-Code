data = []

while True:
    a = input("Enter Country Name: ").strip()
    if a == "":
        break
    else:
        population = int(input("Enter Country's Population: "))
        area = int(input("Enter Country's Area: "))
        density = population / area
        data.append((a, population, area, density))

if len(data) > 0:
    total_density = sum(country[3] for country in data)
    average_density = total_density / len(data)
    print("Average population density:", average_density)

    min_density_country = min(data, key=lambda x: x[3])
    print("The country with the minimum population density is:", min_density_country[0])
else:
    print("No country data entered.")


