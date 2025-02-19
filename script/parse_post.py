#! /usr/bin/python3
import re
import os
import markdown

def parse_all_post(path, o_f):
  paths=os.scandir(path)
  o_file = open(o_f,'w')
  post_dict={}
  for file in paths:
      if (file.is_file()) and (re.match("\d{1,4}\_\d{1,2}\_\d{1,2}\_\d{1,2}\_\d{1,2}\_\d{1,3}\_(.*)\.md",file.name)):
         tmp_file = str(file.name)
         tmp_str  = tmp_file.split("_")
         tmp_year   = tmp_str[0].rjust(4,'0')
         tmp_mounth = tmp_str[1].rjust(2,'0')
         tmp_day    = tmp_str[2].rjust(2,'0')
         tmp_hour   = tmp_str[3].rjust(2,'0')
         tmp_minites= tmp_str[4].rjust(2,'0')
         tmp_id     = tmp_str[5].rjust(3,'0')
         tmp_post_time = tmp_year+tmp_mounth+tmp_day+tmp_hour+tmp_minites+tmp_id
         tmp_post_tile =  tmp_str[6][:-3]
         post_dict[tmp_post_time]=tmp_post_tile
      print(file.name)
  
  sorted_post_dict = dict(sorted(post_dict.items()))

  post_list=[]
  i=0 

  for tmp_post_time in sorted_post_dict:
     tmp_list = [tmp_post_time,sorted_post_dict[tmp_post_time]]
     post_list.append(tmp_list)
     i=i+1

  for ii in range(i):
    if(ii==0):
      o_file.writelines("document.write(\"<aside id = \\\"post_nav\\\">\")\n")
      o_file.writelines("document.write(\"  <ul id=\\\"post_nav_"+str(ii)+"\\\" class=\\\"text-margin-tl\\\"><a href=\\\"#\\\", style=\\\"margin-right:4rem\\\" >"+ post_list[ii][1]+"</a></ul>\");\n")
    elif (ii==i-1):
      o_file.writelines("document.write(\"  <ul id=\\\"post_nav_"+str(ii)+"\\\" class=\\\"text-margin-bl\\\"><a href=\\\"#\\\" , style=\\\"margin-right:4rem\\\">"+post_list[ii][1]+"</a></ul>\");\n")
      o_file.writelines("document.write(\"</aside>\")\n")
    else:
      o_file.writelines("document.write(\"  <ul id=\\\"post_nav_"+str(ii)+"\\\" class=\\\"text-margin-l\\\"><a href=\\\"#\\\" , style=\\\"margin-right:4rem\\\" >"+post_list[ii][1]+"</a></ul>\");\n")

  for ii in range(i):
      o_file.writelines("document.write(\"<article class=\\\"blog-post\\\" id=\\\"post_"+ str(ii) +"\\\">\");\n")
      o_file.writelines("document.write(\"    <h2>"+ post_list[ii][1]+"</h2>\");\n")
      o_file.writelines("document.write(\"    <p class=\\\"post-date\\\">"+ post_list[ii][0][0:4]+"年"+post_list[ii][0][4:6]+"月"+post_list[ii][0][6:8]+"日"+"</p>\");\n")
      o_file.writelines("document.write(\"<div id=\\\"post_content_"+ str(ii) +"\\\" style=\\\"display:none\\\" >\");\n")
      tmp_str  = "../doc/"+ post_list[ii][0][ 0: 4] + \
                  "_"     + post_list[ii][0][ 4: 6] + \
                  "_"     + post_list[ii][0][ 6: 8] + \
                  "_"     + post_list[ii][0][ 8:10] + \
                  "_"     + post_list[ii][0][10:12] + \
                  "_"     + post_list[ii][0][12:15] + \
                  "_"     + post_list[ii][1] + ".md"
      tmp_file = open(tmp_str,'r',encoding='utf-8')
      for line in tmp_file.readlines():
        tmp_html = markdown.markdown(line)
        if tmp_html :
          o_file.writelines("document.write("+repr(tmp_html)+");\n")
      o_file.writelines("document.write(\"</div>\");\n")
      o_file.writelines("document.write(\"</article>\");\n")
  o_file.close()

def main():
  parse_all_post("../doc","all_post.js")


if __name__ == '__main__':
  main()