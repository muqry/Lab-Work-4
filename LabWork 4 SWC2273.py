"""
    Program Purpose: to analyze flower sales data for a shop. It calculates various metrics like total units sold,
                    identifies the flower with the highest sales, finds flowers with above-average customer reviews,
                    calculates the average customer review score, and pinpoints flowers with below-average sales.
                    The program also validates input data to ensure accuracy and provides user-friendly error messages
                    in case of invalid entries.
    Programmer: Muhammad Muqry Bin Razaly
    Date 8 March 2024
"""

def analyze_flower_sales(product_names, units_sold, customer_reviews):

  # Input validation
  if len(product_names) != len(units_sold) != len(customer_reviews):
    print("Error: Unequal list lengths for product names, units sold, and reviews.")
    return
  for review in customer_reviews:
    if review < 0 or review > 5:
      print("Error: Customer reviews must be between 0 and 5.")
      return

  # 1. Total Units Sold
  total_units = sum(units_sold)
  print(f"Total units sold: {total_units}")

  # 2. Highest Sales
  highest_sales_index = units_sold.index(max(units_sold))
  highest_sales_product = product_names[highest_sales_index]
  highest_sales_value = units_sold[highest_sales_index]
  print(f"Flower with highest sales: {highest_sales_product} ({highest_sales_value} units)")

  # 3. Above-Average Customer Reviews
  above_average_reviews = []
  for i in range(len(product_names)):
    if customer_reviews[i] > 3:
      above_average_reviews.append((product_names[i], customer_reviews[i]))
  if above_average_reviews:
    print("Flowers with above-average customer reviews (above 3):")
    for product, review in above_average_reviews:
      print(f"- {product} ({review})")
  else:
    print("No flowers have above-average customer reviews.")



  # 4. Average Customer Review Score
  def average(numbers):
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers)
  average_review = average(customer_reviews)
  print(f"Average customer review score: {average_review:.2f}")

  # 5. Below-Average Sales
  # Identify flowers with reviews below 3
  below_average_sales = []
  for i in range(len(product_names)):
      if customer_reviews[i] < 3:
          below_average_sales.append((product_names[i], units_sold[i], customer_reviews[i]))

  if below_average_sales:  # Corrected indentation
      print("Flowers with customer reviews below 3:")
      for product, units, review in below_average_sales:
          print(f"- {product} ({units} units, {review} review)")
  else:
      print("No flowers have customer reviews below 3.")


# Sample dataset
product_names = [
    "Rose", "Lily", "Orchid", "Tulip", "Daisy", "Sunflower",
    "Hydrangea", "Carnation", "Freesia", "Hyacinth", "Iris",
    "Peony", "Dahlia", "Poppy", "Aster", "Zinnia",
    "Gerbera Daisy", "Lily of the Valley", "Gladiolus", "Alstroemeria"
]

units_sold = [
    250, 180, 120, 100, 75, 55,
    150, 200, 80, 110, 90,
    95, 130, 70, 140, 105,
    60, 40, 80, 70
]

customer_reviews = [
    4.8, 4.2, 3.9, 4.5, 3.3, 2.2,
    2.0, 4.7, 4.2, 3.8, 4.5,
    4.3, 4.1, 3.5, 4.8, 4.0,
    4.4, 4.9, 2.9, 4.2
]

analyze_flower_sales(product_names, units_sold, customer_reviews)
