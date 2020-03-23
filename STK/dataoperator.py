#coding=utf-8

import jqdatasdk as jq
from datetime import datetime
from datagent import BaosAgent

if __name__ == "__main__":
    jq.auth('15808061188', 'allan2jq')
    all_securities = jq.get_all_securities(date=datetime.now())
    all_securities = all_securities[all_securities.display_name.str.find('ST') == -1]
    all_securities = all_securities[all_securities.display_name.str.find('退') == -1]
    all_sto_id = all_securities.index.str[:6].to_list()

    ba = BaosAgent(all_sto_id)
    start_date = '2017-01-01'
    freq       = 15
    ba.persist_freq_data(start_date, freq)