import Vue from 'vue'
import VueRouter from 'vue-router'
import ui_index from "@/components/ui_index";
import introduction from "@/components/introduction";
import manageSpider from "@/components/manageSpider";
import autoMake from "@/components/autoMake";
import wordCloud from "@/components/wordCloud";

Vue.use(VueRouter)

const routes=[
    {
        path:"/",
        redirect:"/ui_index/introduction"
    },
    {
        path:"/ui_index",
        name:"ui_index",
        component: ui_index,
        children:[
            {
                path:"introduction",
                name:"introduction",
                component:introduction
            },
            {
                path:"manageSpider",
                name:"manageSpider",
                component: manageSpider
            },
            {
                path:"autoMake",
                name:"autoMake",
                component: autoMake
            },
            {
                path:"wordCloud",
                name:"wordCloud",
                component: wordCloud
            },
        ]
    }
]

export default new VueRouter({
    routes
})