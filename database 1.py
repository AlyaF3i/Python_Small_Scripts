import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  password="",
  database="qa"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user;")
for a in mycursor:
  print(a)
#mydb.commit()
#arr=['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_batch_insert', '_binary', '_check_executed', '_connection', '_description', '_execute_iter', '_executed', '_executed_list', '_fetch_row', '_fetch_warnings', '_handle_eof', '_handle_noresultset', '_handle_result', '_handle_resultset', '_handle_warnings', '_have_unread_result', '_last_insert_id', '_nextrow', '_process_params', '_process_params_dict', '_raw', '_reset_result', '_rowcount', '_set_connection', '_stored_results', '_warning_count', '_warnings', 'arraysize', 'callproc', 'close', 'column_names', 'description', 'execute', 'executemany', 'fetchall', 'fetchmany', 'fetchone', 'fetchwarnings', 'getlastrowid', 'lastrowid', 'next', 'nextset', 'reset', 'rowcount', 'setinputsizes', 'setoutputsize', 'statement', 'stored_results', 'with_rows']
"""for a in arr:
  try:
    print(f"{a}:   ",eval(f'mycursor.{a}()'))
  except:
    continue
"""