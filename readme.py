import textwrap

def format_paper_data(stats):

	papers_text = """
	## Overall statistics 

	Total number of accepted papers: {0:0d}<br/>
	Total number of affiliations: {1:0d}<br/>
	Total number of subjects: {2:0d}<br/>
	Total number of unique abstract words: {3:0d}<br/>

	### Top Authors
	Number of papers in which each individual is listed an author.

	![authors](img/paper_authors.svg) 

	### Top Affiliations
	Number of papers including each affiliation (an author may have multiple affiliations).

	![affiliations](img/paper_affiliations.svg) 

	### Top Subjects
	Total number of papers tagged with one of the provided subjects.

	![subjects](img/paper_subjects.svg) 

	### Top Abstract Words
	Most commonly occurring words within paper abstracts. 

	![authors](img/abstract_words.svg) 
	""".format(stats['papers'], len(stats['affiliations']),
			   len(stats['subjects']), len(stats['words']))

	with open("markdown/papers.md", "w") as papers_fp:
		papers_fp.write(textwrap.dedent(papers_text))

def format_presenter_data(stats):
	presenters_text = """
	## Presenters
	This section outlines statistics about all of the presenters at the convention. It it not limited to just accepted papers.

	Total number of presenters: {0:0d}<br/>
	Total number of affiliations:  {1:0d}<br/>
	Total number of cities: {2:0d}<br/>
	Total number of countries: {3:0d}<br/>

	### Top Affiliations

	![names](img/presenter_names.svg) 

	### Top Cities

	![locations](img/presenter_locations.svg)

	### Top Countries

	![countries](img/presenter_countries.svg)

	## Disclaimer
	These statistics are only estimates. Formatting discrepancies in the scrapped data may skew some of these metrics.  

	""".format(stats['presenters'], len(stats['names']),
			   len(stats['locations']), len(stats['countries']))
	
	with open("markdown/presenters.md", "w") as presenters_fp:
		presenters_fp.write(textwrap.dedent(presenters_text))

def compile_readme():
	# load markdown source files
	with open("markdown/intro.md", "r") as intro_fp:
		intro = intro_fp.read()
	with open("markdown/papers.md", "r") as papers_fp:
		papers = papers_fp.read()
	with open("markdown/presenters.md", "r") as presenters_fp:
		presenters = presenters_fp.read()
	with open("markdown/disclaimer.md", "r") as disclaimer_fp:
		disclaimer = disclaimer_fp.read()

	# load README.md file
	with open("README.md", "w") as readme_fp:
		readme_fp.write(intro)
		readme_fp.write(papers)
		readme_fp.write(disclaimer)
		#readme_fp.write(presenters)