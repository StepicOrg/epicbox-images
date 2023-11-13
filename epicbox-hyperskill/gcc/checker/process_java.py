import os

from util import finish, finish_badly, run_process, TASK_ROOT

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


def is_java_tests() -> bool:
    tests_folder = f'{TASK_ROOT}/test'

    if not os.path.isdir(tests_folder):
        return False

    for path, folders, files in os.walk(tests_folder):
        for file in files:
            if file.endswith('.java') or file.endswith('.kt'):
                return True

    return False


def compilation_error_feedback(stderr: str) -> str:
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


def process_java():
    compile_files('javac', '.java')
    compile_files('kotlinc', '.kt')
    run_java()
