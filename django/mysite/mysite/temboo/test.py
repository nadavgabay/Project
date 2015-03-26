__author__ = 'nadav'

import apache_log_parser

file = "Mar  4 14:26:07 10.203.166.9 1 2015-03-04T14:26:07.849Z direct-run-i-42a368b2 http-bio-10621-exec-49 1415   112.215.63.6, 107.167.102.146, 10.31.218.43 127.0.0.1 - - [04/Mar/2015:14:26:07 +0000] 'GET /favicon.ico HTTP/1.0' 200 5430 0.000 m.bosloker.com [Opera/9.80 (Android; Opera Mini/7.6.40234/35.7770; U; id) Presto/2.8.119 Version/11.10]"
splited_file = file.split(" ")
print splited_file

little = splited_file[4]

line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
print(log_line_data)