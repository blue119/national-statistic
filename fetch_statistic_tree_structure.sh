#!/usr/bin/env bash

national_statistic_url='http://ebas1.ebas.gov.tw/pxweb/Dialog/statfile9L.asp'
national_income_url='http://ebas1.ebas.gov.tw/pxweb/Dialog/NI.asp'
national_price_url='http://ebas1.ebas.gov.tw/pxweb/Dialog/price.asp'

fetch_tree()
{
    url=$1

    curl ${url} | iconv -f big5 -t utf8 | grep 'span class\|span style' \
        | sed 's/.*rootFront.*>\(.*\)<\/span.*/rootFront: \1/' \
        | sed 's/.*folder.*>\(.*\)<\/span.*/folder: \1/' \
        | sed 's/.*a\ href="\(.*\)"\ target.*/\1/' \
        | sed 's/.*ma=\(.*\)\&ti=\(.*\)\&path=\(.*\)\&lang.*/\1\t\2\t\3/'
}

fetch_tree $national_statistic_url > tree_list/national_statistic_tree.txt
fetch_tree $national_income_url    > tree_list/national_income_tree.txt
fetch_tree $national_price_url     > tree_list/national_price_tree.txt

