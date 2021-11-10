from openpyxl import Workbook, load_workbook

#abre libro de trabajo
wb = Workbook()
#hoja activa
ws = wb.active
ws.title = "Data"
#agrega una fila con los datos ingresados en forma de texto
ws.append(["Asset UUID","CVE","CVSS","CVSS Base Score", "CVSS Temporal Score ","CVSS Temporal Vector ","CVSS Vector ","CVSS3 Base Score ","CVSS3 Temporal Score ","CVSS3 Temporal Vector ","CVSS3 Vector","Description" ,"FQDN" ,"Host" ,"Host End" ,"Host Start" ,"IP Address" ,"MAC Address" ,"Name" ,"NetBios","OS","Plugin Family","Plugin ID","Plugin Output ","Port ","Protocol ","Risk ","See Also","Solution","Synopsis" ,"System Type" ,"Vulnerability Priority Rating (VPR)" ,"Vulnerability State","Age" ,"First Seen","Last Seen","Recast Reason"])

#guarda el excel con los cambios realizados
wb.save('reportVulnerability.xlsx')