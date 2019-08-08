#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build, [-b] for bash shell" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dpb" opt; do
    case "$opt" in
        d)
          DEBUG=true
          if [ `uname -s` = "Linux" ]
          then
            sudo docker-compose up
          else
            docker-compose up
          fi
          ;;
        p)
          DEBUG=false
          if [ `uname -s` = "Linux" ]
          then
            sudo docker-compose up
          else
            docker-compose up
          fi
          ;;
        b)
          if [ `uname -s` = "Linux" ]
          then
            sudo docker-compose run --entrypoint bash api
          else
            docker-compose run --entrypoint bash api
          fi
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
