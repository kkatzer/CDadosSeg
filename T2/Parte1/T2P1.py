import xml.etree.ElementTree as ET
import sys
import os


# Mensagem de parâmetros inválidos
def invalid_params():
    print("Parâmetros inválidos:")
    print("'./T2P1.py listAll [directory]' para listar todas as permissões por manifesto")
    print("'./T2P1.py listUnique [directory]' para listar as permissões únicas e comuns")


# Função para remover prefixo
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


# Função que lê um arquivo xml e retorna as permissões de sistema
def read_xml(file):
    root = ET.parse(file).getroot()
    xmlPermissions = root.findall("uses-permission")

    permissions = []

    for perm in xmlPermissions:
        for att in perm.attrib:
            if perm.attrib[att].startswith("android.permission."):
                permissions.append(remove_prefix(perm.attrib[att], "android.permission."))

    return permissions


# Imprime as permissões
def print_permissions(permissions):
    print("===================\n")
    print("Permissões por APK\n")
    print("===================\n")

    for app in permissions:
        print()
        print(app[16:][:-4] + ": ", end="")
        print(permissions[app])


# Conta quantas vezes a permissão aparece entre os manifestos
def count_permission(perm, permissions):
    count = 0
    for app in permissions:
        if perm in permissions[app]:
            count += 1
    return count


# Imprime as permissões únicas e comuns das APK
def print_unique_permissions(permissions):
    permInEveryApp = []
    print("===================\n")
    print("Permissões únicas por APK\n")
    print("===================\n")
    for app in permissions:
        uniquePerms = []
        for perm in permissions[app]:
            count = count_permission(perm, permissions)
            if (count == len(permissions)) and (perm not in permInEveryApp):
                permInEveryApp.append(perm)
            if count == 1:
                uniquePerms.append(perm)
        print()
        print(app[16:][:-4] + ": ", end="")
        print(uniquePerms)
    print("\n===================\n")
    print("Permissões comuns das APKs\n")
    print("===================\n")
    print(permInEveryApp)


permissions = {}

# Número incorreto de argumentos
if len(sys.argv) < 3:
    invalid_params()
    sys.exit()

# Itera pela pasta e pega as permissões de cada manifesto
for filename in os.listdir(sys.argv[2]):
    if filename.endswith(".xml"):
        permissions[filename] = read_xml(sys.argv[2] + "/" + filename)

# Checa qual função a ser usada
if sys.argv[1] == "listAll":
    print_permissions(permissions)
elif sys.argv[1] == "listUnique":
    print_unique_permissions(permissions)
else:
    invalid_params()
