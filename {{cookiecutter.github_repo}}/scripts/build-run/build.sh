#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dp" opt; do
    case "$opt" in
        d)
          if [ `uname -s` = "Linux" ]
          then
            sudo docker-compose build --build-arg DEBUG=true api
          else
            docker-compose build --build-arg DEBUG=true api
          fi
          ;;
        p)
          if [ `uname -s` = "Linux" ]
          then
            sudo docker-compose build api
          else
            docker-compose build api
          fi
          ;;
        *)
          usage
          ;;
    esac
done
