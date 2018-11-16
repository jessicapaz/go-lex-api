import subprocess


code = '''
import "fmt"

if 2 < 2 {
    if 2 < 2 {
        3 + 3212
    }
    func teste (i int){
        return x = i + 2
    }
    for i=2; 2<2; i++{
        2 + 2
    }
}
'''
pipe = subprocess.Popen(f"python syntax_analysis.py {code}", shell=True, stdout=subprocess.PIPE).stdout
output = pipe.read()
print(output.decode('utf-8'))

