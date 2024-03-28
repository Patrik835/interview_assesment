#I had to create function to check if number is float, isdigit() retuns False on floats
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
#reworked solution with split    
def parse_with_split(duration_str):
    try:
        if duration_str[0] != "P":
            raise ValueError("Error, input must start with P.")
        #date and time factors to calculate final result
        date_factors = [31536000, 2592000, 86400]
        time_factors = [3600, 60, 1]
        # Split the string into date and time components if there is "T"
        if "T" in duration_str:
            date, time = duration_str[1:].split('T')
            #split the date so we get list of 3 values
            split_y = date.split("Y")
            split_mon = split_y[-1].split("M")
            split_d = split_mon[-1].split("D")
            date_list = [split_y[0],split_mon[0], split_d[0]]
            #split the time so we get list of 3 values
            split_h = time.split("H")
            split_min = split_h[-1].split("M")
            split_s = split_min[-1].split("S")
            time_list = [split_h[0],split_min[0], split_s[0]]

            date_count = 0
            #loop trough date list, isdigit() is like a filter for the values,
            #throwing error if month isn't 0
            for index, value in enumerate(date_list):
                if value.isdigit():
                    if date_factors[index] == 2592000 and value !=0 :
                        raise ValueError("Error, month can't be used for this conversion")
                    date_count += date_factors[index] * float(value)

            time_count = 0
            #loop trough time list, isdigit() is like a filter for the values
            for index, value in enumerate(time_list):
                if value.isdigit() or is_float(value):
                    time_count += time_factors[index] * float(value)
            #counting both sides together and returning result
            result = date_count + time_count
            return result
        #if there is no "T" we split just the date side
        else:
            split_y = duration_str[1:].split("Y")
            split_mon = split_y[-1].split("M")
            split_d = split_mon[-1].split("D")
            date_list = [split_y[0],split_mon[0], split_d[0]]

            date_count = 0
            for index, value in enumerate(date_list):
                if value.isdigit():
                    if date_factors[index] == 2592000 and value !=0 :
                        raise ValueError("Error, month can't be used for this conversion")
                    date_count += date_factors[index] * float(value) 
            return date_count
    except ValueError as e:
        return e