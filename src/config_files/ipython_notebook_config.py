c = get_config()                                                                                                                   
# Kernel config                                                                                                                    
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always                                                              
                                                                                                                                   
                                                                                                                                   
c.NotebookApp.keyfile = u'/home/ubuntu/nbserver.pem'                                                                             
c.NotebookApp.certfile = u'/home/ubuntu/nbserver.pem'                                                                            
PWDFILE="/home/ubuntu/.ipython/profile_nbserver/nbpasswd.txt"                                                                    
c.NotebookApp.password = open(PWDFILE).read().strip()                                                                              
                                                                                                                                   
c.NotebookApp.ip = '*'                                                                                                             
c.NotebookApp.open_browser = False                                                                                                 
                                                                                                                                   
# It is a good idea to put it on a known, fixed port                                                                               
c.NotebookApp.port = 9999                                                                                                          
                                                                                                                                   
c.TerminalIPythonApp.display_banner = True                                                                                         
c.InteractiveShellApp.log_level = 20                                                                                               
c.InteractiveShellApp.extensions = [                                                                                               
    'myextension'                                                                                                                  
]                                                                                                                                  
c.InteractiveShellApp.exec_lines = [                                                                                               
    'import numpy',                                                                                                                
    'import scipy'                                                                                                                 
]                                                                                                                                  
c.InteractiveShellApp.exec_files = [                                                                                               
    'mycode.py',                                                                                                                   
    'fancy.ipy'                                                                                                                    
]                                                                                                                                  
c.InteractiveShell.autoindent = True                                                                                               
c.InteractiveShell.colors = 'LightBG'                                                                                              
c.InteractiveShell.confirm_exit = False                                                                                            
c.InteractiveShell.deep_reload = True                                                                                              
c.InteractiveShell.editor = 'nano'                                                                                                 
c.InteractiveShell.xmode = 'Context'                                                                                               
                                                                                                                                   
c.PromptManager.in_template  = 'In [\#]: '                                                                                         
c.PromptManager.in2_template = '   .\D.: '                                                                                         
c.PromptManager.out_template = 'Out[\#]: '                                                                                         
c.PromptManager.justify = True                                                                                                     
                                                                                                                                   
c.PrefilterManager.multi_line_specials = True                                                                                      
                                                                                                                                   
c.AliasManager.user_aliases = [                                                                                                    
 ('la', 'ls -al')                                                                                                                  
]                              
