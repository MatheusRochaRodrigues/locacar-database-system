import os
import PySimpleGUI as pyGui
from datetime import datetime, date, timedelta

DiariaCOMPACTO = 90
DiariaMEDIO = 120
DiariaGRANDE = 320
DiariaSUV = 116
DiariaCAMINHAO = 650
SemCOMPACTO = DiariaCOMPACTO * 7 -100
SemMEDIO = DiariaMEDIO * 7 -100
SemGRANDE = DiariaGRANDE * 7 -100
SemSUV = DiariaSUV * 7 -100
SemCAMINHAO = DiariaCAMINHAO * 7 -100


td=[]
Alugueis = []
cabecalhos = ['Nome', 'Telefone']
toprow = ['Id', 'Nome', 'Telefone']
dawnrow = ['Id','Tipo', 'Diaria', 'Semanal', 'Marca', 'Modelo', 'Ano']
alugaRow = ['DataInicio','DataFinal', 'idCarFK', 'numDias', 'ativo', 'finish', 'InAberto', 'idClienteFK']


def blank_frame():
    return pyGui.Frame("", [[                    
                    ]], pad=(5, 3), expand_x=True, expand_y=True, border_width=0)


def janelaBuscaCliente(values):
    rows = []
    for tup in values:
        rows.append([tup[0], tup[1], tup[2]])

    pyGui.theme('Reddit')
    layout = [            
                    [pyGui.Button('Voltar')],
                    [pyGui.Table(values=rows, headings=toprow, key='-myTable',justification='center',expand_x=True,
   expand_y=True)]
                    ]
    return pyGui.Window('busca',  layout, margins=(2, 2),size=(600, 500), finalize=True)


def janelaBuscaCarro(values):
    rows = []
    for tup in values:
        rows.append([tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6]])

    pyGui.theme('Reddit')
    layout = [
                    [pyGui.Button('Voltar')],
                    [pyGui.Table(values=rows, headings=dawnrow, key='-myTable',justification='center',expand_x=True,
   expand_y=True)]
                    ]
    
    return pyGui.Window('busca',  layout, margins=(2, 2),size=(600, 500), finalize=True)

def BuscaAluguel(values):
    Alugueis.clear()
    
    for tup in values:
        #print(f"{tup[4]}")
        diasTotal = tup[0]+timedelta(days=tup[2])
        Alugueis.append([tup[0], diasTotal, tup[1], tup[2], tup[3], tup[4], tup[5], tup[6]])


def JanelaStatus(select_row, dado):
    pyGui.theme('Reddit')
    aux0 = select_row[0].strftime('%Y-%m-%d')
    aux1 = select_row[1].strftime('%Y-%m-%d')
    popup_message = "Name: " + aux0 + "\n" + "Address: " + aux1 + "id car = \n" + str(select_row[2]) + "\n" 
    #print(popup_message)
    #pyGui.popup(popup_message)
    # print(selected_row)
    auxPreco = 0
    Dias = select_row[3] - 7
    diaria = 0.0
    semanal = 0.0

    if dado[1] == 'COMPACTO':
        diaria = DiariaCOMPACTO
        semanal = SemCOMPACTO
    if dado[1] == 'MÉDIO':
        diaria = DiariaMEDIO
        semanal = SemMEDIO
    if dado[1] == 'GRANDE':
        diaria = DiariaGRANDE
        semanal = SemGRANDE
    if dado[1] == 'SUV':
        diaria = DiariaSUV
        semanal = SemSUV
    if dado[1] == 'CAMINHÃO': 
        diaria = DiariaCAMINHAO
        semanal = SemCAMINHAO
    
    while Dias > 0:
        auxPreco += semanal
        Dias -= 7
    auxPreco += diaria * (select_row[3] % 7)

    status = [  
                    [pyGui.Text('Id_Car: '+str(dado[0]))],
                    [pyGui.Text('Tipo: '+str(dado[1]))],
                    [pyGui.Text('Marca: '+str(dado[4]))],
                    [pyGui.Text('Modelo: '+str(dado[5]))],
                    [pyGui.Text('Ano: '+str(dado[6]))],
    
                    [pyGui.Text('Diaria '+str(dado[2]))],
                    [pyGui.Text('Semanal '+str(dado[3]))],
                    [pyGui.Text('NumeroDeDias: '+str(select_row[3]))],
                    [pyGui.Text(f'PreçoFinal: {auxPreco}')],
                    [pyGui.Frame('InAberto', [
                    [   pyGui.Radio('Aberto','rd_bread', key ='aberto'),
                        pyGui.Radio('Fechar','rd_bread', key='!aberto',default=True)
                    ]])],
                    [pyGui.Button('Voltar'), pyGui.Button('Finalizar')]
    ]                                 
    return pyGui.Window('Status',  status, margins=(2, 2),size=(600, 500), finalize=True)

def listaTaxa():
    pyGui.theme('Reddit')
    status = [  
                    [pyGui.Text('COMPACTO   diaria: '+str(DiariaCOMPACTO)+'     semanal: '+str(SemCOMPACTO))],
                    [pyGui.Text('MÉDIO      diaria: '+str(DiariaMEDIO)+'        semanal: '+str(SemMEDIO))],
                    [pyGui.Text('GRANDE     diaria: '+str(DiariaGRANDE)+'       semanal: '+str(SemGRANDE))],
                    [pyGui.Text('SUV        diaria: '+str(DiariaSUV)+'          semanal: '+str(SemSUV))],
                    [pyGui.Text('CAMINHÃO   diaria: '+str(DiariaCAMINHAO)+'     semanal: '+str(SemCAMINHAO))],
                    [pyGui.Button('Voltar')]
            ]                                
    return pyGui.Window('Status',  status, margins=(2, 2),size=(600, 500), finalize=True)


def janelaPrincipal ():
    pyGui.theme('Reddit')

    layout5 = pyGui.Frame("", [
        [pyGui.Text('Cadastro de Taxas de Aluguel')],
                [pyGui.Text('Diaria'), pyGui.InputText(size=(20), key='Diaria')],
                [pyGui.Text('Semanal'), pyGui.InputText(size=(20), key='Semanal')],
                [pyGui.Frame('Tipo', [
                    [   pyGui.Radio('COMPACTO','rd_bread1', key ='Taxa_CarC', default=True),
                        pyGui.Radio('MÉDIO','rd_bread1', key='Taxa_CarM'),
                        pyGui.Radio('GRANDE','rd_bread1', key='Taxa_CarG'),
                        pyGui.Radio('SUV','rd_bread1', key='Taxa_CarS'),
                        pyGui.Radio('CAMINHAO','rd_bread1', key='Taxa_CarCAM')
                    ]
                    ])
                ],
                [pyGui.Button('AtualizarTaxa'), pyGui.Button('ListarTaxas')]
                                ], pad=(5, 3), expand_x=True, expand_y=True, border_width=2)

    layout4 = pyGui.Frame("", [
                    [pyGui.Table(values=Alugueis, headings=alugaRow, key='-myTableAluga',enable_events=True, expand_x=True,
   expand_y=True,justification='center')]
                    ], pad=(5, 3), expand_x=True, expand_y=True, border_width=0,)

    layout1 = pyGui.Frame("", [
            [pyGui.Text('Cadatrar cliente')],
                    [pyGui.Text('Nome'), pyGui.InputText(size=(20), key='nomeC')],
                    [pyGui.Text('Telefone'), pyGui.InputText(size=(20), key='telC')],
                    [pyGui.Button('CadastrarCliente'), pyGui.Button('Cancel'), pyGui.Button('ListarCliente')]
                                ], pad=(5, 3), expand_x=True, expand_y=True, border_width=2)
        
    layout2 = pyGui.Frame("", [
        [pyGui.Text('Cadastro Carro')],
                [pyGui.Text('Marca'), pyGui.InputText(size=(20), key='Marca')],
                [pyGui.Text('Modelo'), pyGui.InputText(size=(20), key='Modelo')],
                [pyGui.Text('ano'), pyGui.InputText(size=(20), key='ano')],
                [pyGui.Frame('Tipo', [
                    [   pyGui.Radio('COMPACTO','rd_bread2', key ='Tipo_CarC', default=True),
                        pyGui.Radio('MÉDIO','rd_bread2', key='Tipo_CarM'),
                        pyGui.Radio('GRANDE','rd_bread2', key='Tipo_CarG'),
                        pyGui.Radio('SUV','rd_bread2', key='Tipo_CarS'),
                        pyGui.Radio('CAMINHAO','rd_bread2', key='Tipo_CarCAM')
                    ]
                    ])
                ],

                [pyGui.Button('CadastrarCarro'), pyGui.Button('ListarCarros')]
                                
                                ], pad=(5, 3), expand_x=True, expand_y=True, border_width=2)
        #interface visual

    layout3 = pyGui.Frame("", [
        [pyGui.Text('Cadastro Aluguel')],
                [pyGui.Text('Data-> YYYY-MM-DD'), pyGui.InputText(size=(20), key='Data')],
                [pyGui.Text('id_Carro'), pyGui.Input(size=(20), key='idCar')],
                [pyGui.Text('Numero Dias'), pyGui.Input(size=(20), key='NumDias')],
                #[pyGui.Text('finalizado'), pyGui.InputText(size=(20), key='Fin')],
                [pyGui.Text('id_cliente_fk'), pyGui.InputText(size=(20), key='IdCli')],
                [pyGui.Frame('Ativo', [
                    [   pyGui.Radio('Sim','rd_bread', key ='Ativo', default=True),
                        pyGui.Radio('Não','rd_bread', key='!Ativo'),
                    ]
                    ])],

                [pyGui.Button('CadastrarAluguel')]
                                
                                ], pad=(5, 3), expand_x=True, border_width=2)

    layout_frame1 = [
            [layout1], [layout2],[layout5]
        ]
        
    layout_frame2 = [[layout3],[layout4]]

        #------------------------------------------------------------------------
    layout = [
        [pyGui.Frame("Cadastros_Listas", layout_frame1, size=(550, 640)),
        pyGui.Frame("ControleDeAlugueis", layout_frame2, size=(850, 640), title_location=pyGui.TITLE_LOCATION_TOP)],]
    

    return pyGui.Window("Locadora", layout, margins=(2, 2), finalize=True)



