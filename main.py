#  define the function
def heating_cooling(actual_temp:int, desired_temp:int) -> str:
    if desired_temp > actual_temp:
        return 'Run heat'
    elif actual_temp > desired_temp:
        return  'Run A/C'
    else:
        return 'Standby'

#  Bonus: unit conversion
def convert_temp(temp_celsius:int, target_unit:str) -> int:
    match target_unit:
        case 'C':
            return temp_celsius
        case 'K':
            return temp_celsius - 273
        case 'F':
            return (temp_celsius * 9 / 5) + 32

desired_temp = int(input('What is the desired temperature in Celsius? '))
current_temp = int(input('What is the current temperature in Celsius? '))

print(f'Current Temp: {convert_temp(current_temp, "C")} C, {convert_temp(current_temp, "K")} K, {convert_temp(current_temp, "F")} F, ')
print(f'Desired Temp: {convert_temp(desired_temp, "C")} C, {convert_temp(desired_temp, "K")} K, {convert_temp(desired_temp, "F")} F, ')
print(heating_cooling(int(current_temp), int(desired_temp)))
