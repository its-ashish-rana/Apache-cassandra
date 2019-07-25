from cassandra.cluster import Cluster

def create_connection():
    # TO DO: Fill in your own contact point
    cluster = Cluster(['127.0.0.1'])
    return cluster.connect('emp')

def set_user(session, name, m_id, m_city, m_email):
    # TO DO: execute SimpleStatement that inserts one user into the table


def get_user(session, name):
    # TO DO: execute SimpleStatement that retrieves one user from the table
    # TO DO: print firstname and age of user


def update_user(session, new_mem_id, name):
    # TO DO: execute SimpleStatement that updates the age of one user


def delete_user(session, name):
    # TO DO: execute SimpleStatement that deletes one user from the table


def main():

    session = create_connection()
    name = "Ashish"
    m_id = AR
    m_city = "Delhi"
    m_email = "ashish05.rana05@gmail.com"
    new_mem_id = 36

    set_user(session, name, id, m_city, m_email)

    get_user(session, name)

    update_user(session, new_mem_id, name)

    get_user(session, name)

    delete_user(session, name)

if __name__ == "__main__":
    main()
    
 
