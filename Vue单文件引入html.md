Vue.js单方件引入html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <div id="app">
        <h1>{{ message }}</h1>
        <p>Count is:{{ counter.count }}</p>
        <button @click="count++">点我{{ count }}</button>
    </div>
    
    <script type="module">
        import {createApp, reactive, ref} from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
    
        createApp({
            setup() {
                const counter = reactive({count: 10})
                const count = ref(0)
                const message = ref('Hello world!')
                return {
                    counter,
                    message,
                    count,
                }
            }
        }).mount('#app')
    </script>
    
    </body>
    </html>

Vue.js组件引入html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Vue 测试实例</title>
        <script src="https://cdn.staticfile.org/vue/3.2.36/vue.global.min.js"></script>
    </head>
    <body>
    <div id="app">
        <blog-post v-for="blog in blogs" :post="blog" :key="blog.id" v-on:like-changed="outerLikeChanged"></blog-post>
    </div>
    
    <script>
        const app = Vue.createApp({
            data() {
                return {
                    blogs: [
                        {"title": "钢铁是怎样练成的？", "id": 1, "like": true},
                        {"title": "AI会毁灭人类吗？", "id": 2, "like": false},
                        {"title": "如何学好Vue！", "id": 3, "like": false},
                    ]
                }
            },
            methods: {
                outerLikeChanged: function (post_id) {
                    this.blogs.forEach(blog => {
                        if (blog['id'] === post_id) {
                            blog.like = !blog.like
                            console.log(blog);
                        }
                    });
                }
            }
        })
        app.component('blog-post', {
            props: ['post'],
            template: `
              <div>
              <h3>{{ post.title }}</h3>
              <input type="checkbox" v-model="post.like" v-on:change="innerLikeChanged">
              </div>
            `,
            methods: {
                innerLikeChanged: function () {
                    this.$emit('like-changed', this.post.id)
                }
            }
        })
        app.mount('#app')
    </script>
    </body>
    </html>
