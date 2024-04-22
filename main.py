import streamlit as st
import plotly.express as px
from backend import get_data

# Add title,text input, selectbox, slider and subheader
st.title('Weather forecast for the next days')
place = st.text_input('Place:')
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view',
                            ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')

if place:
    try:
        filtered_data = get_data(place,days)
        # Get Temperature/Sky data
        if option == 'Temperature':
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Days', 'y': 'Temperature(C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[conditions] for conditions in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write('Please enter an existing city name')
