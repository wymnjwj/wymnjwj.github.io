1、assign 对齐中，信号domain对齐，等号对齐，后面的内容也对齐
2、if与else有时并不会连接begin end块，可能独立存在，需要考虑这种情况 ，次行开始进行缩进(解决中间插有注释的行时缩进不对齐的bug)。
3、信号名中可能存在.这种sv语法。
4、if else、begin end等代码块里的 =或者<=或者:需要对齐。
5、如果if else 后紧跟表达式在一行内，将表达内容换行缩进
6、连续的else if与上面的if、else if同级，其内部块与上面的对齐（解决if后跟较复杂条件时或者带注释时次行存在bug）。
7、具有参数的模块例化时，例如 inst #() inst_name (); 中，# ( 可能与信号名同行; ‘)’ ‘inst_name’ ‘(’ 可能分别分组在3行、2行、1行内均有可能，当前inst识别存在bug;
8、模块信号列表中可能存在input/output/inout/interface(anyname), 后面可能存在 reg/wire/logic关键字(可选)，整体需要对齐; 然后是位宽domain需要对齐方式为[:]分别对齐;然后是信号名需要对齐;
9、模块内部的信号wire/reg/interface/logic等声明仅考虑连续的块，有空行或注释后重新对齐
10、