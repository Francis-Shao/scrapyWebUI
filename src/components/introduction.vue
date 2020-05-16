<template>
    <div id="introduction" style="float: left ;width: 100%;text-align: left">
        <div class="intro_idv">
            <h2>脚本管理</h2>
            <ul>
                <li><span>主要功能为运行Scrapy项目</span></li>
                <li><span>需要Scrapy项目打包的zip压缩包，项目名和需要运行的脚本名</span></li>
                <li><span>项目名请按照settings的项目填写，否则容易出现未知错误</span></li>
                <li><span>项目运行之后可以查看和下载项目的log输出</span></li>
                <li><span>可以选择在项目运行过程中停止项目</span></li>
                <li><span>项目停止阶段可以删除项目</span></li>
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