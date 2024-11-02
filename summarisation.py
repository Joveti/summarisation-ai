import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Step 1: Extract Information
def extract_company_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract key details (this will vary based on the structure of the website)
    company_name = soup.find('h1').text
    about_section = soup.find('div', {'id': 'about'}).text
    
    return company_name, about_section

# Step 2: Summarize Information
def generate_summary(text):
    summarizer = pipeline('summarization')
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Step 3: Generate Article
def create_article(url):
    company_name, about_section = extract_company_info(url)
    summary = generate_summary(about_section)
    
    article = f"""
    **Company Overview:**
    {company_name}

    **Summary:**
    {summary}
    """
    return article

# Example usage
url = 'http://example.com'
article = create_article(url)
print(article)
