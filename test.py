

cmd=''
list = ['', ' --interactive']
list1 = ['', ' --wait', ' --terminate']
actionInteractive = ['', ' --action=list', ' --action=log', ' --action=ignore', ' --action=remove', ' --action=user']
actionNotInteractive = ['', ' --action=list', ' --action=log', ' --action=ignore', ' --action=delete', ' --action=copy', ' --action=move', ' --action=remove']
dest = ['', ' --destination']
excl = ['', ' --exclusions=[path]', ' --exclusions=default']
QSpath = [' --QS', ' [path]'] # /scan requires QS or path

for element in list:
	if element == ' --interactive':
		for element1 in list1:
			for element2 in actionInteractive:	
				for element4 in excl:  #no need to check for interactive since in first if statement
                                        for element5 in QSpath: 
                                                print 'mbamlite.exe /scan' + element + element1 + element2 + element4 + element5		
	else:
		for element2 in actionNotInteractive:
			if element2 in (' --action=copy', ' --action=move'):
				for element3 in dest:
					for element4 in excl: 
						for element5 in QSpath: 
							cmd = 'mbamlite.exe /scan' + element + element2 + element3 + element4 + element5
							print cmd
			else:
				for element4 in excl:  
					for element5 in QSpath: 
						cmd = 'mbamlite.exe /scan' + element + element2 + element4 + element5
						print cmd	
