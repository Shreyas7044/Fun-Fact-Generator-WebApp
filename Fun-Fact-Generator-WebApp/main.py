# Import the necessary modules
import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    # Clear the screen
    clear()

    # Header
    put_html(
        '<p align="left">'
        '<h2>🎉 Fun Fact Generator</h2>'
        '</p>'
    )

    # API URL
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    # GET request
    response = requests.get(url)

    # Convert response to dictionary
    data = json.loads(response.text)

    # Extract fact text
    useless_fact = data['text']

    # Display fact
    style(put_text(useless_fact), 'color:blue; font-size:30px')

    # Button to load next fact
    put_buttons(
        [dict(label='Click me', value='outline-success')],
        onclick=get_fun_fact
    )

# Driver code
if __name__ == '__main__':
    put_html(
        '<p align="left">'
        '<h2>🎉 Fun Fact Generator</h2>'
        '</p>'
    )

    put_buttons(
        [dict(label='Click me', value='outline-success')],
        onclick=get_fun_fact
    )

    hold()
