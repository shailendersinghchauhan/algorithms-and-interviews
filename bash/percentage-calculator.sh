#!/bin/bash
cut -f "9" -d " " nginx_logs > http_code.log
total_error_code=$(wc -l http_code.log|cut -f 1 -d " ")
echo "total Error coe is: $total_error_code"
ERROR_CODE_FILE=http_code.log
echo "Parsing 2XX"
grep ^2 $ERROR_CODE_FILE > 200.log
echo "Parsing 3XX"
grep ^3 $ERROR_CODE_FILE > 300.log
echo "Parsing 5XX"
grep ^5 $ERROR_CODE_FILE >500.log
total_200_count=$(wc -l 200.log| cut -f 1 -d " ")
total_300_count=$(wc -l 300.log| cut -f 1 -d " ")
total_500_count=$(wc -l 500.log| cut -f 1 -d " ")
echo "Total Code values"
echo "-----------------"
echo "Total 2XX $total_200_count"
echo "Total 3XX $total_300_count"
echo "total 5XX $total_500_count"

two_per=$(( $total_200_count*100/$total_error_code ))
three_per=$(( $total_300_count*100/$total_error_code ))
five_per=$(( $total_500_count*100/$total_error_code ))
echo "Print % of error codes are mentioned Below:"
echo "--------------------"
echo "1. 2XX % is:$two_per"
echo "1. 3XX % is:$three_per"
echo "1. 5XX % is:$five_per"
#echo "3XX % is:$three_per"
#echo "4XX % is:$five_per"
