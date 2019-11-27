import zipfile


def main():
    file_name = 'code.zip'

    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    print(alphabet)



    for i in range (len(alphabet)):
        pswd = ""
        pswd += alphabet[i]
        #print(pswd,"\n")
        for j in range (len(alphabet)):
            if len(pswd) > 1 :
                pswd = pswd[:1]
            pswd += alphabet[j]
            #print(pswd)

            for k in range (len(alphabet)):
                if len(pswd) > 2 :
                    pswd = pswd[:2]
                pswd += alphabet[k]
                #print(pswd,"\n")
                for o in range (len(alphabet)):
                    if len(pswd) > 3 :
                        pswd = pswd[:3]
                    pswd += alphabet[o]
                    #print(pswd,"\n")
                    for p in range (len(alphabet)):
                        if len(pswd) > 4 :
                            pswd = pswd[:4]
                        pswd += alphabet[p]
                        try:
                            #print(1)
                            with zipfile.ZipFile(file_name) as file:
                                file.extractall(pwd = bytes(pswd, 'utf-8'))
                            print(pswd)
                            break

                        except:
                            pass

if __name__ == '__main__': main()
