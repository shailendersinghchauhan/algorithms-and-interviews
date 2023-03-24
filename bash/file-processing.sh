#!/bin/bash

function file_processing_example()
{
ls -l . >temp_file
FILE_NAME=temp_file
TOTAL_WORD_COUNT=$(wc -l $FILE_NAME|cut -f 1 -d " ")

for((l=1;l<=$TOTAL_WORD_COUNT;l++));do
  FIELD_ONE=$(awk "NR >= $l && NR <= $l" $FILE_NAME| cut -d " " -f 2)
  echo "FIELD_NAME is: $FIELD_NAME"
done

}

#####
file_processing_example