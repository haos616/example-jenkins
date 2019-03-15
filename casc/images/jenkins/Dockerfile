ARG JENKINS_VERSION

FROM jenkins/jenkins:${JENKINS_VERSION}

COPY ./files/plugins.txt /usr/share/jenkins/ref/plugins.txt

RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
