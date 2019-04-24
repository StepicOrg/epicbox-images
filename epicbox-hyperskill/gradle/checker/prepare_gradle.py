import os

PROJECT_FOLDER = '/sandbox'
BUILD_GRADLE = '/sandbox/build.gradle'

KOTLIN_PLUGIN = "id 'org.jetbrains.kotlin.jvm'"
KOTLIN_DEPENDENCY = "implementation 'org.jetbrains.kotlin:"


def need_include_kotlin():
    for path, dirs, files in os.walk(PROJECT_FOLDER):
        for file in files:
            if file.endswith('.kt'):
                return True
    return False


if __name__ == '__main__':

    if not need_include_kotlin():
        # kotlin is included by default
        build = open(BUILD_GRADLE, 'r').read()
        build = build.replace(KOTLIN_PLUGIN, '//' + KOTLIN_PLUGIN)
        build = build.replace(KOTLIN_DEPENDENCY, '//' + KOTLIN_DEPENDENCY)
        with open(BUILD_GRADLE, 'w') as file:
            file.write(build)
