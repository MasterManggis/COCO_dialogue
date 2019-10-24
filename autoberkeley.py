from nltk.draw import TreeView
from nltk.tree import *
from nltk.parse import CoreNLPParser


# s = '* kid （PP on right）(PP in back) (NP blondish hair)'
#
# tree = Tree.fromstring(s, leaf_pattern=r"([^\s\(\)\\]+(\\(?=\()\([^\s\(\)\\]+\\(?=\))\))*[\\]*)+", read_leaf=lambda x: x.replace("\\(", "(").replace("\\)", ")"))
# print(type(tree))
# sentence = ParentedTree.convert(tree)
# print(sentence[1].label())


# import benepar
import pandas as pd


def result(tree):
    subtree = tree
    res=''
    while type(subtree) == ParentedTree and len(subtree) == 1:
        if type(subtree[0]) == ParentedTree:
            subtree = subtree[0]
        else:
            break
    for i in range(0,len(subtree)):
        if len(subtree[i]) == 1 and type(subtree[i]) == ParentedTree:
            o_tree=subtree[i]
            while type(o_tree[0]) == ParentedTree and len(o_tree) == 1:
                o_tree =o_tree[0]
            res=res+o_tree.label()+'('+' '.join(subtree[i].leaves())+')'
        else:
            res=res+subtree[i].label()+'('+' '.join(subtree[i].leaves())+')'
    return res
    #
    # if type(subtree) == ParentedTree and len(subtree) > 1:
    #     return subtree
    # else:
    #     return None

if __name__ == '__main__':
    res=[]
    parser = CoreNLPParser(url='http://localhost:9000')
    # dataset=pd.read_csv("Result.csv",sep=',',header=None)
    sentence = [bala for bala in parser.parse("right with something thing white in his hand".split())]
    sentence = ParentedTree.convert(sentence[0])
    print(sentence)
    # res.append(result(sentence))
    # tree = parser.parse("old lady with glasses holding teddy bear")
    # sentence = ParentedTree.convert(tree)
    # print(result(sentence))

    # for i in range(0,dataset.shape[0]):
    # # for i in range(0,1):
    #     sentence = [bala for bala in parser.parse(dataset[1][i].split())]
    #     sentence = ParentedTree.convert(sentence[0])
    #     res.append(result(sentence))
    #     print(i)
    # dataset[3] = res
    # print(dataset)
    # dataset.to_csv('Result1.csv',sep=',',header=0,index=0)


        # print(dataset[1][i])
        # print(result(sentence))
    TreeView(sentence)._cframe.print_to_file("lalalal.ps")
