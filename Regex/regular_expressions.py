import re

regex_birthday_validation = re.compile(
        r'(3[0-1]|[1-2]\d|0[1-9])/' # day
        r'(0[1-9]|1[0-2])/' # month
        r'(19\d{2}|20\d{2})' # year 
    )

regex_email_validation = re.compile(
        r'^([A-Z0-9]+|[A-Z0-9][A-Z0-9\.-]+[A-Z0-9])' # cannot start with '.' and '-'  
        r'@'
        r'([A-Z0-9]+|[A-Z0-9][A-Z0-9\.-]+[A-Z0-9])' # cannot start with '.' and '-'
        r'(\.[A-Z]{2,6})$', re.IGNORECASE
    )

regex_website_validation = re.compile(
        r'^(https?://)'  # http:// or https:// are necessary
        r'(www\.([A-Z0-9]{1,62}|[A-Z0-9][A-Z0-9\.-]{1,60}[A-Z0-9])\.[A-Z]{2,6}|'  # url comain 
        r'localhost|'  # or a 'localhost' but it will not be necessary here (just for practice)
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # or ip - also not necessary (just for practice)
        r'(?::\d+)?'  # optional port - not necessary (just for practice)
        r'(?:/?|[/?]\S+/?)$', re.IGNORECASE
    )

regex_passport_number_validation = re.compile(
        r'^[A-Z]{2}\s[0-9]\s[0-9]{6}$'
    )

regex_date_validation = re.compile(
        r'(3[0-1]|[1-2]\d|0[1-9])/' # day
        r'(0[1-9]|1[0-2])/' # month
        r'(19\d{2}|20\d{2})' # year 
    )

regex_string_value = re.compile(
    r'^([A-Z][a-z]{1,30})|([A-Z][a-z]*-[a-z]+)$'
)