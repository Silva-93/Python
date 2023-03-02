""" 
    Criando arquivos com Python + Context Manager with
    Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
    Modos:
        r (leitura), 
        
        w (escrita e sobrescreve), 
        
        x (para criação)
    
        a (escreve ao final), 
        
        b (binário)
    
        t (modo texto), 
        
        + (leitura e escrita)
    
    Context manager - with (abre e fecha)
    
    Métodos úteis
        write, read (escrever e ler)

        writelines (escrever várias linhas)
        
        seek (move o cursor)
    
        readline (ler linha)
    
        readlines (ler linhas)
    
    Vamos falar mais sobre o módulo os, mas:
    
        os.remove ou unlink - apaga o arquivo
    
        os.rename - troca o nome ou move o arquivo
    
    Vamos falar mais sobre o módulo json, mas:
    
        json.dump = Gera um arquivo json
    
        json.load
"""
import os


file_path = r'C:\Users\Jouber\Desktop\work_python_file.txt'

with open(file_path, 'w+', encoding='utf-8') as file:
    file.write('Linha 1\n')  # Escrevendo dentro do arquivo.
    file.write('Linha 2\n')  
    file.write('Atenção\n')  

    file.writelines(
        ('Linha 3\n', 'Linha 4\n')  # Escrevendo mais de uma linha no arquivo.
    )


with open(file_path, 'r') as file:
    print(file.read())  # Lendo o arquivo


with open(file_path, 'a') as file:
    file.write('Escrevendo no final do arquivo.')  #  Escrevendo no final do arquivo.


#os.remove(file_path)  # Apagando o arquivo

#os.unlink(file_path)  # Apagando o arquivo