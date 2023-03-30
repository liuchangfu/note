# 1. v-on

用于绑定事件，用法如下：

(1) 先来看看有哪些事件：

绑定键盘事件：

    <input type="text" placeholder="请输入" v-on:keyup="ShowInfo" />

绑定鼠标单击事件：

    <a href="#" v-on:click="ShowInfo">鼠标单击事件</a>

绑定鼠标覆盖事件：

    <a href="#" v-on:mouseover="ShowInfo">鼠标覆盖事件</a>

绑定鼠标双击事件：

    <a href="#" v-on:dblclick="ShowInfo">鼠标双击事件</a>

鼠标事件

![](https://pic1.zhimg.com/v2-822b9ae1adf580c7bf0587b52b33ef04_r.jpg)

![](https://pic2.zhimg.com/v2-2d95c137ba1e19438143c48edc4f5ee5_r.jpg)

在这里再总结一下input框的几个事件：

input事件：适用于实时查询，每输入一个字符都会出发这个事件

    <input type="text" v-on:input="ShowInfo" />

blur事件：失去焦点时触发的事件

    <input type="text" v-on:blur="ShowInfo" />

# (2) v-on的简写形式：

v-on：可以简写成@，即上边所有的v-on:事件名都可以简写成@事件名，比如@click，@keyup，@input……

# (3) 传参（以click事件为例）：

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <a href="#" v-on:click="ShowInfo">{{msg}}</a>
        </div>
        <script>
          Vue.config.productionTip = false; //阻止Vue在启动时生成生产提示
          const vm = new Vue({
            el: '#root',
            data: {
              msg: '点我提示信息',
            },
            methods: {
              ShowInfo(event) {
                console.log(event); //event是这个事件对象，这里会有一个默认的参数
              },
            },
          });
        </script>
      </body>
    </html>

v-on:可以简写为@: @click="ShowInfo"

传参:

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <a href="#" @click="ShowInfo(1)">{{msg}}</a>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              msg: '点我提示信息',
            },
            methods: {
              ShowInfo(num) {
                console.log(num); //打印结果为1
              },
            },
          });
        </script>
      </body>
    </html>

这样传参会导致丢失event，那么怎么给event占位呢？看下面：

![](https://pic1.zhimg.com/v2-c08760bba2de1d77ccb413488f9828b8_r.jpg)

总结：

事件的基本使用：

1.使用v-on:xxx 或 @xxx 绑定事件，其中xxx是事件名；

2.@click="demo" 和 @click="demo($event)" 效果一致，但后者可以传参；

# (4) v-on绑定多个事件：

语法：v-on="{事件名：方法名，事件名：方法名,……}"，v-on里面是一个对象，例如：

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="./js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <!-- v-on绑定多个事件： -->
          <button v-on="{click:single,dblclick:double}">单击n+1,双击m-1</button>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              n: 1,
              m: 2,
            },
            methods: {
              single() {
                console.log('我被单击了');
              },
              double() {
                console.log('我被双击了');
              },
            },
          });
        </script>
      </body>
    </html>

# 2. v-bind

    单向数据绑定，它是为标签里的某个属性绑定值用的

(1) 基本用法：

    <body>
        <div id="root">
         单向数据绑定：<input type="text" v-bind:value="aname">
        </div>
        <script>
          const vm = new Vue({
            el: '#root',
            data: {
              aname:'进击的Giser'
            },
          });
        </script>
     </body>

![](https://pic4.zhimg.com/v2-8c266bab0f4f649fbfdfce3b4867dc97_r.jpg)

(2) 简写形式：

v-bind:可以简写为:，举例：v-bind:href='xxx'可以简写为：:href='xxx'

# 3. v-model

    双向数据绑定，v-model只能应用在表单类元素（如：input、select等）

(1) 基本用法：

    <body>
       <div id="root">
        双向数据绑定：<input type="text" v-model:value="aname">
       <!-- 下边一行代码是错误的，因为v-model只能应用在表单类元素（输入类元素）上 -->
       <!-- <h2 v-model:x="name">你好啊</h2> -->
       </div>
       <script>
         const vm = new Vue({
           el: '#root',
           data: {
             aname:'学编程的Giser'
           },
         });
       </script>
     </body>

(2) 简写形式：

v-model:value 可以简写为 v-model，因为v-model默认收集的就是value值。

# 4. v-for

    遍历

(1) 遍历数组：

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1 v-for="(i,index) in arr">每一项：{{i}}--索引值：{{index}}</h1>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              arr: ['学', '编程', '的', 'GISer'],
            },
          });
        </script>
      </body>
    </html>

(2) 遍历对象：

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1 v-for="(i,index) in arr">键：{{i}}--值：{{index}}</h1>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              arr: {
                name: 'Dapan',
                age: 3,
                sex: 'boy',
              },
            },
          });
        </script>
      </body>
    </html>

(3) 迭代数字：

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1 v-for="(i,index) in 6">每一项：{{i}}--索引：{{index}}</h1>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {},
          });
        </script>
      </body>
    </html>

# 5. v-show

    条件渲染，v-show指令通过改变元素的 css 属性（display）来决定元素是显示还是隐藏。v-show等于false时,相当于设置了样式的display为none

> 

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1>下边测试v-show：</h1>
          <h3 v-show="showTest">v-show = true,故这个元素显示出来了</h3>
          <button @click="showTest = true">点击按钮，showTest变为true</button>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              showTest: false,
            },
          });
        </script>
      </body>
    </html>

#6. v-if

>    条件渲染，与v-show类似，唯一不同的是，当v-if = false的时候，直接删掉DOM结构

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1>下边测试v-if：</h1>
          <h3 v-if="ifTest">v-if = true,故这个元素显示出来了</h3>
          <button @click="ifTest = true">点击按钮，ifTest变为true</button>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              ifTest: false,
            },
          });
        </script>
      </body>
    </html>

# 7. v-else/v-else-if

v-else-if: 和if语句中else if的用法相同

v-else: 当v-if不成立时执行

> 

    !DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <div v-if="n==1">{{a}}</div>
          <div v-else-if="n==2">{{b}}</div>
          <div v-else-if="n==3">{{c}}</div>
          <div v-else-if="n==4">{{d}}</div>
          <div v-else style="font-weight: 700">{{e}}</div>
          <button @click="n++">点我n加一</button>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              n: 0,
              a: '欢迎',
              b: '关注',
              c: '公众号',
              d: '学编程的GISer',
              e: '欢迎关注公众号:学编程的GISer',
            },
          });
        </script>
      </body>
    </html>

注意: 如果用v-if和v-else去做判断,中间不能被打断,如:

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <!-- 错误： -->
        <div id="root">
          <div v-if="n==1">{{a}}</div>
          <div v-else-if="n==2">{{b}}</div>
          <!-- v-if和v-else被打断了: -->
          <div>@</div>
          <div v-else-if="n==3">{{c}}</div>
          <div v-else-if="n==4">{{d}}</div>
          <div v-else style="font-weight: 700">{{e}}</div>
          <button @click="n++">点我n加一</button>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              n: 0,
              a: '欢迎',
              b: '关注',
              c: '公众号',
              d: '学编程的GISer',
              e: '欢迎关注公众号:学编程的GISer',
            },
          });
        </script>
      </body>
    </html>

# 8. v-text

    用于将数据填充到标签中，作用于插值语法表达式类似，但是没有闪动问题 （如果数据中有HTML标签会将html标签一并输出 ）

用法：

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1>{{str}}</h1>
          <h1 v-text="str">公众号:</h1>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              str: '学编程的GISer',
            },
          });
        </script>
      </body>
    </html>

注意：1. v-text会把解析到为文本完全替换掉标签里的内容,如上边例子中，页面上并没有显示出“公众号：”这几个字符，因为它被v-text完全替换掉了

2. 不能解析字符串，v-text会把所有的字符串都当成正常的文本解析，不会当成标签，即使你的data里的str数据中有标签结构（比如: `<h1>123</h1>`）

# 9. v-html

v-html和v-text的区别：它与v-text区别在于v-text输出的是纯文本，浏览器不会对其再进行html解析，但v-html会将其当html标签解析后输出。

…………………… 共同点：都会全部替换原本标签里的内容。

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <div v-html="name"></div>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              name: '<h1>Dapan</h1>',
            },
          });
        </script>
      </body>
    </html>

总结：

v-html指令：

1.作用：向指定节点中渲染包含html结构的内容。

2.与插值语法的区别：

(1).v-html会替换掉节点中所有的内容，{{xx}}则不会。

(2).v-html可以识别html结构。

3.严重注意：v-html有安全性问题！！！！

(1).在网站上动态渲染任意HTML是非常危险的，容易导致XSS攻击。

(2).一定要在可信的内容上使用v-html，永不要用在用户提交的内容上！

# 10. v-cloak

    1.本质是一个特殊属性，Vue实例创建完毕并接管容器后，会删掉v-cloak属性。
    2.使用css配合v-cloak可以解决网速慢时页面展示出{{xxx}}的问题。

代码演示：

网速慢的时候：

    <!DOCTYPE html>
    <html lang="en">
    <head>
     <meta charset="UTF-8" />
     <meta http-equiv="X-UA-Compatible" content="IE=edge" />
     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
     <title>v-clock</title>
     <script src="../js/vue.js"></script>
    </head>
    <body>
     <div id="root">
       <h1>{{name}}</h1>
     </div>
     <script>
       Vue.config.productionTip = false;
       const vm = new Vue({
         el: '#root',
         data: {
           name:"Dapan"
         },
       });
     </script>
    </body>
    </html>

这个时候因为网速过慢，导致vue.js并没有加载出来，所以页面渲染如下：

`{{name}}`

使用v-cloak之后：

    <!DOCTYPE html>
    <html lang="en">
    <head>
     <meta charset="UTF-8" />
     <meta http-equiv="X-UA-Compatible" content="IE=edge" />
     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
     <title>v-cloak</title>
     <script src="../js/vue.min.js"></script>
     <style>
       [v-cloak] {
         display: none;
       }
     </style>
    </head>
    <body>
     <div id="root">
       <h1 v-cloak>{{name}}</h1>
     </div>
     <script>
       Vue.config.productionTip = false;
       const vm = new Vue({
         el: '#root',
         data: {
           name:"Dapan"
         },
       });
     </script>
    </body>
    </html>

设置了所有包含v-cloak属性的页面的display为none：

打开Live Server为空白，但是当vue.js加载好之后会删掉v-cloak属性，进而display值也就不再是none

# 11. v-once

    1.v-once所在节点在初次动态渲染后，就视为静态内容了。
    2.以后数据的改变不会引起v-once所在结构的更新，可以用于优化性能。

> 

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1 v-once>初始化时候的n是:{{n}}</h1>
          <h1>现在的n是:{{n}}</h1>
          <button @click="n++">点我n加1</button>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              n: 1,
            },
          });
        </script>
      </body>
    </html>

注意：v-cloak和v-once都没有值（后面都没有等号）。

# 12. v-pre

    1.跳过Vue在有v-pre属性的所在节点的编译过程。
    2.可利用它跳过：没有使用指令语法、没有使用插值语法的节点，会加快编译速度。

> 

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>test</title>
        <script src="../js/vue.js"></script>
      </head>
      <body>
        <div id="root">
          <h1 v-pre>没有使用指令语法和插值语法</h1>
          <h1 v-pre>{{name}}</h1>
        </div>
        <script>
          Vue.config.productionTip = false;
          const vm = new Vue({
            el: '#root',
            data: {
              name: 'dapan',
            },
          });
        </script>
      </body>
    </html>

一句话总结这12个常用指令：

- v-on : 绑定事件监听, 可简写为@
- v-bind : 单向绑定解析表达式, 可简写为 :xxx
- v-model : 双向数据绑定
- v-for : 遍历数组/对象/字符串
- v-show : 条件渲染 (动态控制节点是否展示)
- v-if : 条件渲染（动态控制节点是否存存在）
- v-else : 条件渲染（动态控制节点是否存存在）
- v-text：将数据填充到标签中（不会解析填充内容中的HTML标签）
- v-html：将数据填充到标签中（会解析填充内容中的HTML标签）
- v-cloak：一个特殊属性，Vue接管标签后会删掉这个属性（没有值）
- v-once：只渲染一次，之后Vue就不再渲染这个标签了（视为静态内容了）
- v-pre：Vue不接管这个属性所在的标签（可用于加快编译速度，用于没有使用指令语法、没有使用插值语法的节点上）