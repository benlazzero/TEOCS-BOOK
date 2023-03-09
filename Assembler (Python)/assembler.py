import sys
import hackparser
import coder
import tables

# get file path from cli
asmPath = sys.argv[1]

# prepare text of asm file
asmText = ''
with open(asmPath, "r") as asmFile: 
  asmText = asmFile.read()
  
claz = hackparser.ASMParser(tables.constantSymbols, asmText)
#print(claz.instructions)
#print(claz.symbolTable)

codz = coder.ASMCoder(claz.symbolTable, claz.instructions)
codz()




    

