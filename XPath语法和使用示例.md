## [XPath](https://so.csdn.net/so/search?q=XPath&spm=1001.2101.3001.7020)语法和使用示例

## 选取节点

| 表达式      | 描述                            |
| -------- | ----------------------------- |
| nodename | 选取此节点的所有子节点。                  |
| /        | 从根节点选取。                       |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
| .        | 选取当前节点。                       |
| ..       | 选取当前父节点。                      |
| @        | 选取属性。                         |
| text()   | 选取文本内容。                       |

实例

在下面的表格中，列出一些路径表达式以及表达式的结果：

| 路径表达式               | 结果                                                   |
| ------------------- | ---------------------------------------------------- |
| bookstore           | 选取bookstore元素                                        |
| /bookstore          | 选取根元素bookstore。注释：假如路径起始于(/)，则此路径始终代表到某元素的绝对路径。      |
| bookstore/book      | 取属于bookstore的子元素的所有book元素。                           |
| //book              | 选取所有book子元素，而不管他们在文档中的位置。                            |
| bookstore//book     | 选择属于bookstore元素的后代的所有book元素，而不管它们位于bookstore之下的什么位置。 |
| //book/title/@lang  | 选择所有的book下面的title中的lang属性的值。                         |
| //book/title/text() | 选择所有的book下面的title的文本。                                |

## 查找特定的节点

| 路径表达式                               | 结果                                                     |
| ----------------------------------- | ------------------------------------------------------ |
| //title[@lang]                      | 选取所有拥有名为lang的属性的title元素。                               |
| //title[@lang="eng"]                | 选取lang属性值为eng的所有title元素。                               |
| /bookstore/book[1]                  | 选取属于bookstore子元素的第一个book元素。                            |
| /bookstore/book[last()]             | 选取属于bookstore子元素的最后一个book元素。                           |
| /bookstore/book[position()>1]       | 选择bookstore下面的book元素，从第二个开始选择。                         |
| //book/title[text()='Harry Potter'] | 选择所有book下的title元素，仅仅选择文本为Harry Potter的title元素。         |
| /bookstore/book[price>35.00]/title  | 选取bookstore元素中的book元素的所有title元素，且其中的price元素的值需大于35.00。 |

注意点：在xpath中，第一个元素的位置是1，最后一个元素的位置是last()，倒数第二个是last()-1。

## 选取未知节点

Path通配符可用来选取未知的XML元素。

| 通配符    | 描述         |
| ------ | ---------- |
| *      | 匹配任何元素节点。  |
| @*     | 匹配任何属性的节点。 |
| node() | 匹配任何类型的节点。 |

实例

在下面的表格中，列出一些路径表达式以及表达式的结果：

| 路径表达式         | 结果                   |
| ------------- | -------------------- |
| //bookstore/* | 选取bookstore元素的所有子元素。 |
| //*           | 选取文档中的所有元素。          |
| //title[@*]   | 选取所有带属性的title元素。     |

## 选取若干路径

通过在路径表达式中使用"|"运算符，您可以选取若干个路径。

实例

在下面的表格中，列出一些路径表达式以及表达式的结果：

| 路径表达式                            | 结果                                                |
| -------------------------------- | ------------------------------------------------- |
| //book/title \| //book/price     | 选取book元素的所有title和price元素。                         |
| //title \| //price               | 选取文档中的所有title和price元素。                            |
| /bookstore/book/title \| //price | 选取属于bookstore元素的book元素的所有title元素，以及文档中所有的price元素。 |
