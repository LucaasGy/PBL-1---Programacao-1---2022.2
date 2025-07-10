'''
************************************************************************************
Autor: Lucas Gabriel Cerqueira Santos Lima    Matrícula: 22211305
Componente Curricular: MI - Algoritmos
Concluido em: 21/09/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros
e apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de
código de outra autoria que não a minha está destacado com uma citação do autor e
a fonte do código, e estou ciente que estes trechos não serão considerados para fins
de avaliação.
************************************************************************************
'''
#Acumuladores e Contadores
menu = '1'
totalNORDESTE=0                                                                                                   #Área total reflorestada da Região Nordeste 
totalal=0 ; totalba=0 ; totalce=0 ; totalma=0 ; totalpb=0 ; totalpe=0 ; totalpi=0 ; totalrn=0 ; totalse=0         #Área total reflorestada por estado
contAL=0 ; contBA=0 ; contCE=0 ; contMA=0 ; contPB=0 ; contPE=0 ; contPI=0 ; contRN=0 ; contSE=0                  #Quantidade de áreas reflorestada por estado
total_bambugigante=0 ; total_cajueiro=0 ; total_coqueiro=0 ; total_dende=0 ; total_ipe=0 ; total_mangueira=0      #Área total reflorestada por cada tipo de árvore
contBambugigante=0 ;contCajueiro=0 ; contCoqueiro=0 ; contDende=0; contIpe=0 ; contMangueira=0                    #Quantidade de cada tipo de árvore usada no reflorestamento
maiorAREA=0                                                                                                       #Maior área cadastrada
Mcodigo='' ; Mcidade='' ; Mestado='' ; Marea='' ; Marvore=''                                                      #Informações da maior área cadastrada
codigos = []                                                                                                      #Lista para adicionar o código de cada área cadastrada

#Menu
while menu != '0':
    
    menu= input('-------------------------------------------------------------------\n            SISTEMA DE GERENCIAMENTO DE REFLORESTAMENTO\n-------------------------------------------------------------------\n             ---- 1. Cadastrar área reflorestada ---- \n             ---- 2.         Relatório           ---- \n             ---- 0.           Sair              ---- \n-------------------------------------------------------------------\n>> ')
    
    #Se escolher sair
    if menu == '0':
        print('-------------------------------------------------------------------\n                      #### Saindo... ####\n-------------------------------------------------------------------')
         
    #Se escolher se cadastrar   
    elif menu == '1': 
        
        #Código da área reflorestada (caso já tenha um código atribuído a um cadastro, pede um código novamente)
        codigo = int(input('-------------------------------------------------------------------\n1. Digite um código numérico para a área reflorestada: '))
        while codigo in codigos:
            codigo = int(input('Código já atribuido a uma área reflorestada. Tente novamente: '))
        codigos.append(codigo)
        
        #Cidade da área reflorestada
        cidade = input('-------------------------------------------------------------------\n2. Digite a Cidade da área: ')
        
        #Estado da área reflorestada (caso digite uma sigla inválida, pede uma sigla novamente)
        estado = input('-------------------------------------------------------------------\n3. Digite a sigla do Estado da área \n\n| Alagoas = AL  | Bahia = BA               | Ceará = CE      |\n| Maranhão = MA | Paraíba = PB             | Pernambuco = PE |\n| Piauí = PI    | Rio Grande do Norte = RN | Sergipe = SE    |\n\nSigla: ').lower()
        while estado != 'al' and  estado != 'ba' and  estado != 'ce' and estado != 'ma' and estado != 'pb'and estado != 'pe' and  estado != 'pi' and estado != 'rn' and  estado != 'se':                             
            estado = input ('Sigla inválida. Tente novamente: ').lower()
        
        #Dimensões para calcular a área (caso digite uma base ou altura menor ou igual a 0, pede a base e altura novamente)
        base = float(input('-------------------------------------------------------------------\n4. Digite as dimensões da área em quilômetro\nBase: '))  
        while base <= 0:
            base = float(input('Dimensão inválida. Tente novamente: '))
        altura = float(input('Altura: '))
        while altura <= 0:
            altura = float(input('Dimensão inválida. Tente novamente: '))
        
        #Tipo de árvore reflorestada (caso digite um tipo de árvore inválido, pede o tipo de árvore novamente)
        arvore = input('-------------------------------------------------------------------\n5. Digite o tipo de árvore reflorestada\n\n| Bambu Gigante | Coqueiro | Ipê       |\n| Cajueiro      | Dendê    | Mangueira |\n\nTipo de árvore: ').lower()
        while arvore != 'cajueiro' and arvore != 'mangueira' and arvore != 'dende' and arvore != 'dendê' and arvore != 'coqueiro' and arvore != 'bambu gigante' and arvore != 'ipe' and arvore != 'ipê':
            arvore = input('Tipo de árvore inválida. Tente novamente: ').lower()
        
        #Calcula o valor da área reflorestada e soma a área total da região nordeste
        totalNORDESTE += base*altura
                
        #Dependendo do estado escolhido, irá calcular a área total de cada estado e a quantidade de área reflorestada de cada estado
        if estado == 'al':
            totalal += base*altura
            contAL += 1             
        elif estado == 'ba':
            totalba += base*altura
            contBA += 1       
        elif estado == 'ce':           
            totalce += base*altura
            contCE += 1       
        elif estado == 'ma':
            totalma += base*altura
            contMA += 1      
        elif estado == 'pb':          
            totalpb += base*altura 
            contPB += 1     
        elif estado == 'pe':            
            totalpe += base*altura 
            contPE += 1       
        elif estado == 'pi':          
            totalpi += base*altura 
            contPI += 1       
        elif estado == 'rn':           
            totalrn += base*altura
            contRN += 1       
        elif estado == 'se':            
            totalse += base*altura
            contSE+=1
        
        #Dependendo do tipo da árvore escolhida, irá calcular o total de área reflorestada por cada tipo de árvore e a quantidade dos tipos de árvores reflorestadas
        if arvore == 'bambu gigante':
            total_bambugigante += base*altura
            contBambugigante+=1        
        elif arvore == 'cajueiro':
            total_cajueiro += base*altura
            contCajueiro+=1       
        elif arvore == 'coqueiro':
            total_coqueiro += base*altura
            contCoqueiro+=1
        elif arvore == 'dende' or arvore == 'dendê':
            total_dende += base*altura
            contDende+=1           
        elif arvore == 'ipe' or arvore == 'ipê':
            total_ipe += base*altura
            contIpe+=1        
        elif arvore == 'mangueira':          
            total_mangueira += base*altura
            contMangueira+=1
            
        #Guarda as informações da maior area cadastrada
        if (base*altura) > maiorAREA:      
            maiorAREA = base*altura
            Mcodigo = codigo
            Mcidade = cidade
            Mestado = estado
            Marea = base*altura
            Marvore = arvore  

        #Finaliza cadastro e volta pro menu
        print('-------------------------------------------------------------------\n  #### Área cadastrada com sucesso. Reflorestar é reviver!!! ####')
                  
    #Se escolher pedir o relatório
    elif menu == '2': 
       
        #Se não tiver nenhuma área cadastrada, exibe erro e volta pro menu
        if totalNORDESTE == 0:
            print('-------------------------------------------------------------------\n## Dados insuficientes. Cadastre uma área reflorestada primeiro! ##')
        
        #Se tiver pelo menos uma área cadastrada, exibe o relatório solicitado
        else:
            print('-------------------------------------------------------------------\n                       #### Relatório ####')
            print(f'-------------------------------------------------------------------\n            °Área total reflorestada da Região Nordeste° \n\n{round(totalNORDESTE,2)} km²')
            print(f'-------------------------------------------------------------------\n                °Área total reflorestada por estado° \n\nAlagoas: {round(totalal, 2)} km²\nBahia: {round(totalba, 2)} km²\nCeará: {round(totalce, 2)} km²\nMaranhão: {round(totalma, 2)} km²\nParaíba: {round(totalpb, 2)} km²\nPernambuco: {round(totalpe, 2)} km²\nPiauí: {round(totalpi, 2)} km²\nRio Grande do Norte: {round(totalrn, 2)} km²\nSergipe: {round(totalse, 2)} km²')            
            print(f'-------------------------------------------------------------------\n         °Área total reflorestada por cada tipo de árvore° \n\nBambum Gigante: {round(total_bambugigante,2)} km²\nCajueiro: {round(total_cajueiro,2)} km²\nCoqueiro: {round(total_coqueiro,2)} km²\nDendê: {round(total_dende,2)} km²\nIpê: {round(total_ipe,2)} km²\nMangueira: {round(total_mangueira,2)} km²')
            print(f'-------------------------------------------------------------------\n   °Total de quantas vezes cada tipo de árvore foi reflorestada°\n\nBambu Gigante: {contBambugigante}\nCajueiro: {contCajueiro}\nCoqueiro: {contCoqueiro}\nDendê: {contDende}\nIpê: {contIpe}\nMangueira: {contMangueira}')
            #Tipo de árvore mais usado no reflorestamento (quantidade)
            print(f'-------------------------------------------------------------------\n      °Tipo(s) de árvore(s) mais usado(s) no reflorestamento°\n')
            if contBambugigante>=contCajueiro and contBambugigante>=contCoqueiro and contBambugigante>=contDende and contBambugigante>=contIpe and contBambugigante>=contMangueira:
                print(f'Bambu gigante: {contBambugigante} uso(s)')
            if contCajueiro>=contBambugigante and contCajueiro>=contCoqueiro and contCajueiro>=contDende and contCajueiro>=contIpe and contCajueiro>=contMangueira:
                print(f'Cajueiro: {contCajueiro} uso(s)')
            if contCoqueiro>=contBambugigante and contCoqueiro>=contCajueiro and contCoqueiro>=contDende and contCoqueiro>=contIpe and contCoqueiro>=contMangueira:
                print(f'Coqueiro: {contCoqueiro} uso(s)')
            if contDende>=contBambugigante and contDende>=contCajueiro and contDende>=contCoqueiro and contDende>=contIpe and contDende>=contMangueira:
                print(f'Dendê: {contDende} uso(s)')
            if contIpe>=contBambugigante and contIpe>=contCajueiro and contIpe>=contCoqueiro and contIpe>=contDende and contIpe>=contMangueira:
                print(f'Ipê: {contIpe} uso(s)')
            if contMangueira>=contBambugigante and contMangueira>=contCajueiro and contMangueira>=contCoqueiro and contMangueira>=contDende and contMangueira>=contIpe:
                print(f'Mangueira: {contMangueira} uso(s)')
            #Tipo de árvore menos usado no reflorestamento (quantidade)
            print(f'-------------------------------------------------------------------\n     °Tipo(s) de árvore(s) menos usado(s) no reflorestamento°\n')
            if contBambugigante<=contCajueiro and contBambugigante<=contCoqueiro and contBambugigante<=contDende and contBambugigante<=contIpe and contBambugigante<=contMangueira:
                print(f'Bambu gigante: {contBambugigante} uso(s)')
            if contCajueiro<=contBambugigante and contCajueiro<=contCoqueiro and contCajueiro<=contDende and contCajueiro<=contIpe and contCajueiro<=contMangueira:
                print(f'Cajueiro: {contCajueiro} uso(s)')
            if contCoqueiro<=contBambugigante and contCoqueiro<=contCajueiro and contCoqueiro<=contDende and contCoqueiro<=contIpe and contCoqueiro<=contMangueira:
                print(f'Coqueiro: {contCoqueiro} uso(s)')
            if contDende<=contBambugigante and contDende<=contCajueiro and contDende<=contCoqueiro and contDende<=contIpe and contDende<=contMangueira:
                print(f'Dendê: {contDende} uso(s)')
            if contIpe<=contBambugigante and contIpe<=contCajueiro and contIpe<=contCoqueiro and contIpe<=contDende and contIpe<=contMangueira:
                print(f'Ipê: {contIpe} uso(s)')
            if contMangueira<=contBambugigante and contMangueira<=contCajueiro and contMangueira<=contCoqueiro and contMangueira<=contDende and contMangueira<=contIpe:
                print(f'Mangueira: {contMangueira} uso(s)')        
            print(f'-------------------------------------------------------------------\n       °Informações da maior extensão de área reflorestada° \n\nCódigo: {Mcodigo} \nCidade: {Mcidade.title()} \nSigla do Estado: {Mestado.upper()} \nÁrea: {round(Marea,2)} km²\nTipo de Árvore: {Marvore.title()}')
            print(f'-------------------------------------------------------------------\n             °Total de áreas reflorestadas por estado° \n\nAlagoas: {contAL}\nBahia: {contBA}\nCeará: {contCE}\nMaranhão: {contMA}\nParaíba: {contPB}\nPernambuco: {contPE}\nPiauí: {contPI}\nRio Grande do Norte: {contRN}\nSergipe: {contSE}')                
            #Estado mais reflorestado (área)
            print(f'-------------------------------------------------------------------\n                 °Estado(s) mais reflorestado(s)°\n')
            if totalal>=totalba and totalal>=totalce and totalal>=totalma and totalal>=totalpb and totalal>=totalpe and totalal>=totalpi and totalal>=totalrn and totalal>=totalse:
                print(f'Alagoas: {round(totalal, 2)} km²')
            if totalba>=totalal and totalba>=totalce and totalba>=totalma and totalba>=totalpb and totalba>=totalpe and totalba>=totalpi and totalba>=totalrn and totalba>=totalse:
                print(f'Bahia: {round(totalba, 2)} km²')
            if totalce>=totalal and totalce>=totalba and totalce>=totalma and totalce>=totalpb and totalce>=totalpe and totalce>=totalpi and totalce>=totalrn and totalce>=totalse:
                print(f'Ceará: {round(totalce, 2)} km²')
            if totalma>=totalal and totalma>=totalba and totalma>=totalce and totalma>=totalpb and totalma>=totalpe and totalma>=totalpi and totalma>=totalrn and totalma>=totalse:
                print(f'Maranhão: {round(totalma, 2)} km²')
            if totalpb>=totalal and totalpb>=totalba and totalpb>=totalce and totalpb>=totalma and totalpb>=totalpe and totalpb>=totalpi and totalpb>=totalrn and totalpb>=totalse:
                print(f'Paraíba: {round(totalpb, 2)} km²')
            if totalpe>=totalal and totalpe>=totalba and totalpe>=totalce and totalpe>=totalma and totalpe>=totalpb and totalpe>=totalpi and totalpe>=totalrn and totalpe>=totalse:
                print(f'Pernambuco: {round(totalpe, 2)} km²')
            if totalpi>=totalal and totalpi>=totalba and totalpi>=totalce and totalpi>=totalma and totalpi>=totalpb and totalpi>=totalpe and totalpi>=totalrn and totalpi>=totalse:
                print(f'Piauí: {round(totalpi, 2)} km²')
            if totalrn>=totalal and totalrn>=totalba and totalrn>=totalce and totalrn>=totalma and totalrn>=totalpb and totalrn>=totalpe and totalrn>=totalpi and totalrn>=totalse:
                print(f'Rio grande do Norte: {round(totalrn, 2)} km²')
            if totalse>=totalal and totalse>=totalba and totalse>=totalce and totalse>=totalma and totalse>=totalpb and totalse>=totalpe and totalse>=totalpi and totalse>=totalrn:
                print(f'Sergipe: {round(totalse, 2)} km²')
            #Estado menos reflorestado (área)
            print(f'-------------------------------------------------------------------\n                 °Estado(s) menos reflorestado(s)°\n')
            if totalal<=totalba and totalal<=totalce and totalal<=totalma and totalal<=totalpb and totalal<=totalpe and totalal<=totalpi and totalal<=totalrn and totalal<=totalse:
                print(f'Alagoas: {round(totalal, 2)} km²')
            if totalba<=totalal and totalba<=totalce and totalba<=totalma and totalba<=totalpb and totalba<=totalpe and totalba<=totalpi and totalba<=totalrn and totalba<=totalse:
                print(f'Bahia: {round(totalba, 2)} km²')
            if totalce<=totalal and totalce<=totalba and totalce<=totalma and totalce<=totalpb and totalce<=totalpe and totalce<=totalpi and totalce<=totalrn and totalce<=totalse:
                print(f'Ceará: {round(totalce, 2)} km²')
            if totalma<=totalal and totalma<=totalba and totalma<=totalce and totalma<=totalpb and totalma<=totalpe and totalma<=totalpi and totalma<=totalrn and totalma<=totalse:
                print(f'Maranhão: {round(totalma, 2)} km²')
            if totalpb<=totalal and totalpb<=totalba and totalpb<=totalce and totalpb<=totalma and totalpb<=totalpe and totalpb<=totalpi and totalpb<=totalrn and totalpb<=totalse:
                print(f'Paraíba: {round(totalpb, 2)} km²')
            if totalpe<=totalal and totalpe<=totalba and totalpe<=totalce and totalpe<=totalma and totalpe<=totalpb and totalpe<=totalpi and totalpe<=totalrn and totalpe<=totalse:
                print(f'Pernambuco: {round(totalpe, 2)} km²')
            if totalpi<=totalal and totalpi<=totalba and totalpi<=totalce and totalpi<=totalma and totalpi<=totalpb and totalpi<=totalpe and totalpi<=totalrn and totalpi<=totalse:
                print(f'Piauí: {round(totalpi, 2)} km²')
            if totalrn<=totalal and totalrn<=totalba and totalrn<=totalce and totalrn<=totalma and totalrn<=totalpb and totalrn<=totalpe and totalrn<=totalpi and totalrn<=totalse:
                print(f'Rio grande do Norte: {round(totalrn, 2)} km²')
            if totalse<=totalal and totalse<=totalba and totalse<=totalce and totalse<=totalma and totalse<=totalpb and totalse<=totalpe and totalse<=totalpi and totalse<=totalrn:
                print(f'Sergipe: {round(totalse, 2)} km²')

    #Se escolher algum numero diferente de 0, 1 e 2, exibe erro e volta pro menu
    else:                                            
        print('-------------------------------------------------------------------\n      #### Escolha inválida. Esta opção não está no menu! ####')