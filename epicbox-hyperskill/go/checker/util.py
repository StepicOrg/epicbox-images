import json
import subprocess
import sys
import traceback

TASK_ROOT = '/sandbox'

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
        '{reason}\n'
        '\n'
        'stdout:\n'
        '{stdout}\n'
        '\n'
        'stderr:\n'
        '{stderr}'
        .format(reason=reason,
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


def format_exception(ex):
    if sys.version_info >= (3, 10):
        traceback_stack = traceback.format_exception(ex)
    else:
        exc_tb = ex.__traceback__
        traceback_stack = traceback.format_exception(etype=type(ex), value=ex, tb=exc_tb)

    return ''.join(traceback_stack)
