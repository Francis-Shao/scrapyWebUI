<template>
  <div id="app">
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;

    /*margin-top: 60px;*/
    height: 100%;
    margin-top: -10px;
    margin-left: -10px;
    margin-right: -10px;
}
    html{
        height: 100%;
    }
    body{
        height: 100%;
    }
</style>
