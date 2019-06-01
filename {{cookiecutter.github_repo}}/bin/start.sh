#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build, [-b] for bash shell" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dpb" opt; do
    case "$opt" in
        d)
          DEBUG=true
          docker-compose up
          ;;
        p)
          DEBUG=false
          docker-compose up
          ;;
        b)
          docker-compose run --entrypoint bash api
          ;;
        *)
          usage
          ;;
    esac
done

# fix ownership
echo "Fixing ownership on Linux"
if [ `uname -s` = "Linux" ]
then
  ls -l
  echo "sudo chown -R `id -u $USER`:`id -g $USER` ."
  sudo chown -R `id -u $USER`:`id -g $USER` .
  ls -l
fi
