import sys
import traceback
import time
def get_exception_info():
    try:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        file_name, line_number, procedure_name, line_code = \
            traceback.extract_tb(exception_traceback)[-1]
        exception_info = ''.join('[Time Stamp]: '
        + str(time.strftime('%d-%m-%Y %I:%M:%S %p'))
        + '\n' + '[File Name]: ' + str(file_name) + '\n'
        + '[Procedure Name]: ' + str(procedure_name) + '\n'
        + '[Error Message]: ' + str(exception_value) + '\n'
        + '[Error Type]: ' + str(exception_type) + '\n'
        + '[Line Number]: ' + str(line_number) + '\n'
        + '[Line Code]: ' + str(line_code))
    except:
        pass
    return exception_info
def division_by_zero():
    try:
        division = 1/0
    except:
        exception_info = get_exception_info()
        print(exception_info)
    finally:
        pass

def main():
    division_by_zero()
if __name__ == '__main__':
    main()