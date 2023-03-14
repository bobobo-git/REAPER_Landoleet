import requests
import clipboard as c

out=""
versioncount=0
url = 'https://www.landoleet.org/whatsnew.txt'
content=requests.get(url).text

for x in range(0, 333):
    testline=content.splitlines()[x]
    if (testline[0:1])=='v':
        version=testline
        versioncount += 1
    if versioncount==1:
        line=testline.strip()
        if line!="":
            #print(line.split('[t=]'[2]))
            if line[0:1]=='*':
                newline ='[B][COLOR="INDIGO"]'+line.split(':')[0]+':[/COLOR][/B]'+line.split(':')[1]+'\n'
            elif line[0:1]=='+':
                newline ='[B][COLOR="GREEN"]'+line.split(':')[0]+':[/COLOR][/B]'+line.split(':')[1]+'\n'
            elif line[0:1]=='#':
                newline ='[B][COLOR="BLUE"]'+line.split(':')[0]+':[/COLOR][/B]'+line.split(':')[1]+'\n'
            else:
                newline ='[B][COLOR="BLACK"]'+line+'[/COLOR][/B]'+'\n'
            if newline.find('[t=')>0:
                val=newline.split('[t=')[1].split(']')[0]
                newline=newline.split('[t=')[0]+'[URL="https://forum.cockos.com/showthread.php?t='+val+'"] [t='+val+'][/URL]\n'
            if newline.find('[p=')>0:
                val=newline.split('[p=')[1].split(']')[0]
                newline=newline.split('[p=')[0]+'[URL="https://forum.cockos.com/showthread.php?p='+val+'"] [p='+val+'][/URL]\n'
                #[URL="https://forum.cockos.com/showthread.php?t=266880"][t=266880][/URL]
                #[URL="https://forum.cockos.com/showthread.php?t=266880"] [t=266880][/URL]
            #newline=newline.replace('[t=','[URL="[URL="https://forum.cockos.com/showthread.php?t=')
            out=out+newline
out=out+"[size=1]created by a strange python script that bobobo made with all those python things like split find and strip[/size]"            
c.copy(out)
print('you can paste it now')


        

        
        
    




    

        




