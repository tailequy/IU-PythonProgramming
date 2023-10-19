'''
Logging is an excellent programming tool for debugging and auditing your program. By
logging data in the necessary places, you can debug errors easily and use it to analyze program
performance for futures updates. In general, the data is logged in text file(s) and/or
in database table(s). To log data in Python, we use the built-in logging module with the
“import logging” statement.
The log messages have five levels of event severity:
• DEBUG — This is used to log messages during programming debugging. It is very often
applied in order to see returner values of variables and functions.
• INFO — This is used to log any information messages during program running.
• WARNING — This is used to log warning messages. It is very often applied in order to see
preventing information that may have occurred during program running.
• ERROR — This is used to log error messages that occurred during program running. In
general, these messages include specific error information, error line of code, date and
time that the error occurred, function and module file names where the error occurred,
etc.
• CRITICAL — This is used to log critical errors. It is very often applied in order to see
generic program crashes.

'''
import logging
def main():
    logging.basicConfig(filename="app.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s")
    logging.warning("This message gets logged as warning.")
if __name__ == '__main__':
    main()