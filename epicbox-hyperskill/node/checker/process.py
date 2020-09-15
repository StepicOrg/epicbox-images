import json

TASK_ROOT = '/checker/sandbox/'

FAILED_TEST_BEGIN = '#educational_plugin FAILED + '
FAILED_TEST_CONTINUE = '#educational_plugin '

COMPILATION_ERROR_BEGIN = 'SyntaxError:'
COMPILATION_ERROR_END = '    at '  # start of the stacktrace

if __name__ == '__main__':
    score = 1
    feedback = ''

    code = open('code.txt', encoding="utf-8").read().strip()
    stdout = open('stdout.txt', encoding="utf-8").read().splitlines()
    stderr = open('stderr.txt', encoding="utf-8").read().splitlines()
    if code != '0':
        score = 0
        feedback = (
            'Cannot check the submission.\n\nPerhaps your program '
            'has fallen into an infinite loop or created too many objects in memory. '
            'If you are sure that this is not the case, please send the report to support@hyperskill.org\n'
            'stdout:\n{stdout}\n\nstderr:\n{stderr}'
                .format(stdout='\n'.join(stdout), stderr='\n'.join(stderr))
        )

    elif any(line.startswith(COMPILATION_ERROR_BEGIN) for line in stderr):
        score = 0
        output = []
        output_started = False

        for line in stderr:
            if line.startswith(COMPILATION_ERROR_END):
                break

            if TASK_ROOT in line:
                line = line.replace(TASK_ROOT, '', 1)

            if line.startswith(COMPILATION_ERROR_BEGIN):
                output_started = True

            if output_started:
                output.append(line)

        feedback = '\n'.join(output).strip()

    elif any(line.startswith(FAILED_TEST_BEGIN) for line in stdout):
        score = 0
        output = []
        output_started = False

        for line in stdout:
            if output_started and line.startswith(FAILED_TEST_CONTINUE):
                output.append(line[len(FAILED_TEST_CONTINUE):])

            if not output_started and line.startswith(FAILED_TEST_BEGIN):
                output_started = True
                output.append(line[len(FAILED_TEST_BEGIN):])

        feedback = '\n'.join(output).strip()

    result = {
        'score': score,
        'feedback': feedback,
    }
    print(json.dumps(result))
