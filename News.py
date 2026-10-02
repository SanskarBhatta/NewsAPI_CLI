import os
import requests
import argparse
os.system('cls')
url="https://newsapi.org/v2/top-headlines"
parser=argparse.ArgumentParser(description="NewsAPI")
parser.add_argument("--category","-c",type=str.lower,required=True,choices=["sports","business","tech","science","general","entertainment","health","politics"],help="Choose the News U wanna know.")
args=parser.parse_args()
req=requests.get(url, 
                 params={
            "q": args.category,
            "sortBy": "publishedAt",
            "apiKey": "Your API_KEY"
        })
data=req.json()
if data["status"] == "ok":
    print(f"The News U Chose: {args.category}")
    print("="*35)
    print("📰 TOP HEADLINES")
    print("="*35)
    for i,article in enumerate(data["articles"][:3]):
        print(f"{i+1}. {article["title"]}")
        print(f"{'Source':<10}: {article["source"]["name"]}")
        print(f"{'Summary':<10}: {article["description"]}")
        print(f"{'Link':<10}: {article["url"]}")
        print("-"*35)
        print("\n")
else:
    print("Error:", data["message"])
