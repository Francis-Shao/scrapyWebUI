<template>
    <div id="wordCloud">
        <el-container>
            <el-header>
                <el-row>
                    <el-col offset="6" span="10">
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
                    <el-col offset="2" span="4">
                        <el-button @click="select_address">确定</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <el-image
                    style="width: 1000px; height: 1000px"
                    :src="url" fit="contain">
                </el-image>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import testImg from "../../static/1_5.jpg"
    export default {
        name: "wordCloud",
        data(){
            return{
                options:[
                    {
                        "value":1,
                        "name":"douban",
                        "address":"http:121.121.121.111"
                    },
                    {
                        "value":2,
                        "name":"ali",
                        "address":"http:121.121.121.111"
                    },
                    {
                        "value":3,
                        "name":"tencent",
                        "address":"http:121.121.121.111"
                    },
                    {
                        "value":4,
                        "name":"baidu",
                        "address":"http:121.121.121.111"
                    },
                    {
                        "value":5,
                        "name":"netease",
                        "address":"http:121.121.121.111"
                    }
                ],
                value:"",
                url:testImg
            }
        },
        methods:{
            select_address(){
                this.$message.success("当前value: "+this.value)
            }
        }
    }
</script>

<style scoped>

</style>