#!/bin/bash


RUN_DIRECTORY=`dirname $0`
if [[ ! $RUN_DIRECTORY =~ "scripts" ]]; then
   echo "This script is meant to be run from the root of the project, in order to properly load everything, like this:"
   echo "./scripts/`basename $0`"
   exit 1
fi

FIXTURES=community/fixtures
apps=(auth forum forum_conversation forum_member forum_attachments forum_polls forum_feeds forum_moderation forum_search forum_tracking forum_permission category)

for i in "${apps[@]}"
do
    echo "exporting $i"
    poetry run python manage.py dumpdata $i --indent 2 --format json > $FIXTURES/$i.json
done
