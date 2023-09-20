import os.path

from util import TASK_ROOT, finish, finish_badly, run_process

FAILED_TEST_BEGIN = '#educational_plugin FAILED + '
FAILED_TEST_CONTINUE = '#educational_plugin '

TESTS_FILES = [
    f'{TASK_ROOT}/tests.py',
    f'{TASK_ROOT}/test/tests.py'
]


def is_python_tests() -> bool:
    return any(os.path.isfile(f) for f in TESTS_FILES)


def process_python():
    test_file = ''
    for file in TESTS_FILES:
        if os.path.isfile(file):
            test_file = file
            break

    python_execute_command = [
        'python3', test_file, '--inside_docker'
    ]

    code, out, err = run_process(python_execute_command)
    out = out.strip().splitlines()

    if code != 0:
        finish_badly(f'Exit code = {code}')

    if any(line.startswith(FAILED_TEST_BEGIN) for line in out):
        output = []
        output_started = False

        for line in out:
            if output_started and line.startswith(FAILED_TEST_CONTINUE):
                output.append(line[len(FAILED_TEST_CONTINUE):])

            if not output_started and line.startswith(FAILED_TEST_BEGIN):
                output_started = True
                output.append(line[len(FAILED_TEST_BEGIN):])

        feedback = '\n'.join(output).strip()

        finish(False, feedback)

    else:
        finish(True, '')
