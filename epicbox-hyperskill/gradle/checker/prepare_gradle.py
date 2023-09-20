import os

PROJECT_FOLDER = '/sandbox'
BUILD_GRADLE = '/sandbox/build.gradle'

TO_COMMENT = {
    '.kt': [
        "id 'org.jetbrains.kotlin.jvm'",
        "implementation 'org.jetbrains.kotlin:"
    ],
    '.scala': [
        "id 'scala'",
        "implementation 'org.scala-lang:scala-library:",
        "scala.srcDir 'src'",
        "scala.srcDir 'test'"
    ]
}


def contains_extension(ext):
    for path, dirs, files in os.walk(PROJECT_FOLDER):
        for file in files:
            if file.endswith(ext):
                return True
    return False


if __name__ == '__main__':

    build = open(BUILD_GRADLE, 'r').read()

    for ext, to_comment in TO_COMMENT.items():
        if not contains_extension(ext):
            for line in to_comment:
                build = build.replace(line, '//' + line)

    with open(BUILD_GRADLE, 'w') as file:
        file.write(build)
