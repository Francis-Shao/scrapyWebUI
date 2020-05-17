<template>
    <div style="height: 100%;">
        <el-container style="height: 100%">
            <el-header id="rightHeader" height="50px">
                <div style="height: 50px;width: 95%" v-cloak>
                    <img src="../assets/logo_shell.png" height="40" style="position: relative;float: left" />
                    <span style="color: white;font-family: Georgia;float: left;position: relative;left: 15px" class="anim2">
                        Scrapy UI
                    </span>
                    <span style="float: right" class="anim1" @click="ins">
                        Instructions
                    </span>
                </div>

            </el-header>
            <el-main id="indexMain">
                <el-container class="container" >
                    <el-aside id="asideBar" width="14%" style="background-color: transparent;overflow: hidden;position: relative;top: 10px">
                        <div>

                            <el-menu text-color="#d2d1cd" v-bind:router="true"  id="menu" default-active="introduction" active-text-color="black" >
                                <el-menu-item index="introduction" style="display: none">
                                    <i class="el-icon-menu" id="ins" ></i>
                                    <span>简介</span>
                                </el-menu-item>
                                <el-menu-item index="manageSpider">
                                    <i class="el-icon-menu"></i>
                                    <span slot="title">脚本管理</span>
                                </el-menu-item>
                                <el-menu-item index="autoMake">
                                    <i class="el-icon-menu"></i>
                                    <span slot="title">自动生成</span>
                                </el-menu-item>
                                <el-menu-item index="wordCloud">
                                    <i class="el-icon-menu"></i>
                                    <span slot="title">词云生成</span>
                                </el-menu-item>
                            </el-menu>
                        </div>
                    </el-aside>
                    <el-main>
                        <router-view></router-view>
                    </el-main>
                </el-container>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "ui_index",
        data(){
            return {
                message: "beforeClick"
            }
        },
        methods:{
            ins:function () {
               document.getElementById("ins").click()
            }
        }

    }
</script>

<style scoped>
    /*.el-menu-item{*/
    /*    width: 20%;*/
    /*    float: left;*/
    /*}*/

    #asideBar{
        background-color: #ffffff;
        height: 100%;

    }

    #menu{
        height: 95%;
    }


    #rightHeader{
        background-color: #0a4b53;

        line-height: 50px;
    }

    #indexMain{
        padding: 0;
        height: 90%;

    }

    .el-menu-item{
        height: 50px;
        line-height: 50px;
    }

    .container{
        height:90%
    }
    .anim1 {
        animation-name: anim1;
        animation-duration: 1.3s;
        animation-timing-function:ease-out;
        -webkit-animation-timing-function:ease-out; /* Safari 和 Chrome */
        /*animation-delay: 0.4s;*/
        height: 50px;
        line-height: 50px;
        text-align: left;
        font-family: Georgia;
        font-size: 18px;
        color: white;
    }
    .anim1:hover{
        opacity: 0.6;
        cursor: pointer;
    }
    @keyframes anim1{
        0%{opacity: 0;position: relative;right: 40%}
        99%{opacity: 0.99;position: relative;right: 0%}
    }
    .anim2 {
        animation-name: anim2;
        animation-duration: 1s;
        animation-timing-function:ease-out;
        -webkit-animation-timing-function:ease-out; /* Safari 和 Chrome */
        animation-delay: 0s;
        height: 50px;
        line-height: 50px;
        text-align: left;
        font-size: 18px;
        color: white;
    }
    @keyframes anim2{
        0%{opacity: 0;position:relative;left: -10%;}
        99%{opacity: 0.99;position:relative;right: 0;}
    }
    [v-cloak]{
        display: none;
    }
</style>
