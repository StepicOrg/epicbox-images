import json

TASK_ROOT = '/checker/sandbox/'

# Jest uses custom formatting:
# an actual feedback is between the following strings
FAILED_TEST_BEGIN = 'Error: Failed: "'
FAILED_TEST_END = '"\n    at Env.fail'

COMPILATION_ERROR_BEGIN = 'SyntaxError:'
COMPILATION_ERROR_END = '    at '  # start of the stacktrace
MODULE_ERROR_BEGIN = 'ERROR in'

COMPILATION_ERROR_TEXT = 'Compilation error during testing\n\n'
UNEXPECTED_ERROR_TEXT = 'Unexpected error during testing\n\n'

if __name__ == '__main__':
    score = 1
    feedback = ''

    code = open('code.txt', encoding="utf-8").read().strip()
    stdout = open('stdout.txt', encoding="utf-8").read()
    stderr = open('stderr.txt', encoding="utf-8").read()

    fatal_feedback = (
        'Cannot check the submission.\n\nPerhaps your program '
        'has fallen into an infinite loop or created too many objects in memory. '
        'If you are sure that this is not the case, please send the report to support@hyperskill.org\n'
        'stdout:\n{stdout}\n\nstderr:\n{stderr}'
        .format(stdout=stdout, stderr=stderr)
    )

    try:
        stdout_json = json.loads(stdout)
    except:
        code = '-1'

    # 0 is accepted, 1 is wrong answer
    if code != '0' and code != '1':
        score = 0
        feedback = fatal_feedback

    elif code == '0':
        pass

    else:
        score = 0
        try:
            error_message = stdout_json["testResults"][0]["assertionResults"][0]["failureMessages"][
                0]

            if error_message.startswith(FAILED_TEST_BEGIN) and FAILED_TEST_END in error_message:
                start = len(FAILED_TEST_BEGIN)
                end = error_message.index(FAILED_TEST_END)
                error_message = error_message[start: end]

                # Jest escapes " characters in the actual feedback
                # because it presents an actual feedback as a string inside string
                error_message = error_message.replace(r'\"', '"')
                lines = error_message.split('\n')

                # Syntax errors (during compilation)
                if any(l.startswith(COMPILATION_ERROR_BEGIN) for l in lines):
                    start = min(i for i, l in enumerate(lines)
                                if l.startswith(COMPILATION_ERROR_BEGIN))
                    end = min(i for i, l in enumerate(lines)
                              if l.startswith(COMPILATION_ERROR_END))
                    error_message = COMPILATION_ERROR_TEXT + '\n'.join(lines[start: end])

                # Module not found errors (during compilation)
                elif any(l.startswith(MODULE_ERROR_BEGIN) for l in lines):
                    start = min(i for i, l in enumerate(lines)
                                if l.startswith(MODULE_ERROR_BEGIN))
                    error_message = COMPILATION_ERROR_TEXT + '\n'.join(lines[start:])

                feedback = error_message

            else:
                feedback = UNEXPECTED_ERROR_TEXT + error_message

        except:
            feedback = fatal_feedback

    result = {
        'score': score,
        'feedback': feedback,
    }
    print(json.dumps(result))
