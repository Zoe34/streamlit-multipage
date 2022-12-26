import streamlit as st
from app_pages.multi_page import MultiPage
from app_pages.page_calculator import calculator_body


# instance of MultiPage class
app = MultiPage(app_name = 'Calculator App')
app.add_page("Calculator", calculator_body)

app.run() 