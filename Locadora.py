import mysql.connector
import Janela
import PySimpleGUI as pyGui

from datetime import datetime, date, timedelta


def atualizaAluga():
    cur.execute("select * from aluga")
    al = cur.fetchall()
    Janela.BuscaAluguel(al)

def verificaData(values):
    cur.execute("select * from aluga")
    al = cur.fetchall()

    for tup in al:
        if int(values['idCar']) == int(tup[1]):

            diasTotal = tup[0]+timedelta(days=tup[2])#total dias tupla
            aux0 = diasTotal.strftime('%Y-%m-%d')#converti para str
            tupDataFinal = datetime.strptime(aux0, '%Y-%m-%d')# converti para datetime
            
            aux0 = tup[0].strftime('%Y-%m-%d')#converti str
            tupDataInicio = datetime.strptime(aux0, '%Y-%m-%d')# converti datetime

            cre_date = datetime.strptime(values['Data'], '%Y-%m-%d')

            if cre_date < tupDataInicio or cre_date > tupDataFinal:
                diasTotalNovo = cre_date+timedelta(days=int(values['NumDias']))     

                aux0 = diasTotalNovo.strftime('%Y-%m-%d')#converti para str
                diasTotalNewTup = datetime.strptime(aux0, '%Y-%m-%d')# converti para datetime

                if diasTotalNewTup < tupDataInicio or diasTotalNewTup > tupDataFinal:
                    #print(f"Passou IF {diasTotalNewTup}  < {tupDataInicio}  or {diasTotalNewTup} > {tupDataFinal}")
                    print(f"Horario Disponivel")
                else:
                    pyGui.popup("Choque De horario no agendamento")
                    return False
            else:
                pyGui.popup("Choque De horario no agendamento")
                return False
                
    return True    



def program(window, window1):       
    try:      

        while True:
            #event, values = window.read()
            win, event, values = pyGui.read_all_windows()
                
            if win == window and event == 'CadastrarCliente':
                #executa uma consulta
                if(values['nomeC'] and values['telC']):
                    params = values['nomeC'], values['telC']
                    args = cur.callproc('VerificaProcTel', [values['telC'], 0])
                    if(args[1] == True):
                        cur.execute(sql, (params)) #usando tupla
                        con.commit()
                        pyGui.popup('Cadastrado')
                    else:
                        pyGui.popup('ConsultaParam Descobriu que esse numero de celular ja foi cadastrado')

                    
                else:
                    pyGui.popup('Não foi possivel cadastrar o cliente')


            
            if win == window and event == 'CadastrarCarro':
                diaria = 0.0
                semanal = 0.0
                Tipo = None
                
                if values['Tipo_CarC'] == True:
                    diaria = Janela.DiariaCOMPACTO
                    semanal = Janela.SemCOMPACTO
                    Tipo = 'COMPACTO'
                if values['Tipo_CarM'] == True:
                    diaria = Janela.DiariaMEDIO
                    semanal = Janela.SemMEDIO
                    Tipo = 'MÉDIO'
                if values['Tipo_CarG'] == True:
                    diaria = Janela.DiariaGRANDE
                    semanal = Janela.SemGRANDE
                    Tipo = 'GRANDE'
                if values['Tipo_CarS'] == True:
                    diaria = Janela.DiariaSUV
                    semanal = Janela.SemSUV
                    Tipo = 'SUV'
                if values['Tipo_CarCAM'] == True: 
                    diaria = Janela.DiariaCAMINHAO
                    semanal = Janela.SemCAMINHAO
                    Tipo = 'CAMINHÃO'

                if(values['Marca'] and values['Modelo'] and values['ano']):
                    params = Tipo, diaria, semanal, values['Marca'], values['Modelo'], values['ano']
                    cur.execute(sqlCar, (params)) #usando tupla
                    con.commit()

                    pyGui.popup('Cadastrado')
                else:
                    pyGui.popup('Não foi possivel cadastrar o carro')



            if win == window and event == 'AtualizarTaxa':
                if(values['Diaria'] and values['Semanal']):
                    if values['Taxa_CarC'] == True:
                        Janela.DiariaCOMPACTO = int(values['Diaria'])
                        Janela.SemCOMPACTO = int(values['Semanal'])
                    if values['Taxa_CarM'] == True:
                        Janela.DiariaMEDIO = int(values['Diaria'])
                        Janela.SemMEDIO = int(values['Semanal'])
                    if values['Taxa_CarG'] == True:
                        Janela.DiariaGRANDE = int(values['Diaria'])
                        Janela.SemGRANDE = int(values['Semanal'])
                    if values['Taxa_CarS'] == True:
                        Janela.DiariaSUV = int(values['Diaria'])
                        Janela.SemSUV = int(values['Semanal'])
                    if values['Taxa_CarCAM'] == True: 
                        Janela.DiariaCAMINHAO = int(values['Diaria'])
                        Janela.SemCAMINHAO = int(values['Semanal'])

                    pyGui.popup("Atualizado")
                else:
                    pyGui.popup("Campos vazios")
                

            if win == window and event == 'ListarTaxas':
                window1 = Janela.listaTaxa()
                
            
            if win == window and event == 'CadastrarAluguel':
                at = None
                if values['Ativo'] == True:
                    at = True
                else:
                    at = False

                if(values['Data'] and values['idCar'] and values['NumDias'] and values['IdCli']):
                    if(verificaData(values) == True):
                        params = values['Data'], values['idCar'], values['NumDias'], at, False, True, values['IdCli']
                        cur.execute(sqlAlug, (params)) #usando tupla
                        con.commit()

                        pyGui.popup('Cadastrado')

                        atualizaAluga()
                        win['-myTableAluga'].update(values=Janela.Alugueis)
                else:
                    pyGui.popup('Não foi possivel cadastrar o Aluguel pois possui campos mal preechidos')

            if win == window and event == pyGui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break

            if win == window1 and event == pyGui.WIN_CLOSED:
                window1.close()

            if win == window and event == 'ListarCliente':
                sqlList = """select * from cliente"""
                cur.execute(sqlList)

                if cur.with_rows:
                    tuplas = cur.fetchall()
                    window1 = Janela.janelaBuscaCliente(tuplas)
            # window.hide()

            if win == window and event == 'ListarCarros':
                sqlList = """select * from carro"""
                cur.execute(sqlList)

                if cur.with_rows:
                    tuplas = cur.fetchall()
                    window1 = Janela.janelaBuscaCarro(tuplas)
                    
            if win == window1 and event == 'Voltar':    
                window1.close()
            
            if event == '-myTableAluga Double':
                sqlAux = """select * from carro where id = %s"""
                

                select_index = values['-myTableAluga'][0]
                global select_row
                select_row = Janela.Alugueis[select_index]

                cur.execute(sqlAux, (select_row[2],))

                window1 = Janela.JanelaStatus(select_row, cur.fetchone())
                
            if win == window1 and event == 'Finalizar':
                sqpUp= """update aluga set ativo = False, finalizado = True, inAberto = %s where Data_Init = %s and id_carro_fk = %s"""  
                aberto = False
                if(values['aberto'] == 'True'):
                    aberto = True

                params = aberto,select_row[0], select_row[2]
                cur.execute(sqpUp, params=(params))
                con.commit()

                atualizaAluga()
                window['-myTableAluga'].update(values=Janela.Alugueis)
                window1.close()
                
                
        cur.close()
        con.close() 
        window.close()
        return 0
    
    except Exception as e:
        con.rollback()
        print(e)
        pyGui.popup(f'[Error]{e}')
        return 1

   
   
if __name__ == '__main__':
# Event Loop to process "events" and get the "values" of the inputs
    con = mysql.connector.connect(option_files = 'config.cnf')
    #cria um cursor
    cur = con.cursor()
    sql = """insert into cliente(nome, telefone) values(%s, %s)"""
    sqlCar = """insert into carro (tipo, diaria, semanal, marca, modelo, ano) values(%s, %s, %s, %s, %s, %s)"""
    sqlAlug="""insert into aluga(Data_init, id_carro_fk, numeroDias, ativo, finalizado, inAberto, id_cliente_fk) values (%s, %s, %s, %s, %s, %s, %s)"""
    
    #nivelIsolamento == "Repeatable Read";

    atualizaAluga()
    window, window1 = Janela.janelaPrincipal(), None

    window['-myTableAluga'].bind("<Double-Button-1>", " Double")

    while (program(window, window1)) == 1:
        program(window, window1)
    
    cur.close()
    con.close()