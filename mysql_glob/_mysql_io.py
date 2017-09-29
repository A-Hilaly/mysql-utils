import mysql.connector

def load_mysql_logs():
    return "localhost", "root", "uehMLMRw"

def load_mysql_connector_conf():
    return True, True

def configure_mysql_logs():
    pass

def gen_mysql_server_connector():
    host, user, password = load_mysql_logs()
    use_pure, raise_on_warnings = load_mysql_connector_conf()
    c = mysql.connector.connect(host=host,
                                user=user,
                                password=password,
                                use_pure=use_pure,
                                raise_on_warnings=raise_on_warnings)
    return c

class BadConnector(Exception):
    pass

def execute_only(*args, commit=False):
    connector = GMSC()
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    if commit:
        connector.commit()

def execute_and_fetch(*args, commit=False):
    connector = GMSC()
    result = []
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    for e in cursor:
        result.append(e)
    if commit:
        connector.commit()
    return result
