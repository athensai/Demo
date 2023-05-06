import requests
import streamlit as st
from util.util import chat


def fetch_acs_data(state_code, api_key):
    variables = ','.join([
        'NAME',
        'B01001_001E', 'B01001_002E', 'B01001_026E', 'B01001_020E', 'B01001_021E', 'B01001_022E',
        'B01001_023E', 'B01001_024E', 'B01001_025E', 'B01001_044E', 'B01001_045E', 'B01001_046E',
        'B02001_002E', 'B02001_003E', 'B02001_004E', 'B02001_005E', 'B02001_006E', 'B02001_008E',
        'B03001_003E', 'B15003_017E', 'B15003_018E', 'B15003_021E', 'B15003_022E', 'B15003_023E',
        'B15003_024E', 'B19013_001E', 'B19083_001E', 'B23025_002E', 'B23025_004E', 'B23025_005E',
        'B23025_007E', 'B25001_001E', 'B25002_002E', 'B25002_003E', 'B25077_001E', 'B27001_004E', 
        'B27001_007E', 'B11001_001E', 'B11001_002E', 'B11001_007E'
    ])

    acs_url = f'https://api.census.gov/data/2021/acs/acs1?get={variables}&for=state:{state_code}&key={api_key}'
    response = requests.get(acs_url)
    return response.json()

st.title("Census Data by State")

api_key = "87600fbd504102a9bd0e2d5f2176ec4c5613d210"  # Replace with your actual API key

state_fips_codes = {
    'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08', 'CT': '09', 'DE': '10', 'FL': '12',
    'GA': '13', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 'IA': '19', 'KS': '20', 'KY': '21', 'LA': '22',
    'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27', 'MS': '28', 'MO': '29', 'MT': '30', 'NE': '31',
    'NV': '32', 'NH': '33', 'NJ': '34', 'NM': '35', 'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39', 'OK': '40',
    'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45', 'SD': '46', 'TN': '47', 'TX': '48', 'UT': '49', 'VT': '50',
    'VA': '51', 'WA': '53', 'WV': '54', 'WI': '55', 'WY': '56'
}

state = st.selectbox("State", list(state_fips_codes.keys()))

if st.button("Fetch Data"):
    if state:
        try:
            state_code = state_fips_codes[state]
            acs_data = fetch_acs_data(state_code, api_key)
            data = dict(zip(acs_data[0], acs_data[1]))

            st.header("American Community Survey (ACS) Data")
            st.write("State:", data['NAME'])
            
            st.subheader("Population")
            st.write("Total:", data['B01001_001E'])
            st.write("Male:", data['B01001_002E'])
            st.write("Female:", data['B01001_026E'])
            st.write("Age 20-24:", data['B01001_020E'])
            st.write("Age 25-29:", data['B01001_021E'])
            st.write("Age 30-34:", data['B01001_022E'])
            st.write("Age 35-44:", data['B01001_023E'])
            st.write("Age 45-54:", data['B01001_024E'])
            st.write("Age 55-64:", data['B01001_025E'])
            st.write("Age 65-74:", data['B01001_044E'])
            st.write("Age 75-84:", data['B01001_045E'])
            st.write("Age 85 and over:", data['B01001_046E'])

            st.subheader("Race and Ethnicity")
            st.write("White alone:", data['B02001_002E'])
            st.write("Black or African American alone:", data['B02001_003E'])
            st.write("American Indian and Alaska Native alone:", data['B02001_004E'])
            st.write("Asian alone:", data['B02001_005E'])
            st.write("Native Hawaiian and Other Pacific Islander alone:", data['B02001_006E'])
            st.write("Two or more races:", data['B02001_008E'])
            st.write("Hispanic or Latino:", data['B03001_003E'])

            st.subheader("Education")
            st.write("High school graduate:", data['B15003_017E'])
            st.write("Some college, no degree:", data['B15003_018E'])
            st.write("Bachelor's degree:", data['B15003_021E'])
            st.write("Master's degree:", data['B15003_022E'])
            st.write("Professional degree:", data['B15003_023E'])
            st.write("Doctorate degree:", data['B15003_024E'])

            st.subheader("Income")
            st.write("Median household income:", data['B19013_001E'])
            st.write("Gini Index of Income Inequality:", data['B19083_001E'])

            st.subheader("Employment")
            st.write("In labor force:", data['B23025_002E'])
            st.write("Civilian labor force - Employed:", data['B23025_004E'])
            st.write("Civilian labor force - Unemployed:", data['B23025_005E'])
            st.write("Not in labor force:", data['B23025_007E'])

            st.subheader("Housing")
            st.write("Total housing units:", data['B25001_001E'])
            st.write("Occupied housing units:", data['B25002_002E'])
            st.write("Vacant housing units:", data['B25002_003E'])
            st.write("Median value of owner-occupied housing units:", data['B25077_001E'])
            
            st.subheader("Health Insurance")
            st.write("Under 65 years - With health insurance coverage:", data['B27001_004E'])
            st.write("Under 65 years - No health insurance coverage:", data['B27001_007E'])
            
            st.subheader("Household Type")
            st.write("Total households:", data['B11001_001E'])
            st.write("Family households:", data['B11001_002E'])
            st.write("Non-family households:", data['B11001_007E'])
        


        except Exception as e:
            st.error(f"Error fetching data: {e}")
    else:
        st.error("Please select a valid state.")
