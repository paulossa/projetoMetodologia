#coding: utf-8

from os import listdir

def getParams(fileName):
    fileName = fileName.replace("-", ".")
    temp = fileName.split(".")
    return temp[:3]

def getContent(fileName):
    out = None

    tempFile = open("output/" + fileName, "r")
    out = tempFile.read()
    out = out.split()
    tempFile.close()
    return out

def main():
    """Aqui processaremos os dados gerados pela execução do algoritmo para montar
    um CSV, com os dados do experimento para facilitar a análise"""
    outputCSV = open("output.csv", "w")
    directories = listdir("output")
    outputCSV.write(';'.join(['alg', "size", "order", "timeTaken"]) + "\n")
    for f in directories:
        print getContent(f)
        line = ";".join(getParams(f) + getContent(f))
        outputCSV.write(line + "\n")
    outputCSV.close()

main()
