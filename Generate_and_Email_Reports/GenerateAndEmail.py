#!/usr/bin/env python3
import json
import locale
import mimetypes
import os.path
import sys
import reports
import emails


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data



def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])

def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def process_data(data):
  """Analyzes the data, looking for maximums.

 Returns a list of lines that summarize the information.
 """
  locale.setlocale(locale.LC_ALL, 'C.UTF-8')
  max_sales = {"total_sales": 0, "car":""}
  max_revenue = {"revenue": 0}
#  best_car={"year":0, "sales":0}
  best_car={}
  for item in data:
    # We need to convert "$1234.56" into 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
#TODO1
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales["total_sales"] = item["total_sales"]
      max_sales["car"] = item["car"]

#TODO2
#    best_car["year"]=item["car"]["car_year"]
#    best_car["sales"]=item["total_sales"]
#    initial_best_car=(0,0)
#    for year , sales in best_car.items():
#      if sales > initial_best_car[1]:
#        max_best_car=(year,sales)

    best_car[item["car"]["car_year"]] = best_car.get(item["car"]["car_year"],0)+ item["total_sales"]
  best_car_sorted = sorted(best_car.items(), key=lambda a: a[1], reverse=True)

  summary=[]
  summary.append("The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]))
#TODO1
  summary.append("The {} had the most sales: {}".format(format_car(
       max_sales['car']), max_sales['total_sales']))
#TODO2
  summary.append("The most popular year was {} with {} sales.".format
       (best_car_sorted[0][0], best_car_sorted[0][1]))
  return summary




def main(argv):
    data = load_data("/home/student-04-8004cef6e6d2/car_sales.json")
    summary = process_data(data)
    print(summary)
# TODO: turn this into a PDF report
    car_data = cars_dict_to_table(data)
    reports.generate("/tmp/cars.pdf", "Sales summary for last month", "<br/>".join(summary), car_data)

# TODO: send the PDF report as an email attachment
    message = emails.generate("automation@example.com", "student-04-8004cef6e6d2@example.com", "Sales summary for last month", "\n".join(summary), "/tmp/cars.pdf")
    emails.send(message)


if __name__ == "__main__":
  main(sys.argv)
