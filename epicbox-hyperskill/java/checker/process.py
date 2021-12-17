import json
import os
import subprocess
import sys
import traceback

TASK_ROOT = '/sandbox'

HSTEST_JAR = f'/checker/hs-test.jar'
KOTLIN_JAR = f'/checker/kotlinc/lib/kotlin-stdlib.jar'

CLASSES_FOLDER = f'{TASK_ROOT}/out'
MODULES = [
    f'{TASK_ROOT}/src',
    f'{TASK_ROOT}/test',
    f'{TASK_ROOT}/util/src',
    f'{TASK_ROOT}/util/test',
]

COMPILE_OPTIONS = [
    '-cp', HSTEST_JAR, '-d', CLASSES_FOLDER
]

JAVA_EXECUTE = [
    'java', '-cp', f'{HSTEST_JAR}:{KOTLIN_JAR}:{CLASSES_FOLDER}', '-ea',
    f'-DinsideDocker=true',
    f'-DignoreStdout=true',
    f'-Duser.dir={TASK_ROOT}',
    f'-Dfile.encoding=utf-8',
    'org.hyperskill.hstest.stage.StageTest'
]

all_stdout = []
all_stderr = []


def finish(successful: bool, feedback: str):
    score = 1 if successful else 0

    if '--debug' in sys.argv:
        print(f'Score: {score}\nFeedback:\n{feedback}')

    else:
        result = {
            'score': score,
            'feedback': feedback,
        }
        print(json.dumps(result, sort_keys=True))

    exit(0)


def finish_badly(reason: str = ''):
    bad_feedback = (
        'Cannot check the submission.\n'
        '\n'
        'Perhaps your program has fallen into an infinite loop or created too many objects in memory.\n'
        'If you are sure that this is not the case, please send the report to support@hyperskill.org\n'
        '\n'
        'reason:\n'
        '{exception}\n'
        '\n'
        'stdout:\n'
        '{stdout}\n'
        '\n'
        'stderr:\n'
        '{stderr}'
        .format(exception=reason,
                stdout='\n---\n'.join(all_stdout),
                stderr='\n---\n'.join(all_stderr))
    )
    finish(False, bad_feedback)


def run_process(args):
    proc = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    exit_code = proc.wait()

    stdout = proc.stdout.read().decode().strip()
    stderr = proc.stderr.read().decode().strip()

    all_stdout.append(stdout)
    all_stderr.append(stderr)

    return exit_code, stdout, stderr


def compilation_error_feedback(stderr):
    lines = stderr.strip().splitlines()
    output = []

    for line in lines:
        if line.startswith(TASK_ROOT):
            line = line.replace(TASK_ROOT, '', 1)
        output.append(line)

    return 'Compilation error\n\n' + '\n'.join(output).strip()


def compile_files(compiler: str, extension: str):
    compile_command = [compiler] + COMPILE_OPTIONS

    files_to_compile = []

    for module in MODULES:
        for path, folders, files in os.walk(module):
            for file in files:
                if file.endswith(extension):
                    files_to_compile += [os.path.join(path, file)]

    if not files_to_compile:
        return

    code, out, err = run_process(compile_command + files_to_compile)

    if code != 0:
        finish(False, compilation_error_feedback(out + '\n' + err))


def run_java():
    code, out, err = run_process(JAVA_EXECUTE)
    out = out.strip()
    err = err.strip()

    if code != 0:
        if len(out) == 0 and len(err) == 0:
            finish_badly(f'No stdout, no stderr, code = {code}')

        if len(out):
            finish(False, out)

        if len(err):
            finish(False, err)

    finish(True, '')


if __name__ == '__main__':
    try:
        compile_files('javac', '.java')
        compile_files('kotlinc', '.kt')
        run_java()
    except Exception as ex:
        exc_tb = ex.__traceback__
        traceback_stack = traceback.format_exception(etype=type(ex), value=ex, tb=exc_tb)
        finish_badly(''.join(traceback_stack))
