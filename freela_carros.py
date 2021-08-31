from selenium import webdriver
import time

# codigo para rodar o scraping no chrome invisivel
options = webdriver.ChromeOptions()
options.add_argument("--headless")

letra_A = 'https://classiccardatabase.com/prewar-models/car-models-A.php'
count = 1

for id_page in range(1,2):
    # abrir chrome Driver
    pathChromeDrive = 'C:\chrome\chromedriver.exe'
    driver = webdriver.Chrome(pathChromeDrive,chrome_options=options)
    driver2 = webdriver.Chrome(pathChromeDrive,chrome_options=options)
    # baixar o site
    driver.get(letra_A)
    time.sleep(3)

    x = 0
    fim_coluna = [590,557]
    for coluna in range(2,3):
        saida = ''
        saida_erro = ''
        for i in range(73,fim_coluna[coluna-2]):
            x=x+1
            if x == 110:
                break
            try:
                # pegar o nome e link do carro
                link_path = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div['+str(coluna)+']/a['+str(i)+']')
                link_text = link_path.text
                link_url = link_path.get_attribute("href")

                if link_text[0:4].isdigit():
                    link_text = link_text
                else:
                    print('text', link_text)
                    continue
                saida = str(i)+ '\t'
                saida += link_text+str('\t')
                saida += link_url+str('\t')
                saida_erro = link_text

                # pega o ano
                year = link_text[0:4]
                link_text = link_text[5:]
                saida+= year + '\t'

                # pega a empresa
                id = link_text.index(' ')
                company = link_text[0:id]
                saida += company + '\t'


                # acessar o link
                driver2.get(link_url)
                final_info=[46,44]
                for tabela in range(0,2):
                    for info in range(1,final_info[tabela]):
                        title = ''
                        value = ''
                        try:
                            info_title = driver2.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div['+str(tabela+1)+']/table/tbody/tr['+str(info)+']/td[1]')
                            title = info_title.text
                        except Exception as e:  # work on python 3.x
                            print('Erro: ' + str(e))

                        try:
                            if ( tabela == 1 and info == 42 ) == False:
                                info_value = driver2.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div['+str(tabela+1)+']/table/tbody/tr[' + str(info) + ']/td[2]')
                                value = info_value.text
                        except Exception as e:  # work on python 3.x
                            erro = str(e).replace('\n', ' ')
                            print('Erro: ', saida_erro, erro)
                            break
                        saida += str(title+':'+value)+'\t'


                '''
                # se a vaga é recente aparereca a string NOVA
                name = name.replace('\nNOVA','')
                print(count, name)
                count+=1
                time.sleep(1)
                    
                # pegar o link da vaga
                link_path = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(x)+']/a')
                link = link_path.get_attribute("href")
                print(link)
    
    
                # pega as skills da  vaga
                skills = []
                for j in range(1, 10):
                    try:
                        skill = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(x)+']/a/div/div[2]/div/div[2]/span['+str(j)+']')
                        skills.append(skill.text)
                    except:
                        break
                    j+=1
                print(skills)
    
                # pega as informacoes  da  vaga
                infos = []
                for j in range(1,10):
                    try:
                        info = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[' + str(x) + ']/a/div/div[2]/div/div[1]/span['+str(j)+']')
                        infos.append(info.text)
                    except:
                        break
                print(infos)
                
            '''

            # se for uma propaganda, vai dar um erro
            # então passa para o proximo loop, e diminui o contador
            except Exception as e:  # work on python 3.x
                erro = str(e).replace('\n',' ')
                print('Erro: ', saida_erro , erro)

                #i-=1
            print(saida)

    # encerra o driver

    driver.quit()
    driver2.quit()
