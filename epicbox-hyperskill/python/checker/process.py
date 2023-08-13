import json

FAILED_TEST_BEGIN = '#educational_plugin FAILED + '
FAILED_TEST_CONTINUE = '#educational_plugin '

if __name__ == '__main__':
    score = 1
    feedback = ''

    with open('code.txt') as f:
        code = f.read().strip()
    with open('stdout.txt') as f:
        stdout = f.read().strip()
    with open('stderr.txt') as f:
        stderr = f.read().strip()

    if code != '0':
        score = 0
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
        else:
            feedback = (
                'stdout:\n{stdout}\n\nstderr:\n{stderr}'
                .format(stdout='\n'.join(stdout), stderr='\n'.join(stderr))
            )

    result = {
        'score': score,
        'feedback': feedback,
    }
    print(json.dumps(result))
