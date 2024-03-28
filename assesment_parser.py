# Program to parse format PnYnMnDTnHnMnS to seconds

def parse_xs_duration_format(duration_str):
    try:
        #variables for counting result
        years = 0
        months = 0
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
        num = ""
        time_character = False
        negative = False

        #deciding if the number is negative
        if duration_str[0] == "-":
            negative = True

        for char in duration_str:
            #if statement to detect numbers and a dot, it adds to num until char is string 
            if char.isdigit() or char == ".":
                num += char
            #if we get any other type then digit most probably string then I set value to num and reset num variable
            else:
                if num:
                    value = float(num)
                else:
                    #if we have just character we assign 0 to value
                    value = 0
                num = ""
                #second set of if statements for deciding on character
                #if character one of YMDTHMS we assign value to it
                #I created time_character boolean to decide if value == Month or value == Minutes
                if char == 'Y':
                    years = value
                elif char == 'M':
                    if time_character:
                        minutes = value
                    else:
                        months = value
                elif char == 'D':
                    days = value
                elif char == 'H':
                    hours = value
                elif char == 'S':
                    seconds = value
                elif char == 'T':
                    time_character = True
        #assuming that year has 365 days and month has 30 days
        total_seconds = years * 31536000 + months * 2592000 + days * 86400 + hours * 3600 + minutes * 60 + seconds
    except Exception as e:
        print(f"There was an error: {e}")
        return None

    if negative:
        return -total_seconds
    else:
        return total_seconds