import json

FILES_ROOT = '/checker/sandbox/files/'
FAILED_TEST_BEGIN = '#educational_plugin FAILED + '
FAILED_TEST_CONTINUE = '#educational_plugin'

if __name__ == '__main__':
    score = 1
    feedback = ''

    code = open('code.txt').read().strip()
    if code != '0':
        stdout = open('stdout.txt').read().splitlines()
        stderr = open('stderr.txt').read().splitlines()
        score = 0

        feedback = (
            'Cannot check the submission.\n\nPerhaps your program '
            'has fallen into an infinite loop or created too many objects in memory. '
            'If you are sure that this is not the case, please send the report to support@hyperskill.org\n'
            'stdout:\n{stdout}\n\nstderr:\n{stderr}'
            .format(stdout='\n'.join(stdout), stderr='\n'.join(stderr))
        )

        if any(line.startswith('> Compilation failed;') or  # detect java compile error
               line.startswith('> Compilation error.')  # detect kotlin compile error
               for line in stderr):
            output = []

            for line in stderr:
                if line.startswith('FAILURE'):
                    break

                if line.startswith(FILES_ROOT):
                    line = line.replace(FILES_ROOT, '', 1)

                output.append(line)

            feedback = 'Compilation error\n\n' + '\n'.join(output).strip()

        else:
            if any(line.startswith(FAILED_TEST_BEGIN) for line in stdout):
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
