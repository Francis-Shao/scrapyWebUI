<template>
    <div id="introduction" style="float: left ;width: 100%;text-align: left">
        <div>
            <h2>脚本管理</h2>
            <ul>
                <li><p><span>主要功能为运行Scrapy项目</span></p></li>
                <li><p><span>需要Scrapy项目打包的zip压缩包，项目名和需要运行的脚本名</span></p></li>
                <li><p><span>项目名请按照settings的项目填写，否则容易出现未知错误</span></p></li>
                <li><p><span>项目运行之后可以查看和下载项目的log输出</span></p></li>
                <li><p><span>可以选择在项目运行过程中停止项目</span></p></li>
                <li><p><span>项目停止阶段可以删除项目</span></p></li>
            </ul>
        </div>
        <div >
            <h2>自动化生成脚本</h2>
            <ul>
                <li>
                    <h4><span>操作说明</span></h4>
                    <ol start=''>
                        <li><p><span>点击“自动生成脚本按钮”；</span></p></li>
                        <li><p><span>在弹出框中输入一些必要的参数；</span></p></li>
                        <li><p><span>提交信息后表格上显示您刚刚创建的脚本，并包含下载功能，您可以自行选择下载。</span></p></li>
                    </ol>
                </li>
                <li>
                    <h4><span>参数说明</span></h4>
                    <ul>
                        <li>
                            <p><span>项目名：您需要创建的scrapy项目名称，前后两次创建不要重名，不要以数字开头。</span></p>
                        </li>
                        <li>
                            <p><span>网址：您要爬取的起始网页。</span></p>
                        </li>
                        <li>
                            <p><span>div容器xpath:您选择爬取的主题所在div的xpath，例如您要爬取豆瓣中对电影头号玩家的所有影评，那div容器的xpath就是影评所在容器的xpath。</span>
                            </p>
                        </li>
                        <li>
                            <p><span>next_link：如果要爬取的内容不止一页，需要您填写链接到下一页的xpath。</span></p>
                        </li>
                        <li>
                            <p><span>item：您要爬取的内容名称，例如您要爬取豆瓣中对电影头号玩家的所有影评，item可以是该条影评的用户名、评论时间、评分、影评内容等。请填写英文如用户名可填写为user_name。</span>
                            </p>
                        </li>
                        <li>
                            <p><span>xpath：您要爬取的item对应的xpath。</span></p>
                        </li>
                        <li>
                            <p><span>优化选项：</span></p>
                            <ul>
                                <li><p><span>userAgent：使用随机user-agent头对目标网站发起请求，初级反爬措施，可以降低爬虫被识别出来的概率。</span></p></li>
                                <li><p><span>cookie：选择携带或不携带cookie对目标网站进行访问爬取，应对不同网站的不同情况，可以自行选择。</span></p></li>
                                <li><p><span>robot：选择爬虫是否遵守机器人协议，遵守可能会导致部分页面内容无法爬取，根据爬虫的情况来进行选择。</span></p></li>
                                <li><p><span>bloom：在大数据情况下降低内存消耗，当爬取URL量达到20万以上时建议开启，否则服务器可能无法承担。</span></p></li>
                                <li><p><span>ipPool：选择是否使用代理ip池进行爬取。使用同一ip爬取大量内容可能会导致ip地址被目标网站暂时拒绝访问，使用代理ip池则可以显著降低这一风险，但性能可能会因代理ip的不同而存在差异。</span></p>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <p><span>新增一条和删除：您可以自定义您想要爬取的item的数量</span></p>
                            <p><span>不知道如何获取xpath？点击这里：</span><a
                                    href='https://blog.csdn.net/li6727975/article/details/46126079' target='_blank'
                                    class='url'>https://blog.csdn.net/li6727975/article/details/46126079</a></p>
                            <p><span>或者请您自行百度。</span></p>
                        </li>
                    </ul>
                </li>
                <li>
                    <h4><span>下载说明</span></h4>
                    <p><span>点击“下载”按钮即可下载相应的项目压缩包。</span></p>
                </li>
            </ul>
        </div>
        <div>
            <h2><a name="词云生成" class="md-header-anchor"></a><span>词云生成</span></h2>
            <ul>
                <li><p><span>本模块通过Scrapy爬取热门网页的数据，经过数据清洗等操作后根据词频和词性进行有限的数据分析与归类，进而生成词云图片。</span></p></li>
                <li><p><span>由于不同网站对于爬虫的限制大相径庭，目前暂只支持豆瓣电影、知乎热榜和CSDN首页这三个网站的词云功能。</span></p></li>
                <li><p><span>具体操作：点击“词云生成”页面，在选择框中选择网页，点击“生成词云”，即可看到该网页对应的词云图片。</span></p></li>
                <li><p><span>词云生成的图片并不是网页目前的实时数据，有一定的时间误差。</span></p></li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "introduction"
    }
</script>

<style scoped>
    .intro_idv li{
        line-height: 30px;
        height: 30px;
    }
</style>