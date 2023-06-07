import os
from os.path import exists
import csv

def read_ramen_practice(filename):
    results = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.readlines()
            for line in content[1:]:
                split_line = line.split(',')
                try:
                    if float(split_line[5]) >= 0:
                        results.append(split_line)
                except ValueError:
                    print(f"Could not convert '{split_line[5]}' to a number")
                except IndexError:
                    print("Index out of range")
    return results

def write_to_ramen(filename):
    results = read_ramen_practice(filename)
    unique_results = set()
    for res in results:
        unique_results.add(res[1])
    with open("ramen_recs.csv", 'w') as file:
        writer = csv.writer(file)
        for res in unique_results:
            writer.writerow([res])
    print(results)

write_to_ramen('ramen-ratings.csv')

def review_for_brand(filename, brand):
    all_results = read_ramen_practice(filename)
    brand_results = []
    for res in all_results:
        if res[1] == brand:
            brand_results.append(res)
    with open("brand_reviews.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(brand_results)
    
    return brand_results

#review_for_brand("ramen-ratings.csv", "Nissin")


def brand_average(filename, brand):
    all_brand_reviews = review_for_brand(filename, brand)
    brand_ratings = 0
    for rev in all_brand_reviews:
        brand_ratings += float(rev[5])
    result = brand_ratings / len(all_brand_reviews)
    print(result)

brand_average("ramen-ratings.csv", "Nissin")

def get_country_data(filename, country):
    results = read_ramen_practice(filename)
    with open(f"{country}.csv", "w") as file:
        writer = csv.writer(file)
        for res in results:
            if res[4] == country:
                writer.writerow(res)
    return None
        
get_country_data("ramen-ratings.csv", "Japan")