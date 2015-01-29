'''
Created on 29/1/2015

@author: Andrea
'''

from ec.edu.itsae.conec import DBconec
import json


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    
    
    def reportarMaquinas(self):
        con=self.conexion().connect().cursor()
        con.execute("select * from activos")
        reporte=con.fetchall()
        return reporte