import os

PROJECT_FOLDER = '/sandbox/project'
DEFAULT_GRADLE = '/sandbox/build.gradle'
GRADLE_WITHOUT_KOTLIN = '/sandbox/build_no_kotlin.gradle'


def need_include_kotlin():
    for path, dirs, files in os.walk(PROJECT_FOLDER):
        for file in files:
            if file.endswith('.kt'):
                return True
    return False


if __name__ == '__main__':

    if not need_include_kotlin():
        # kotlin is included in default gradle
        os.remove(DEFAULT_GRADLE)
        os.rename(GRADLE_WITHOUT_KOTLIN, DEFAULT_GRADLE)
