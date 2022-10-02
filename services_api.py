def check_login(user_mail, password):
    # dbcall
    dbcall = True
    if(dbcall):
        return 'success'
    else:
        return 'failure'


def register(uta_id, uta_mail, user_name, password):
    try:
        print("Trying to add user")
        # dbcall
        return('Added user successfully')
    except:
        return('Unable to add user')


def join_course_group(uta_id, course_id):
    # db call
    return 'success'


def add_course_to_db(course_id, dept_name):
    # db call
    return 'success'
