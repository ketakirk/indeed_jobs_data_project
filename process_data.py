from query_params import STATES, INDUSTRIES
import re


with open("data/csv/jobs_by_state_and_industry.csv", "w") as outfile:
	for state in STATES:
		for industry in INDUSTRIES:
			filename = "data/xml/%s_%s_raw_data.xml" % (state, industry)
			with open(filename) as df:
				file_contents = df.read()
				pattern = "<totalresults>([0-9]+)</totalresults>"
				total_jobs = re.findall(pattern, file_contents)[0]
				line = "%s,%s,%s\n" %(state, industry, total_jobs)
				outfile.write(line)
	