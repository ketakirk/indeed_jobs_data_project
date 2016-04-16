import requests
import urllib
from query_params import STATES, INDUSTRIES

url_template = "http://api.indeed.com/ads/apisearch?%s"

CONSTANT_FIELDS = {
    "publisher": "",
    "jt": "fulltime",
    "fromage": "30",
    "v": "2"
}

for state in STATES.keys():
    for industry in INDUSTRIES:
        
        # Create a new instance of CONSTANT_FIELDS
        fields = CONSTANT_FIELDS.copy()


        # Create a dictionary of parameters
        fields.update({
            "q": "data analyst %s" % industry, 
            "l": state
        })

        # Create "&" separated query parameters from the "fields" dictionary
        query_params = urllib.parse.urlencode(fields)
        url = url_template % query_params

        # Query indeed.com API and get response
        response = requests.get(url)

        # Store XML in a file in "indeed_raw_data" folder
        filename = "data/xml/%s_%s_raw_data.xml" % (state, industry)
        with open(filename, "wb") as outfile:
            outfile.write(response.content)

        # Print status message
        print("%s written" % filename)

        
