#!/bin/bash
check_result () {
  RESULT=$?
  MESSAGE=$1
  if [ $RESULT == 0 ]; then
    echo [SUCCESS] $MESSAGE
  else
    echo [FAIL] $MESSAGE
    exit 1
  fi
}

for output in confirmed recovered deaths; do
  sudo docker run coronadata | grep $output
  check_result $output
done

exit 0
