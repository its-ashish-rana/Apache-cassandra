# Apache-cassandra
Working with Apache Cassandra

<pre>
Prerequisites:

A running instance of Apache Cassandra® 2.1+
Python 2.7, 3.4, 3.5, or 3.6.
Use Pip to install the driver:
pip install cassandra-driver
We highly recommend to use a virtualenv
</pre>

Create the keyspace and table
The emp.cql file provides the schema used for this project:
<pre>
CREATE KEYSPACE member
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
</pre>
<pre>
CREATE TABLE emp.member (
    name text PRIMARY KEY,
    m_id int,
    m_city text,
    m_email text,
    );
</pre>
<h3><b>Connect to your cluster</b></h3></br>
All of our code is contained in the <a href = "https://github.com/9718546128/Apache-cassandra/blob/master/Application.py">Application.py</a> file. The <b>create_connection()</b> function connects to our cluster. 
By default, <b>Cluster()</b> will try to connect to <b>127.0.0.1 (localhost)</b>. Replace with your own contact point(s) if necessary.
<pre>
def create_connection():
    # TO DO: Fill in your own contact point
    cluster = Cluster(['127.0.0.1'])
    return cluster.connect('emp')
</pre>

CRUD Operations
Fill the code in the functions that will add a user, get a user, update a user and delete a user from the table with the driver.
<b>INSERT a user</b>
<pre>

def set_user( session, name, m_id, m_city, m_email ):
    # TO DO: execute SimpleStatement that inserts one user into the table
    session.execute("INSERT INTO member( name, m_id, m_city, m_email ) VALUES (%s,%s,%s,%s)", [ name, m_id, m_city, m_email ])

</pre>
    
<pre>
<b>SELECT a user</b>
def get_user(session, name):
    # TO DO: execute SimpleStatement that retrieves one user from the table
    # TO DO: print name and m_id of member
    result = session.execute("SELECT * FROM member WHERE name = %s", [name]).one()
    print result.name, result.m_id
</pre>

<a href= "https://github.com/9718546128/Apache-cassandra/blob/master/Cassandra_read"> What's about bulk read?</a>

<b>UPDATE a user's age</b>
<pre>
def update_user(session, new_mem_id, name):
    # TO DO: execute SimpleStatement that updates the age of one user
    session.execute("UPDATE member SET m_id =%s WHERE name = %s", [new_mem_id, name])
</pre>

<b>DELETE a user</b>
<pre>
def delete_user(session, name):
    # TO DO: execute SimpleStatement that deletes one user from the table
    session.execute("DELETE FROM member WHERE name = %s", [name])
</pre>
