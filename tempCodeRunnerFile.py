
import requests
import matplotlib.pyplot as plt

BASE_URL = "https://api.fda.gov/drug/event.json"

fifty_results_url = f"{BASE_URL}?count=patient.drug.drugindication.exact&limit=50"
print(fifty_results_url)

results = requests.get(fifty_results_url).json()["results"]

for result in results:
    print(result.get("term"), result.get("count"))

# --- Visualization: top 15 drug indications ---
top = results[:15][::-1]  # reverse so the largest bar is on top
plt.figure(figsize=(10, 6))
plt.barh([r["term"] for r in top], [r["count"] for r in top])
plt.title("Top 15 Drug Indications in FDA Adverse Event Reports")
plt.xlabel("Number of reports")
plt.tight_layout()
plt.savefig("top_indications.png")
plt.show()
