<template>
    <div id="wordCloud">
        <el-container>
            <el-header>
                <el-row>
                    <el-col offset="7" span="7">
                        <el-select v-model="value" placeholder="请选择网址">
                            <el-option
                                    v-for="item in options"
                                    :key="item.value"
                                    :label="item.name"
                                    :value="item.value">
                                <span style="float: left">{{ item.name }}</span>
                                <span style="float: right; color: #8492a6; font-size: 13px">{{ item.address }}</span>
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col offset="0" span="1">
                        <el-button @click="select_address">生成词云</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <img v-if="lay_type==1" src="../../static/豆瓣515.png" height="1000" width="1000" alt />
                <img v-if="lay_type==2" src="../../static/知乎515.png" height="1000" width="1000" alt />
                <img v-if="lay_type==3" src="../../static/CSDN515.png" height="1000" width="1000" alt />
            </el-main>
        </el-container>
    </div>
</template>

<script>
    //import img_1 from "../../static/豆瓣515.png"
    export default {
        name: "wordCloud",
        data(){
            return{
                options:[
                    {
                        "value":1,
                        "name":"豆瓣电影",
                        "address":"https://movie.douban.com/"
                    },
                    {
                        "value":2,
                        "name":"知乎热榜",
                        "address":"https://www.zhihu.com/hot"
                    },
                    {
                        "value":3,
                        "name":"CSDN首页",
                        "address":"https://www.csdn.net/"
                    }
                ],
                value:"",
                //url:img_1,
                lay_type:0,
            }
        },
        methods:{
            select_address(){
                if(this.value==1){this.lay_type=1}
                if(this.value==2){this.lay_type=2}
                if(this.value==3){this.lay_type=3}
            }
        }
    }
</script>

<style scoped>

</style>