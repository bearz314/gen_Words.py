import zipfile
import shutil
import sys, os
import glob


with zipfile.ZipFile('Template.docx', 'r') as zipObj:
    # Extract all the contents of zip file in current directory
    print("Extracting zip file...")
    zipObj.extractall('tmp')
    
    # Copy all the emf files over
    print("Copying all *.emf files...")
    for file in glob.glob('*.emf'):
        shutil.copy(file, 'tmp/word/media/')
    
    # Read data from document xml file
    print("Reading original document.xml from zipObj...")
    obj_xml = zipObj.read('word/document.xml')
    
    print("Reading out.txt from Matlab...")
    with open("out.txt","r") as txt:
    	templatetxt = ["{ENDDATE}","{STARTDATE}","{d2}","{d3}","{d4}","{d5}","{d6}","{d7}","{p1}","{p2}","{p3}","{p4}","{p5}","{p6}","{p7}","{description}"]
    	replacedtxt = []
    	for line in txt:
    		replacedtxt.append(line.rstrip())
            
    	print("Replacing all placeholder texts in template.docx...")
    	for i,temptxt in enumerate(templatetxt):
        	obj_xml = obj_xml.replace(templatetxt[i].encode(),replacedtxt[i].encode())

        # write the new document xml
    	os.remove('tmp/word/document.xml')
    	with open('tmp/word/document.xml', "wb" ) as f_xml:
    		f_xml.write(obj_xml)


    # Zip the directory into a word file in working dir
    print("Outputting docx file...")
    shutil.make_archive('output', 'zip', 'tmp/')
    # Rename and change ext
    outputfilename = "Report_" + replacedtxt[1] + ".docx"
    shutil.move('output.zip',outputfilename)


print("DONE!")
print("Saved to " + outputfilename)
print()