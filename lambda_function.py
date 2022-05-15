import json

import psycopg2


def connect():
    return psycopg2.connect(host="host do banco", database="seu banco", user="", password="")


def lambda_handler(event, context):
    try:
        print('Connecting')
        body = event['body']
        id_aluno = body['id_aluno']
        nome = body['nome']
        con = connect()
        cur = con.cursor()
        print('Saving')
        cur.execute('insert into aluno values(%s,%s)', (id_aluno, nome))
        con.commit()
        con.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)










