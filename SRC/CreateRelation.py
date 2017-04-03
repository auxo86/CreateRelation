'''
Created on 2017年4月3日

@author: autoix
'''
import xml.etree.ElementTree as ET

#定義要讀取的xml檔案名稱
strXmlName = "測試二元樹.xml"
#定義要寫入的關係字串List，連 Xpath 一起定義
ListStrRelation = [(" has member ", ".//node"), (" has child ", "./node")]
#定義要寫入的檔案名稱
strWriteFileName = strXmlName.replace(".xml", "") + "_" + "Relation.txt"
#定義要寫入的目錄字串
strOutputDir = "./"
#開啟寫入檔案
FileForWrite = open(strOutputDir + strWriteFileName, 'w', encoding = 'UTF-8')

tree = ET.ElementTree(file=strXmlName)
MemberTree = tree
for elem in tree.iter(tag='node'):
    #每一種關係都要跑一次，不同的關係有不同對應的Xpath
    for Relation in ListStrRelation:
        MemberTree._setroot(elem)
        #用於計算是否有子節點，如果沒有就寫入換行符號
        intCountMember = 0
        for elemMemberNode in MemberTree.iterfind(Relation[1]):
            FileForWrite.write(elem.attrib['TEXT'] + Relation[0] + elemMemberNode.attrib['TEXT'] + "\n")
            intCountMember += 1
        if intCountMember > 0:
            FileForWrite.write("\n")

FileForWrite.close()

