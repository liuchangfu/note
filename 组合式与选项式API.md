# Vue2和Vue3的响应式

## (1) vue2的响应式

    <div id="app" v-cloak>
        <div>学生信息：{{student}}</div>
        <button @click="student.name+='!'">修改学生姓名</button>
        <button @click="student.age++">修改学生年龄</button>
        <button @click="addSex">添加性别</button>
        <button @click="delName">删除姓名</button>
        <hr>
        <div>食物：{{foods}}</div>
        <button @click="addFood">添加食物</button>
        <button @click="delFood">删除帝王蟹</button>
    </div>

----------

    new Vue({
         el:'#app',
             student:{
                 name:'张三',
                 age:20
             },
             foods:['鱼翅','鱼子酱','松茸','帝王蟹']
         },
         methods: {
             addSex(){
                 // 后添加的属性是非响应式的
                 // 可以通过这个方法this.$forceUpdate()强制页面更新一次
                 // this.student.sex='男'
                 // this.$forceUpdate()
                 // 推荐使用$set()方法给对象添加新的属性，确保新添加的属性同样具备响应式
                 this.$set(this.student,'sex','男')
                 console.log(this.student);
             },
             delName(){
                 // 直接使用delete方法删除对象的属性后，不具备响应式
                 // delete this.student.name
                 // 使用$delete，具备响应式
                 this.$delete(this.student,'name')
             },
             addFood(){
                 // 操作数组后同时要具有响应式，必须要使用下面的方法：
                 // push pop unshift shift sort reserve splice
                 // this.foods.push('佛跳墙')
                 // this.foods[4] = '佛跳墙'
                 // this.$forceUpdate()
                 // 推荐使用$set()方法根据下标添加数组元素，确保新添加的元素同样具备响应式
                 this.$set(this.foods,4,'佛跳墙')
             },
             delFood(){
                 // this.foods.splice(3,1)
                 // 直接根据下标删除数组元素，不具备响应式
                 // this.foods[3] = null
                 // 使用$delete,具备响应式
                 this.$delete(this.foods,3)
             }
         },
    })

## (2) vue3的响应式

vue3修复了vue2中响应式的所有缺陷。
在vue3中，直接给对象添加属性、直接删除对象的属性、根据下标操作数组，都依然具备响应式。

    Vue.createApp({
        data() {
            return {
                student: {
                    name: '张三',
                    age: 20
                },
                foods: ['鱼翅', '鱼子酱', '松茸', '帝王蟹']
            }
        },
        methods: {
            addSex(){
                this.student.sex='男'
            },
            delName(){
                delete this.student.name
            },
            addFood(){
                this.foods[4] ='佛跳墙'
            },
            delFood(){
                this.foods[3] = null
            }
        },
    }).mount('#app')

# 引出Vue3新推出的组合式API

## (1) vue2中只能这样写代码，vue3也可以这样写

    <div id="app">
        <div>
            <p>{{carName}}--{{carPrice}}</p>
            <button @click="updateCar">修改汽车信息</button>
        </div>
        <div>
            <p>{{planeName}}--{{planePrice}}</p>
            <button @click="updatePlane">修改飞机信息</button>
        </div>
        <div>
            <p>{{watchName}}--{{watchPrice}}</p>
            <button @click="updateWatch">修改手表信息</button>
        </div>
        <div>
            <p>{{phoneName}}--{{phonePrice}}</p>
            <button @click="updatePhone">修改手机信息</button>
        </div>
    </div>

----------

    Vue.createApp({
        data() {
            return {
                carName:'保时捷',
                carPrice:'100w',
                planeName:'播音747',
                planePrice:'10y',
                watchName:'劳力士',
                watchPrice:'10w',
                phoneName:'iphone13',
                phonePrice:'5999'
            }
        },
        methods: {
            updateCar(){
                this.carName = '布加迪威龙'
                this.carPrice = '200w'
            },
            updatePlane(){
                this.planeName = 'B52轰炸机'
                this.planePrice = '30y'
            },
            updateWatch(){
                this.watchName = '欧米茄'
                this.watchPrice = '4w'
            },
            updatePhone(){
                this.phoneName = '华为'
                this.phonePrice = '6999'
            }
        },
    }).mount('#app')

## (2) vue3引入了全新的功能，组合式API，所有的组合式API都要在setup里面使用

Vue3中，无论是Vue实例，还是组件，data选项都必须是一个方法。

我们之前习惯将所有的数据放在data选项中定义，所有的方法放在methods选项中定义，所有的计算属性放在computed选项中定义，所有的侦听

器放在watch选项中定义。这样就会导致一个业务的代码会拆分到多个结构中去写，如果一个页面中要操作很多个业务，代码后期维护成本会很

高。

所以，Vue3引入了组合式API，简化之前繁琐的过程，将相同业务的代码靠在一起写。

组合式api的作用是：将原来分散开来定义的数据、方法、计算属性、监听器等，组合起来定义一个完整的业务。

组合式API(Composition API)：Vue推出的一些新的方法，这个方法在setup中使用。

ref对象：在setup中，直接定义的数据是不具备响应式的。ref用于定义响应式数据，使用ref组合式API对数据进行包装，包装后返回的是ref
对象。ref对象的value属性保存的是值。

    <div id="app">
        <div>
            <p>{{carName}}--{{carPrice}}</p>
            <button @click="updateCar">修改汽车信息</button>
        </div>
        <div>
            <p>{{planeName}}--{{planePrice}}</p>
            <button @click="updatePlane">修改飞机信息</button>
        </div>
        <div>
            <p>{{watchName}}--{{watchPrice}}</p>
            <button @click="updateWatch">修改手表信息</button>
        </div>
        <div>
            <p>{{phoneName}}--{{phonePrice}}</p>
            <button @click="updatePhone">修改手机信息</button>
        </div>
    </div>

----------

    // ref用于定义响应式数据
    let { ref } = Vue
    
    Vue.createApp({
        // setup是组合式API的舞台，所有的组合式API都要在setup里面使用
        setup() {
            // 定义汽车相关数据
            // 使用ref()方法，定义一个响应式对象
            let carName = ref('保时捷')
            let carPrice = ref('100w')
            // 定义汽车相关方法
            function updateCar() {
                // 修改对象的值，要通过value属性
                carName.value = '布加迪威龙'
                carPrice.value = '200w'
                console.log(carName,carPrice);
            }
    
            // 定义飞机相关数据
            let planeName = ref('播音747')
            let planePrice = ref('10y')
            function updatePlane() {
                planeName.value = 'B52轰炸机'
                planePrice.value = '30y'
            }
    
            // 手表
            let watchName = ref('劳力士')
            let watchPrice =ref( '10w')
            function updateWatch() {
                watchName.value = '欧米茄'
                watchPrice.value = '4w'
            }
    
            // 手机
            let phoneName = ref('iphone13')
            let phonePrice =ref( '5999')
            function updatePhone() {
                phoneName.value = '华为'
                phonePrice.value= '6999'
            }
            return {
                // 返回汽车相关数据
                carName,
                carPrice, 
                updateCar,
                // 返回飞机相关数据
                planeName,
                planePrice,
                updatePlane,
                // 返回手表相关数据
                watchName,
                watchPrice,
                updateWatch,
                // 返回手机相关数据
                phoneName,
                phonePrice,
                updatePhone
            }
        }
    }).mount('#app')

## 3.ref( )和reactive( )

所有的组合式API，要在setup方法里面使用；setup方法，返回出去的对象里面的成员，可以在模板中使用。
ref 和 reactive 用于定义响应式数据。
通常情况下，基本类型的数据，选择用ref定义；引用类型的数据，选择用reactive定义。

ref方法：返回的是ref对象，ref对象的value属性是一个代理对象(Proxy)。使用ref既可以定义基本类型数据，也可以定义引用类型数据。注意：修改值时，必须要先 点value再 点具体的属性 = 值

reactive方法：直接返回一个代理对象(Proxy)。reactive只能定义引用类型数据。

    <div id="app">
        <ul>
            <li>姓名：{{name}}</li>
            <li><button @click="updateName">修改姓名</button></li>
        </ul>
        <ul>
            <li>车名：{{car.name}}</li>
            <li>车价：{{car.price}}</li>
            <li><button @click="updateCar">修改汽车</button></li>
        </ul>
        <ul>
            <li>飞机名：{{plane.name}}</li>
            <li>飞机价：{{plane.price}}</li>
            <li><button @click="updatePlane">修改飞机</button></li>
        </ul>
    </div>

----------

    let { ref, reactive } = Vue
    Vue.createApp({
        setup() {
            // 使用ref定义基本类型数据
            let name = ref('张三')
            let updateName = () => {
                // 修改值时，必须要先 点value
                name.value = '李四'
            }
            // 使用ref定义引用类型数据
            let car = ref({
                name: '奔驰',
                price: 30
            })
            let updateCar = () => {
                // 修改值时，必须要先 点value
                car.value.name = '奥迪'
                car.value.price = 40
            }
            // 使用reactive定义引用类型数据
            // 注意：reactive只能定义引用类型数据
            // 定义引用类型优先选择reactive，定义值类型选择ref
            let plane = reactive({
                name: '长城',
                price: 300
            })
            let updatePlane = () => {
                plane.name = '东风'
                plane.price = 400
            }
            console.log(car);
            console.log(plane);
    
            return {
                name,
                updateName,
                car,
                updateCar,
                plane,
                updatePlane
            }
        }
    }).mount('#app')