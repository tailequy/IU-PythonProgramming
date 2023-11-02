import traceback
import sys
def division_by_zero():
    try:
        division_by_zero = 1/0
    except:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        print("Exception Type: {}\nException Value: {}".
              format(exception_type, exception_value))
        file_name, line_number, procedure_name, line_code = \
            traceback.extract_tb(exception_traceback)[-1]
        print("File Name: {}\nLine Number: {}\nProcedure Name: {}\nLine Code:"
              "{}".format(file_name, line_number, procedure_name, line_code))
    finally:
        pass
def main():
    division_by_zero()
if __name__ == '__main__':
    main()