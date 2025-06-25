import streamlit as st
import webbrowser
import threading
# URL of a site you can use for Selenium POM automation
url = "https://practicetestautomation.com/practice-test-login/"


# Automatically open the POM login page in your browser
def open_browser():
    webbrowser.open_new(url)


threading.Timer(1, open_browser).start()

# Streamlit App UI
st.title("POM Test Automation Launcher")
st.write(f"🔐 Opening login automation page: [Login Page]({url})")
