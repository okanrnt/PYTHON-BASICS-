#Returns the average of the grades entered and the letter grade.
class CalculateExamGrade:
    notes = list()
    dataResults = []
    copyList = []
    
    def enter_notes(name,note1,note2,note3):
        CalculateExamGrade.notes.append({name : {
            'note1' : note1,
            'note2' : note2,
            'note3' : note3
            }
            })
        
        return CalculateExamGrade.find_average(name)
    
    def letter_note(name,result): 
        if 85 <=result <=100:
            print('''{}'s letter note is AA.'''.format(name))
            CalculateExamGrade.dataResults.append('AA')
        elif 75 <=result <=84:
           print('''{}'s letter note is BB.'''.format(name))
           CalculateExamGrade.dataResults.append('BB')
        elif 60 <=result <=74:
            print('''{}'s letter note is CC.'''.format(name))
            CalculateExamGrade.dataResults.append('CC')
        elif 35 <=result <=59:
            print('''{}'s letter note is DD.'''.format(name))
            CalculateExamGrade.dataResults.append('DD')
        elif 0 <=result <=34:
            print('''{}'s letter note is FF.'''.format(name))
            CalculateExamGrade.dataResults.append('FF') 
        
        for j in CalculateExamGrade.notes:
            CalculateExamGrade.copyList.append(j)
        CalculateExamGrade.notes.clear()
    
    def find_average(name):  
        a = list(map(lambda x : x[name],CalculateExamGrade.notes))
        print('All results of the student {}'.format(a))
        for i in a:
            pass

        ort = [v for k,v in i.items()]
        result = int(sum(ort) / 3)
        print('''The average of {}'s tests is {}.'''.format(name,result))
        return CalculateExamGrade.letter_note(name,result)
    
    def displayAllStudentsResults():   
        print(CalculateExamGrade.copyList)
        
    def findData(letterNote):
        dR = CalculateExamGrade.dataResults.count(letterNote)
        print('The number of students taking {} : {}'.format(letterNote,dR))
        
        
CalculateExamGrade.enter_notes(name,note1,note2,note3)