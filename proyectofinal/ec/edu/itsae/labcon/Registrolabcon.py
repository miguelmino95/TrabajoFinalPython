'''
Created on 29/1/2015

@author: Andrea
'''

from ec.edu.itsae.conec import DBconec
import json


class Registrolabcon(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    
    def reportarActivos(self):
        con=self.conexion().connect().cursor()
        con.execute("select * from activos")
        reporte=con.fetchall()
        return reporte