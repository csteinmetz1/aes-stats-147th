import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def clean_presenters_list(presenters):
    for p_idx, presenter in enumerate(presenters):
        for n_idx, name in enumerate(presenter['affiliation_names']):
            if   name == "Queen Mary University London":
                presenters[p_idx]['affiliation_names'][n_idx] = "Queen Mary University of London"
            elif name == "Centre for Digital Music (C4DM)":
                presenters[p_idx]['affiliation_names'][n_idx] = "Queen Mary University of London"
            elif name == "Dolby Laboratories":
                presenters[p_idx]['affiliation_names'][n_idx] = "Dolby Laboratories, Inc."
            elif name == "Meyer Sound Labs" or name == "Meyer Sound":
                presenters[p_idx]['affiliation_names'][n_idx] = "Meyer Sound Laboratories"
            elif name == "BBC R&D":
                 presenters[p_idx]['affiliation_names'][n_idx] = "BBC Research and Development"
            elif name == "The Centre for Interdisciplinary Research in Music Media and Technology":
                presenters[p_idx]['affiliation_names'][n_idx] = "Centre for Interdisciplinary Research in Music Media and Technology"
    
        for l_idx, location in enumerate(presenter['affiliation_locations']):
            country = location.split(',')[-1].strip()
            if   country == "NY USA":
                presenters[p_idx]['affiliation_locations'][l_idx] = "USA"
            elif country == "CA USA":
                presenters[p_idx]['affiliation_locations'][l_idx] = "USA"

    return presenters

def clean_affiliation(affiliation):
    if   affiliation == "Queen Mary University London":
        affiliation = "Queen Mary University of London"
    elif affiliation == "Centre for Digital Music (C4DM)":
        affiliation = "Queen Mary University of London"
    elif affiliation == "Dolby Laboratories":
        affiliation = "Dolby Laboratories, Inc."
    elif affiliation == "Meyer Sound Labs" or affiliation == "Meyer Sound":
        affiliation = "Meyer Sound Laboratories"
    elif affiliation == "BBC R&D":
        affiliation = "BBC Research and Development"
    elif affiliation == "The Centre for Interdisciplinary Research in Music Media and Technology":
        affiliation = "Centre for Interdisciplinary Research in Music Media and Technology"\
                
    return affiliation

# words is a string of words
def remove_stopwords(words):
    my_stop_words = ["’", 'paper', 'using', 'used', 'based', 'different']
    stop_words = set(stopwords.words('english') + list(string.punctuation) + my_stop_words) 
    word_tokens = word_tokenize(words) 
    
    filtered_words = []

    for w in word_tokens: 
        if w not in stop_words: 
            filtered_words.append(w) 

    return filtered_words