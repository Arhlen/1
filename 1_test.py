import main

def get_pas_count():
    line = ['33,1,3,"Glynn, Miss. Mary Agatha",female,,0,0,335677,7.75,,Q'
            '34,0,2,"Wheadon, Mr. Edward H",male,66,0,0,C.A. 24579,10.5,,S',
            '35,0,1,"Meyer, Mr. Edgar Joseph",male,28,1,0,PC 17604,82.1708,,C',
            '36,0,1,"Holverson, Mr. Alexander Oskar",male,42,1,0,113789,52,,S',
            '37,1,3,"Mamee, Mr. Hanna",male,,0,0,2677,7.2292,,C',
            '38,0,3,"Cann, Mr. Ernest Charles",male,21,0,0,A./5. 2152,8.05,,S',
            '39,0,3,"Vander Planke, Miss. Augusta Maria",female,18,2,0,345764,18,,S',
            '40,1,3,"Nicola-Yarred, Miss. Jamila",female,14,1,0,2651,11.2417,,C']
    actual = get_pas_count(line, 1)
    expected = (2, 0, 2)
    print(actual)
    assert actual == expected