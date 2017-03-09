FROM centos:latest

MAINTAINER Ayman Mousa <ayman.mousa.noreply.com>

RUN apt-get update

RUN apt-get install -y wget

RUN echo "centos http://mirror.centos.org/centos/7/" >> /etc/yum.repos.d  /etc/apt/sources.list.d

RUN apt-get -y install build-essential curl git
RUN apt-get -y install python3.6.0 python3-pip python3-dev
RUN apt-get -y install libxml2-dev libxslt-dev

RUN pip-3.2 install virtualenv
