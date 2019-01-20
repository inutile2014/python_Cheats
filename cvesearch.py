import urllib
import requests
import json

    #with urllib.request.urlopen("https://cve.circl.lu/api/search/servicenow") as url:
    #    get = json.loads(url.read().decode())
        #print(get["data"][0]["cwe"])
        #  if data in theJSON["data"]:


    #defin function for json get_data
def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  # Sort json output
  print (json.dumps(theJSON, indent=4, sort_keys=True))


    #print ("--------------\n")

def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "https://cve.circl.lu/api/search/servicenow"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("Connection works result code: " + str(webUrl.getcode()))
  print ("--------------\n")
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

if __name__ == "__main__":
  main()
