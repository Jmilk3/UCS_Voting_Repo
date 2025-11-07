# A file which contains dictionaries mapping NC race and ethnicity codes to the actual values
"""
/* ****************************************************************************
Race codes
race               description
*******************************************************************************
A                  ASIAN
B                  BLACK or AFRICAN AMERICAN
I                  AMERICAN INDIAN or ALASKA NATIVE
M                  TWO or MORE RACES 
O                  OTHER
P                  NATIVE HAWAIIAN or PACIFIC ISLANDER
U                  UNDESIGNATED
W                  WHITE
**************************************************************************** */


/* ****************************************************************************
Ethnic codes
ethnicity          description
*******************************************************************************
HL                 HISPANIC or LATINO
NL                 NOT HISPANIC or NOT LATINO
UN                 UNDESIGNATED
**************************************************************************** */
"""

race_codes = {"A": "Asian", "B":"Black", "I": "Native American", "M": "Two or more races", "O": "Other",
               "P": "Native Hawaiian or Pacific Islander", "U": "Undesignated", "W": "White"}
ethnic_codes = {"HL": "Hispanic", "NL": "Not Hispanic", "UN": "Undesignated"}