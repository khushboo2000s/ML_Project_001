import os
import sys

class HousingException(Exception):
    
    def __init__(self,error_message:Exception , error_detail:sys):
        super().__init__(error_message)  #passing error_message to Exception class

        self.error_message=error_message


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:  #type of return message is string
        """"
        error_message: Exception object
        error_detail: object of sys module
        """

        _,_ ,exec_tb = error_detail.exc_info()

        line_number = exec_tb.tb_frame.f_lineno  #extracting the line number which causing the error
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error_message: [{error_message}]"

        return error_message
    

    def __str__(self):
        return self.error_message
    

    def __repr__(self) -> str:
        return HousingException.__name__.str()
    


    
        


