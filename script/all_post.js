document.write("<aside id = \"post_nav\">")
document.write("  <ul id=\"post_nav_0\" class=\"text-margin-tl\"><a href=\"#\", style=\"margin-right:4rem\" >git操作</a></ul>");
document.write("  <ul id=\"post_nav_1\" class=\"text-margin-l\"><a href=\"#\" , style=\"margin-right:4rem\" >我的测试0</a></ul>");
document.write("  <ul id=\"post_nav_2\" class=\"text-margin-l\"><a href=\"#\" , style=\"margin-right:4rem\" >我的测试1</a></ul>");
document.write("  <ul id=\"post_nav_3\" class=\"text-margin-bl\"><a href=\"#\" , style=\"margin-right:4rem\">我的测试2</a></ul>");
document.write("</aside>")
document.write("<article class=\"blog-post\" id=\"post_0\">");
document.write("    <h2>git操作</h2>");
document.write("    <p class=\"post-date\">2025年02月06日</p>");
document.write("<div id=\"post_content_0\" style=\"display:none\" >");
document.write('<p><strong>github与本地git管理</strong></p>');
document.write('<p>github在2021.08.13之后不再支持密码方式认证，可以通过SSH认证完成本地git仓库的上传</p>');
document.write('<p>1、需要修改本地仓库中的.git/config 中的URL路径，不再使用https而是使用git@github.com:xxxx/xxxxx.git的SSH地址（注意不加ssh://，直接从github网页copy）</p>');
document.write('<p>2、在本地的terminal下 ssh-keygen -t ed25519 -C "your_email@example.com"，来生成对应的SSH公钥和私钥文件（注意密钥文件的权限，777将无法使用，chmod 到600）</p>');
document.write('<p>3、eval "$(ssh-agent -s)"启动ssh服务</p>');
document.write('<p>4、ssh-add ~/私钥文件</p>');
document.write('<p>5、在git hub setting中的的SSH keys增加相应的公钥文件中的内容</p>');
document.write('<p>6、稍等后完成，可以通过 ssh -vT git@github.com 来测试当前的连通</p>');
document.write("</div>");
document.write("</article>");
document.write("<article class=\"blog-post\" id=\"post_1\">");
document.write("    <h2>我的测试0</h2>");
document.write("    <p class=\"post-date\">2025年02月17日</p>");
document.write("<div id=\"post_content_1\" style=\"display:none\" >");
document.write('<p>test</p>');
document.write("</div>");
document.write("</article>");
document.write("<article class=\"blog-post\" id=\"post_2\">");
document.write("    <h2>我的测试1</h2>");
document.write("    <p class=\"post-date\">2025年02月17日</p>");
document.write("<div id=\"post_content_2\" style=\"display:none\" >");
document.write('<p>test</p>');
document.write("</div>");
document.write("</article>");
document.write("<article class=\"blog-post\" id=\"post_3\">");
document.write("    <h2>我的测试2</h2>");
document.write("    <p class=\"post-date\">2025年02月17日</p>");
document.write("<div id=\"post_content_3\" style=\"display:none\" >");
document.write('<p>test</p>');
document.write("</div>");
document.write("</article>");
