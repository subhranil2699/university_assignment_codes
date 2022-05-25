from typing import Dict


str_float_dict = Dict[str, float]

def errors(true_value: float, approx_value: float, round_: int) -> str_float_dict:
    '''
    Calculate abs error, rel error and percn error upto 4 significant digits 
    '''
    
    absolute_error: float = round(abs(true_value - approx_value), round_)
    relative_error: float = round(absolute_error / true_value, round_)
    percentage_error: str = round(relative_error * 100, round_)
    
    result: str_float_dict =  {
        "absolute_error": absolute_error,
        "relative_error": relative_error,
        "percentage_error": percentage_error
    }

    return result


true_value: float = float(input("True value: "))
approx_value: float = float(input("Appx. value: "))
round_ : int = int(input("Round: "))

calc_errors: str_float_dict = errors(true_value, approx_value, round_)


[print(f"{key} = {value}") for key, value in calc_errors.items()]
