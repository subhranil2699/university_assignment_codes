from typing import Dict


str_float_dict = Dict[str, float]

def errors(true_value: float, approx_value: float) -> str_float_dict:
    '''
    Calculate abs error, rel error and percn error upto 4 significant digits 
    '''
    
    absolute_error: float = round(abs(true_value - approx_value), 4)
    relative_error: float = round(absolute_error / true_value, 4)
    percentage_error: str = relative_error * 100
    
    result: str_float_dict =  {
        "absolute_error": absolute_error,
        "relative_error": relative_error,
        "percentage_error": percentage_error
    }

    return result


true_value: float = 36.7458645
approx_value: float = 36.0

calc_errors: str_float_dict = errors(true_value, approx_value)


[print(f"{key} = {value}") for key, value in calc_errors.items()]
    
