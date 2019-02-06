import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'   # >> ./blockchain/ получаем дирректорию, где хранятся блоки

def get_hash(filename):
    
    file = open(blockchain_dir + filename, 'rb').read() #read binary   
    return hashlib.md5(file).hexdigest()

def get_files():
    files = os.listdir(blockchain_dir) #получаем список файлов в папке в не отсортированном виде
    return sorted([int(i) for i in files]) #создаем с помощью генератора списков новый уже отсортированный список (предварительно изменить тип из строк в целые числа)
     

#проверка целостности блоков
def check_integrity():
    
#    1. Считаем хэш предыдущего блока
#    2. Вычислить хэш предыдущего блока
#    3. Сравнить полученные данные 
    files = get_files() # [1, 2, 3, 4, 5, ..]
    
    results = []
    
    for file in files[1:]: # [1, 2, 3, 4, 5, ..]
        f = open(blockchain_dir + str(file))  #'2'      
        h = json.load(f)['Хэш предыдущего блока']  #считываем хэш(n-1) в блоке n
        
        prev_block=str(file-1)        
        actual_hash = get_hash(prev_block) 
                
        if h == actual_hash:
            res = 'Ок'
        else:
            res = 'Ошибка'
            
#        print('Состояние блока {}: {}'.format(prev_block, res))
       
        results.append({'Блок': prev_block, 'состояние': res} )
        
    return results
        
#        print(h) #выводим значения хэш в каждом из файлов (то есть из блока 2 вытаскиваем значение "hash", который равен хэшу блока 1)
        
    

def write_block(name, amount, to_whom, prev_hash=''):    
    files = get_files()   
     
    prev_block = files[-1] #номер последнего блока (файла) в папке
    
    filename = str(prev_block + 1) #создаем новый блок (предыдущий + 1) (поскольку речь идет об имени файла, приводим всё в тип str)
    
    prev_hash = get_hash(str(prev_block)) #считаем хэш предыдущего блока. ф-ия get_hash получает название файла
        
    data = {'Кто': name,
           'Сколько': amount,
           'Кому': to_whom,
           'Хэш предыдущего блока': prev_hash} #создаем переменную "data"
    
    with open(blockchain_dir + filename, 'w') as file:    #открываем файл "test" по нужному пути с возможностью "записи" и сохраняем как файл (после файл будет закрыт)
        json.dump(data, file, indent = 4, ensure_ascii=False) #сохраняем содержимое переменной "data" в переменную "file"
        

def main():
#    write_block(name='Матвей', amount=5, to_whom='Игорь')
    print(check_integrity())
    

if __name__ == "__main__":
       main()
