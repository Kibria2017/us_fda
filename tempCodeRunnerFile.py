### question 1: top 50 drug indications
import requests

BASE_URL = "https://api.fda.gov/drug/event.json"

fifty_results_url = f"{BASE_URL}?count=patient.drug.drugindication.exact&limit=50"
print(fifty_results_url)

fifty_results = requests.get(fifty_results_url)

for result in fifty_results.json()["results"]:
    print(result.get("term"), result.get("count"))