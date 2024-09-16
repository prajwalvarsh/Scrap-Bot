import streamlit as st
from scrape import (scrape_site, 
                    getDriver,
                    extract_body_content,
                    clean_body_content,
                    split_dom_content)
from parse import parse_with_ollama
                    
st.title("Scrape Bot")
url = st.text_input("Enter URL: ")

if st.button("scrape URL"):
    st.write("Scraping URL")
    result = scrape_site()
    # print(result)
    dom_content = getDriver(url,result)
    
    body_content = extract_body_content(dom_content)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

    # Display the DOM content in an expandable text box
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)