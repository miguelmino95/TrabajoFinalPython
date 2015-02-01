'''
Created on 1/2/2015

@author: Miguelm
'''

from ec.edu.itsae.conec import DBconec


class Accionlabcon(DBconec.DBcon):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def validarUsuario(self, usuario, clave):
        con=self.conexion().connect().cursor()
        con.execute("""select * from trabajador where usuario='%s' and clave='%s'""" % (usuario, clave))
        reporte=con.fetchall()
        return reporte
    
    
    def reportarActivo(self):
        con=self.conexion().connect().cursor()
        con.execute("select * from activo")
        reporte=con.fetchall()
        return reporte
    
    def insertarActivo(self, nombre, fcompra, estado, nfactura, modelo):
        con=self.conexion().connect()
        sql=""" insert into personas(nombre, fech_compra, estado, num_factura, modelo) 
        values('%s', '%s', %i , '%s', '%s') """ % (nombre, fcompra, estado, nfactura, modelo)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
            
    def buscarActivoDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from activo where upper(CONCAT(nombre,' ', num_factura,' ', modelo)) like upper('%s') """ %("%"+datobuscado+"%"))
        reporte=con.fetchall()
        return reporte
            
    