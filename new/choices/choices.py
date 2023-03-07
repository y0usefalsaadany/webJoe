import sys
class choices:
    tool_num=''
    def __init__(this,tool_number):
        this.tool_num = tool_number

    def tool(this):
        try:
            sys.path.insert(0, '../tool')
            if this.tool_num == 1:
                from tool.domainInfo import domain_info
                domain_info.domain_info()

            elif this.tool_num == 2:
                from tool.sourceCode import sourceCode
                sourceCode.sourceCode()
            elif this.tool_num == 3:
                from tool.subdomain import subdomain

            elif this.tool_num == 4:
                from tool.paths import paths

            elif this.tool_num == 5:
                from tool.api import api

            elif this.tool_num == 6:
                from tool.make_list import list

            elif this.tool_num == 7:
                from tool.crack import crack
                
            elif this.tool_num == 8:
                from tool.portScanner import portScanner

            else:
             print ('Enter one of the numbers shown in front of you.')

        except KeyboardInterrupt:
            sys.exit()

