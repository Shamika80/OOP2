def main():
    buildings = [
        "Building"("City Hall", 8),
        "Building"("Community Center", 3),
        "Building"("Skyscraper", 50)
    ]

    for building in buildings:
        building.save_to_file()

    buildings.clear()

    with open("buildings.csv", 'r', newline='') as file:
        reader = "csv.reader"(file)
        for row in reader:
            if row:
             buildings.append("Building"(row[0], int(row[1])))

    print("Loaded Buildings:")
    for building in buildings:
        print(f"- {building.name} ({building.floors} floors)")

if __name__ == "__main__":
    main()