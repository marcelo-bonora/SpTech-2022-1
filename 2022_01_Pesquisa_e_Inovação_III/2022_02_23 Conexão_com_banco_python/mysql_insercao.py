import mysql.connector

def sum_of_n_init(n):
    con = mysql.connector.connect(host='127.0.0.1',
    database='analise_algoritmos',
    user='aluno',
    password = 'sptech')

    mycursor = con.cursor()
    sql = "INSERT INTO tblVelocimetro VALUES (null, %s, %s)"
    
    lst = []

    acumul_acelerate = 0
    print(f"Realizando inserção no banco:")
    for i in range(1, n+1):
        acumul_acelerate = acumul_acelerate + i
        lst.append(f"({n}, {acumul_acelerate})")
        val = (f"{n}", f"{acumul_acelerate}")
        mycursor.execute(sql, val)
    con.commit()
    print(lst)
sum_of_n_init(10)
