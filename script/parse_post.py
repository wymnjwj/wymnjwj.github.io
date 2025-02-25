#! /usr/bin/python3
import re
import os
import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions import Extension
from markdown_katex import KatexExtension

class CustomMarkdown(markdown.Markdown):
    enable_attributes = False

md = CustomMarkdown(extensions=[
    'markdown.extensions.fenced_code', 
    'markdown.extensions.tables', 
    'markdown.extensions.extra', 
    'markdown.extensions.nl2br', 
    KatexExtension()  # 使用KaTeX扩展支持数学公式
])

def parse_all_post(path, o_f):
  paths = os.scandir(path)
  o_file = open(o_f, 'w')
  post_dict = {}
  for file in paths:
      if (file.is_file()) and (re.match(r"\d{1,4}_\d{1,2}_\d{1,2}_\d{1,2}_\d{1,2}_\d{1,3}_(.*)\.md", file.name)):
         tmp_file = str(file.name)
         tmp_str = tmp_file.split("_")
         tmp_post_time = ''.join([tmp_str[i].rjust(4 if i == 0 else 2 if i < 5 else 3, '0') for i in range(6)])
         tmp_post_tile = tmp_str[6][:-3]
         post_dict[tmp_post_time] = tmp_post_tile
      print(file.name)
  
  sorted_post_dict = dict(sorted(post_dict.items()))
  post_list = [[k, v] for k, v in sorted_post_dict.items()]

  write_post_navigation(o_file, post_list)
  write_post_content(o_file, post_list)
  o_file.close()

def write_post_navigation(o_file, post_list):
  for ii, post in enumerate(post_list):
    if ii == 0:
      o_file.writelines("document.write(\"<aside id = \\\"post_nav\\\">\")\n")
      o_file.writelines(f"document.write(\"  <ul id=\\\"post_nav_{ii}\\\" class=\\\"text-margin-tl\\\"><a href=\\\"#\\\", style=\\\"margin-right:4rem\\\" >{post[1]}</a></ul>\");\n")
    elif ii == len(post_list) - 1:
      o_file.writelines(f"document.write(\"  <ul id=\\\"post_nav_{ii}\\\" class=\\\"text-margin-bl\\\"><a href=\\\"#\\\" , style=\\\"margin-right:4rem\\\">{post[1]}</a></ul>\");\n")
      o_file.writelines("document.write(\"</aside>\")\n")
    else:
      o_file.writelines(f"document.write(\"  <ul id=\\\"post_nav_{ii}\\\" class=\\\"text-margin-l\\\"><a href=\\\"#\\\" , style=\\\"margin-right:4rem\\\" >{post[1]}</a></ul>\");\n")

def write_post_content(o_file, post_list):
  for ii, post in enumerate(post_list):
      o_file.writelines(f"document.write(\"<article class=\\\"blog-post\\\" id=\\\"post_{ii}\\\">\");\n")
      o_file.writelines(f"document.write(\"    <h2>{post[1]}</h2>\");\n")
      o_file.writelines(f"document.write(\"    <p class=\\\"post-date\\\">{post[0][:4]}年{post[0][4:6]}月{post[0][6:8]}日</p>\");\n")
      o_file.writelines(f"document.write(\"<div id=\\\"post_content_{ii}\\\" style=\\\"display:none\\\" >\");\n")
      tmp_str = f"../doc/{post[0][:4]}_{post[0][4:6]}_{post[0][6:8]}_{post[0][8:10]}_{post[0][10:12]}_{post[0][12:15]}_{post[1]}.md"
      with open(tmp_str, 'r', encoding='utf-8') as tmp_file:
          content = tmp_file.read()
          tmp_html = md.convert(content)
          o_file.writelines(f"document.write({repr(tmp_html)});\n")
      o_file.writelines("document.write(\"</div>\");\n")
      o_file.writelines("document.write(\"</article>\");\n")

def main():
  parse_all_post("../doc", "all_post.js")

if __name__ == '__main__':
  main()