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
  
parsedASM = hackparser.ASMParser(tables.constantSymbols, asmText)

coderASM = coder.ASMCoder(parsedASM.symbolTable, parsedASM.instructions)
coderASM()




    

