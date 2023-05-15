# 后台代码

    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    from random import randrange
    from fastapi import FastAPI
    from pyecharts import options as opts
    from pyecharts.charts import Bar
    from fastapi.responses import JSONResponse, HTMLResponse
    import uvicorn
    
    app = FastAPI()
    
    
    def bar_base() -> Bar:
        c = (
            Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高1.跟鞋", "袜子"])
            .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
        )
        return c
    
    
    @app.get("/barChart")
    async def draw_bar_chart():
        c = bar_base()
        return JSONResponse(c.dump_options_with_quotes())
    
    
    @app.get('/get_bar_base')
    async def get_bar_base():
        with open('./index.html', 'r') as f:
            html = f.read()
        print(html)
        return HTMLResponse(content=html)
    
    
    if __name__ == '__main__':
        uvicorn.run('test08:app', reload=True)

2.前端新建index.html文件，输入代码如下：

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Awesome-pyecharts</title>
        <script src="https://cdn.bootcss.com/jquery/3.0.0/jquery.min.js"></script>
        <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
    
    </head>
    <body>
    <div id="bar" style="width:1000px; height:600px;"></div>
    <script>
        const chart = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
    
        $(
            function () {
                fetchData();
            }
        );
    
        function fetchData() {
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:8000/barChart",
                dataType: 'json',
                success: function (result) {
                    chart.setOption(JSON.parse(result));
                }
            });
        }
    </script>
    </body>
    </html>