from datetime import datetime, date

def lab_status():
    check_t = datetime.now()
    t_now_calc = (60*check_t.minute)+(60*60*check_t.hour)+check_t.second
    if (t_now_calc<72000 and t_now_calc >= 39600 and datetime.today().isoweekday() != 6 and datetime.today().isoweekday() != 7):
        stts = "Открыта"
    elif (t_now_calc<68400 and t_now_calc >= 43200 and datetime.today().isoweekday() != 1,2,3,4,5 and datetime.today().isoweekday() != 7):
        stts = "Открыта"
    else:
        stts = "Закрыта"

    return stts
