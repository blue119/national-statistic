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


for fn in ${ma_list_fn}
do
    dump_ma_table ${fn}
    # ma=${fn%%.*}
    # full_fn=$ma_list/$fn
    # range=(`cat $full_fn`)
    # q_num=$((${#range[@]}/4))

    # s_t=0
    # e_t=0
    # for (( i = 0; i < 3; i++ )); do
        # s_t=$(($q_num * $i))
        # e_t=$(($q_num * $(($i + 1)) - 1))

        # python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}
        # echo "python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}"
        # sleep 1
    # done

    # s_t=$(( $e_t + 1 ))
    # e_t=$((${#range[@]} - 1))
    # python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}
    # echo "python3 fetch_statistic_data.py $ma ${range[$s_t]}-${range[$e_t]}"
    # sleep 1
done



