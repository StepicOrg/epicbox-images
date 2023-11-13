from process_java import is_java_tests, process_java
from process_python import is_python_tests, process_python
from util import finish_badly, format_exception

if __name__ == '__main__':
    try:
        if is_python_tests():
            process_python()
        elif is_java_tests():
            process_java()
        else:
            finish_badly("Cannot find tests for the task")
    except Exception as ex:
        finish_badly(format_exception(ex))
