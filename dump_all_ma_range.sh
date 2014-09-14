MAS=("$(python3 fetch_statistic_data.py --show-tree | sed 's/\(.*\)\t.*/\1/g')")

for ma in ${MAS[@]}
do
    python3 fetch_statistic_data.py --show-query-range ${ma} > tree_list/ma_list/${ma}.range
    echo ${ma}
done
# for (( i = 0; i < ${MAS[#]}; i++ )); do
    # statements
# done

