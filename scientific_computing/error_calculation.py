from typing import Dict

str_float_dict = Dict[str, float]


def errors(true_value: float,
           approx_value: float,
           round_digit: int) -> str_float_dict:
    '''
    Calculate abs error, rel error and percn error upto 4 significant digits 
    '''
    
    absolute_error: float = round(abs(true_value - approx_value), round_digit)
    relative_error: float = round(absolute_error / true_value, round_digit)
    percentage_error: float = round(relative_error * 100, round_digit)
    
    result: str_float_dict =  {
        "absolute_error": absolute_error,
        "relative_error": relative_error,
        "percentage_error": percentage_error
    }

    return result



if __name__ == "__main__":
    true_value: float = float(input("True value: "))
    approx_value: float = float(input("Apprx value: "))
    round_digit: int = int(input("Rounding digit: ")) 

    calc_errors: str_float_dict = errors(true_value, approx_value, round_digit)

    [print(f"{key} = {value}") for key, value in calc_errors.items()]
    
