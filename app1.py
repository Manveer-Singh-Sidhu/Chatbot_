Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import streamlit as st
... from ai21 import AI21Client
... from ai21.models.chat import ChatMessage
... # # New Section
... 
... client = AI21Client(api_key="atCFs8nr2hoZ3b6RG9tHa5bs0ZGcWqXR")
... def func1(user_query):
...   messages = [
...         ChatMessage(
...             role="user",
...             content=user_query
...         )
...     ]
...   response = client.chat.completions.create(
...         model="jamba-instruct-preview",
...         messages=messages,
...         top_p=1.0 # Setting to 1 encourages different responses each call.
...     )
...   return response
...  
... Content = CaptureResponse.choices[0].message.content
... 
... user_query = st.text_input("Ask me anything")
... 
... def_func1(user_query)
... 
... st.write(Content)
