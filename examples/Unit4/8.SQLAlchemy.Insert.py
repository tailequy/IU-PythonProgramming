#Insert Data
#The example below will add tree records into the “actor” table.
import sqlalchemy as db
def main():
    # get engine object using pymysql driver for mysql
    engine = db.create_engine("mysql+pymysql://root:168098205@localhost:3306/movie")
    # get metadata object
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get actor table definitio
    actor_table = db.Table("actor", meta_data, autoload=True, autoload_with=engine)
    # set the insert statement
    sql_query = db.insert(actor_table)
    # set data list
    data_list = [{"first_name":"John", "last_name":"Smith", "age":50,
                  "date_of_birth":"1969-04-05","active":True},
                 {"first_name":"Brian", "last_name":"Morgan", "age":38,
                  "date_of_birth":"1981-02-11", "active":True},
                 {"first_name":"David", "last_name":"White", "age":77,
                  "date_of_birth":"1942-06-30", "active":False}]
    # execute the insert statement
    result = connection.execute(sql_query, data_list)
if __name__ == '__main__':
    main()