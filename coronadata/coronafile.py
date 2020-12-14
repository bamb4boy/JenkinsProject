import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--Country', action='store', dest='country', help='Country Name', required=True)


results = parser.parse_args()

#the url that sends us the json file
url = "https://covid-19-data.p.rapidapi.com/country"

#the parameter that is looked for in the request
querystring = {"name": results.country}

#rapid api stuff - user specific for gleb tyunikov
headers = {
            'x-rapidapi-key': "085d5aa778mshf5300ac0b49235cp1c5691jsne16c836d25ff",
                'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
                }

#the data saved from the requests
response = requests.request("GET", url, headers=headers, params=querystring)
#print(str(response.text))
try:
        response = response.json()
        response = response[0]

        country = response['country']
        confirmed = response['confirmed']
        recovered = response['recovered']
        deaths = response['deaths']

        print(str("In " + str(country)))
        print(str("The number of confirmed cases is: " + str(confirmed)))
        print(str("The number of recovered cases is: " + str(recovered)))
        print(str("The number of deaths is: " + str(deaths)))
except Exception as ex:
        print(ex)
        print("ValueError - text entered is not a country, please check your spelling or provide an existing country name")

            #except Exception as ex:
            #    print(ex)
            #    print("Stock symbol does not exist")
