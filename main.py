import requests as rqs
import sys

def get_request(url):
  try:
      result = rqs.get("https://" + url)
      if(result):
        print("[+] Subdomain Discovered ----> " + url)
      except:
        pass
def main():
  target_url = sys.argv[1]
  with open("subdmainwordlist.txt","r") as wordlist:
    for line in wordlist:
      word = line.strip()
      test_url = word + "." + target_url
      get_request(test_url)
main()
