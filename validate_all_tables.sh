ma_list='tree_list/ma_list'
ma_list_fn=("`ls tree_list/ma_list`")
csv_bucket='tree_list/csv_bucket'

dump_ma_table()
{
    fn=$1
    ma=${fn%%.*}
    full_fn=$ma_list/$fn
    range=(`cat $full_fn`)

    if [[ ${#range[@]} -lt 10 ]]; then
        # fetch all at one time
        s_t=$(( $e_t ))
        e_t=$((${#range[@]} - 1))
        echo "python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}"
        python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}

        sleep 1
        continue
    fi

    q_num=$((${#range[@]}/4))

    s_t=0
    e_t=0
    for (( i = 0; i < 3; i++ )); do
        s_t=$(($q_num * $i))
        e_t=$(($q_num * $(($i + 1)) - 1))

        echo "python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}"
        python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}
        sleep 1
    done

    s_t=$(( $e_t + 1 ))
    e_t=$((${#range[@]} - 1))
    echo "python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}"
    python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}
    sleep 1
}


# validation file number
invalid=''
for fn in ${ma_list_fn}
do
    ma=${fn%%.*}
    full_fn=$ma_list/$fn
    range=(`cat $full_fn`)
    range_num=${#range[@]}
    ma_file_num=$(
        IFS=$'\n'
        ma_files=(`ls ${csv_bucket}/${ma}* 2>/dev/null`)
        echo ${#ma_files[@]}
    )

    if [[ ${range_num} -lt 10  ]]; then
        if [[ ${ma_file_num} != 1 ]]; then
            rm -rf ${csv_bucket}/${ma}*
            invalid="${invalid} ${ma}.range"
            echo "$ma invalidate file_num, ma_file_num(${ma_file_num}), range_num(${range_num})"
        fi

        continue
    fi

    if [[ ${ma_file_num} != 4 ]]; then
        invalid="${invalid} ${ma}.range"
        echo "$ma invalidate, ma_file_num(${ma_file_num})"

        if [[ ${ma_file_num} != 0 ]]; then
            echo "`ls ${csv_bucket}/${ma}* 2>/dev/null`"
        fi
    fi
done

for fn in ${invalid}
do
    echo "Re Fetch ${fn}"
    dump_ma_table ${fn}
    echo ""
done

exit

# TODO: validation range number

