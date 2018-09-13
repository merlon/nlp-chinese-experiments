from lxml import etree

"""parse datasets like msra-chinese-word-segmentation-data-v1/msra_bakeoff3_training.xml"""
def parse_dataset(filepath,encoding='gb18030'):
    Parser=etree.XMLParser(encoding=encoding)
    tree=etree.parse(open(filepath,encoding=encoding),parser=Parser)

    root=tree.getroot()
    s=root.getchildren()[0]

    sentences=[]
    for s in root.getchildren():
        sent=[]
        for w in s.getchildren():
            wchildren=w.getchildren()
            word=[]
            if wchildren:
                for i in wchildren:
                    if i.text:
                        word.append(i.text)
                sent.append(''.join(word))     #I assume that if the word has children, they should be joined together
            else:
                if w.text:
                    sent.append(w.text)
            #if len(wchildren)>1:
            #    print(sent)
        sentences.append(sent)
    return sentences