#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development build, [-p] for a production build" 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":dp" opt; do
    case "$opt" in
        d)
          DEBUG=true
          if [ `uname -s` = "Linux" ]
          then
            sudo docker-compose run --name test-api --entrypoint /code/bin/test-entrypoint.sh   --rm
          else
            docker-compose run --name test-api --entrypoint /code/bin/test-entrypoint.sh   --rm
          fi
          ;;
        p)
          DEBUG=false
          if [ `uname -s` = "Linux" ]
          then
            sudo docker-compose run --name test-api --entrypoint /code/bin/test-entrypoint.sh   --rm
          else
            docker-compose run --name test-api --entrypoint /code/bin/test-entrypoint.sh   --rm
          fi
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
