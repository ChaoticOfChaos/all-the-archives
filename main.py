import os
from tqdm import tqdm

def fileFetch(entryPoint: str, contador: bool) -> list[str]:
    try:
        tempList = os.listdir(entryPoint)
        arquivos = []

        if contador:
            iterator = tqdm(tempList)
        else:
            iterator = tempList

        for item in iterator:
            caminhoCompleto = os.path.join(entryPoint, item)
            if os.path.isdir(caminhoCompleto):
                arquivos.extend(fileFetch(caminhoCompleto, False))
            else:
                arquivos.append(caminhoCompleto)

        return arquivos
    
    except PermissionError:
        fakeReturn = []
        return fakeReturn

allFile = fileFetch("c:\\", True)
print(len(allFile))
print(allFile)