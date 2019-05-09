#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dp" opt; do
    case "$opt" in
        d)
          DEBUG=true
          docker-compose build
          ;;
        p)
          DEBUG=false
          docker-compose build
          ;;
        *)
          usage
          ;;
    esac
done
