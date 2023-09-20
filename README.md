# epicbox-images

Dockerfiles to build images used to automatically grade
[programming assignments](https://stepik.org/lesson/9173/) on [Stepik.org](https://stepik.org/)

Base images with created `sandbox (1000:1000)` user:

* [`stepik/epicbox-base:alpine-3.6`](https://hub.docker.com/r/stepik/epicbox-base/)
* [`stepik/epicbox-base:bullseye`](https://hub.docker.com/r/stepik/epicbox-base/)
* [`stepik/epicbox-base:buster`](https://hub.docker.com/r/stepik/epicbox-base/)
* [`stepik/epicbox-base:stretch`](https://hub.docker.com/r/stepik/epicbox-base/)
* [`stepik/epicbox-base:jessie`](https://hub.docker.com/r/stepik/epicbox-base/)

Images for programming languages:

* ASM32, ASM64, C, C++, C++11: [`stepik/epicbox-gcc:6.3.0`](https://hub.docker.com/r/stepik/epicbox-gcc/)
* C++17, C++20: [`stepik/epicbox-gcc:10.2.1`](https://hub.docker.com/r/stepik/epicbox-gcc/)
* C#: [`stepik/epicbox-mono:5.0.0`](https://hub.docker.com/r/stepik/epicbox-mono/)
* Clojure: [`stepik/epicbox-clojure:1.9.0.397`](https://hub.docker.com/r/stepik/epicbox-clojure/)
* Go: [`stepik/epicbox-go:1.8.1`](https://hub.docker.com/r/stepik/epicbox-go/)
* Haskell 7.8: [`stepik/epicbox-haskell:7.8.4`](https://hub.docker.com/r/stepik/epicbox-haskell/)
* Haskell 8.0: [`stepik/epicbox-haskell:8.0.2`](https://hub.docker.com/r/stepik/epicbox-haskell/)
* Java 7: [`stepik/epicbox-java:7u181`](https://hub.docker.com/r/stepik/epicbox-java/)
* Java 8: [`stepik/epicbox-java:8u181`](https://hub.docker.com/r/stepik/epicbox-java/)
* Java 9: [`stepik/epicbox-java:9.0.1`](https://hub.docker.com/r/stepik/epicbox-java/)
* Java 11: [`stepik/epicbox-java:11.0.1`](https://hub.docker.com/r/stepik/epicbox-java/)
* JavaScript: [`stepik/epicbox-node:10.13.0`](https://hub.docker.com/r/stepik/epicbox-node/)
* Kotlin: [`stepik/epicbox-kotlin:1.3.11`](https://hub.docker.com/r/stepik/epicbox-kotlin/)
* Octave: [`stepik/epicbox-octave:4.0.3`](https://hub.docker.com/r/stepik/epicbox-octave/)
* PascalABC.NET: [`stepik/epicbox-pascalabc:3.2`](https://hub.docker.com/r/stepik/epicbox-pascalabc/)
* Perl: [`stepik/epicbox-perl:5.24.3`](https://hub.docker.com/r/stepik/epicbox-perl/)
* PHP: [`stepik/epicbox-php:7.2.6`](https://hub.docker.com/r/stepik/epicbox-php/)
* R: [`stepik/epicbox-r:3.4.2`](https://hub.docker.com/r/stepik/epicbox-r/)
* Ruby: [`stepik/epicbox-ruby:2.5.3`](https://hub.docker.com/r/stepik/epicbox-ruby/)
* Scala: [`stepik/epicbox-scala:2.12.7`](https://hub.docker.com/r/stepik/epicbox-scala/)
* [TRIK Studio](http://www.trikset.com/): [`stepik/epicbox-trik:20171122`](https://hub.docker.com/r/stepik/epicbox-trik/)
* Valgrind: [`stepik/epicbox-valgrind:3.12.0`](https://hub.docker.com/r/stepik/epicbox-valgrind/)

Images for source code analyzers:

* [PMD](https://pmd.github.io): [`stepik/epicbox-pmd:6.9.0`](https://hub.docker.com/r/stepik/epicbox-pmd/)

Images for Hyperskill (EduTools):

* Gradle: [`stepik/epicbox-hyperskill:gradle-20190424`](https://hub.docker.com/r/stepik/epicbox-hyperskill/)
* Python: [`stepik/epicbox-hyperskill:python-20190424`](https://hub.docker.com/r/stepik/epicbox-hyperskill/)

All images are built automatically in Docker Hub but builds are triggered manually by the Stepik team.
