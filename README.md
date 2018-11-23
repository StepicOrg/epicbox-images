# epicbox-images
Dockerfiles to build images used to automatically grade
[programming assignments](https://stepik.org/lesson/9173/) on [Stepik.org](https://stepik.org/)

Base images with created `sandbox (1000:1000)` user:
* [`stepik/epicbox-base:alpine-3.6`](https://hub.docker.com/r/stepik/epicbox-base/)
* [`stepik/epicbox-base:stretch`](https://hub.docker.com/r/stepik/epicbox-base/)
* [`stepik/epicbox-base:jessie`](https://hub.docker.com/r/stepik/epicbox-base/)

Images for programming languages:
* ASM32, ASM64, C, C++, C++11: [`stepik/epicbox-gcc:6.3.0`](https://hub.docker.com/r/stepik/epicbox-gcc/)
* C#: [`stepik/epicbox-mono:5.0.0`](https://hub.docker.com/r/stepik/epicbox-mono/)
* Go: [`stepik/epicbox-go:1.8.1`](https://hub.docker.com/r/stepik/epicbox-go/)
* Java 7: [`stepik/epicbox-java:7u181`](https://hub.docker.com/r/stepik/epicbox-java/)
* Java 8: [`stepik/epicbox-java:8u181`](https://hub.docker.com/r/stepik/epicbox-java/)
* Java 9: [`stepik/epicbox-java:9.0.1`](https://hub.docker.com/r/stepik/epicbox-java/)
* Java 11: [`stepik/epicbox-java:11.0.1`](https://hub.docker.com/r/stepik/epicbox-java/)
* JavaScript: [`stepik/epicbox-node:10.13.0`](https://hub.docker.com/r/stepik/epicbox-node/)
* Octave: [`stepik/epicbox-octave:4.0.3`](https://hub.docker.com/r/stepik/epicbox-octave/)
* PascalABC.NET: [`stepik/epicbox-pascalabc:3.2`](https://hub.docker.com/r/stepik/epicbox-pascalabc/)
* Perl: [`stepik/epicbox-perl:5.24.3`](https://hub.docker.com/r/stepik/epicbox-perl/)
* PHP: [`stepik/epicbox-php:7.2.6`](https://hub.docker.com/r/stepik/epicbox-php/)
* R: [`stepik/epicbox-r:3.4.2`](https://hub.docker.com/r/stepik/epicbox-r/)
* Ruby: [`stepik/epicbox-ruby:2.5.3`](https://hub.docker.com/r/stepik/epicbox-ruby/)
* Scala: [`stepik/epicbox-scala:2.12.7`](https://hub.docker.com/r/stepik/epicbox-scala/)
* [TRIK Studio](http://www.trikset.com/): [`stepik/epicbox-trik:20171122`](https://hub.docker.com/r/stepik/epicbox-trik/)

Images for source code analyzers:
* [PMD](https://pmd.github.io): [`stepik/epicbox-pmd:6.9.0`](https://hub.docker.com/r/stepik/epicbox-pmd/)

All images are built automatically in Docker Hub but builds are triggered manually by the Stepik team.
