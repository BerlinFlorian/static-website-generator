import re

def extract_markdown_images(text):
    """takes a markdown string and returns a list of tuples, each tuple should contain the alt text and the URL"""
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """takes a markdown string and returns a list of tuples, each tuple should contain the link text and the URL without scrapping images"""
    pattern = r'(?<!\!)\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches

